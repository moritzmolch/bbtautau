from law import CSVParameter
from luigi import BoolParameter, IntParameter, Parameter

from bbtautau.process_spec import ProcessSpec
from bbtautau.shapes import (
    create_ntuple_processor_datasets,
    create_ntuple_processor_units,
    has_all_shapes,
)
from bbtautau.tasks.base.mixins import VariablesMixin
from bbtautau.tasks.base.tasks import BaseTask
from bbtautau.tasks.xsec_friends import XSecFriend
from bbtautau.util import load_object
from configuration.helper_collection import PreserveROOTPathsAsStrings
from configuration.ntuple_processor_config_helper import (
    add_paths,
    get_config_formatter,
)
from ntuple_processor import GraphManager, RunManager, UnitManager


class Shapes(BaseTask, VariablesMixin):
    ntuple_tag = Parameter(
        description="Version tag for the ntuple production.",
    )

    shapes_tag = Parameter(
        description="Version tag for the shape production.",
    )

    ntuple_base_dir = Parameter(
        description="Base directory of the ntuples.",
    )

    process_spec = Parameter(
        description="Path to the process specification file.",
    )

    friend_names = CSVParameter(
        description="List friend trees, which shall be included.",
    )

    selection_func = Parameter(
        description="Module path to the selection.",
    )

    optimization_level = IntParameter(
        description="Level of optimization for the graph manager.",
        default=0,
    )

    variations = CSVParameter(
        description=("List of histogram variations to process",),
        default=[],
    )

    np_workers = IntParameter(
        description="Number of parallel workers used for ntuple processor",
        default=1,
    )

    np_threads = IntParameter(
        description=(
            "Number of parallel threads within a worker used for ntuple " + "processor"
        ),
        default=1,
    )

    cut_and_weight_config = BoolParameter(
        description=(
            "Flag for not processing the shapes, but only creating a YAML "
            + " file with the cut and weight configuration."
        )
    )

    def requires(self):
        return {
            "XSecFriend": XSecFriend.req(self, channel=self.channel_inst.name),
        }

    def output(self):
        if self.cut_and_weight_config:
            return self.local_target(
                self.shapes_tag,
                self.campaign_inst.name,
                self.category_inst.name,
                "selection_and_weights.yaml",
            )
        else:
            return self.local_target(
                self.shapes_tag,
                self.campaign_inst.name,
                self.category_inst.name,
                "shapes.root",
            )

    def complete(self):
        is_complete = super().complete()
        if not is_complete:
            return is_complete

        if self.cut_and_weight_config:
            return is_complete

        # Load the process specification
        process_spec = ProcessSpec(
            process_spec_file=self.process_spec,
            config=self.config_inst,
            channel=self.channel_inst,
        )

        # Check if all shapes exist
        all_exist = has_all_shapes(
            self.output().path,
            process_spec,
            self.campaign_inst,
            self.category_inst,
            self.variable_insts,
            variations=self.variations,
        )

        return all_exist

    def run(self):
        # Load the selection and weight functions
        selection_func = load_object(self.selection_func)

        # Load the process specification
        process_spec = ProcessSpec(
            process_spec_file=self.process_spec,
            config=self.config_inst,
            channel=self.channel_inst,
        )

        # Create the datasets for the ntuple processor
        np_datasets = create_ntuple_processor_datasets(
            self.campaign_inst,
            self.channel_inst,
            process_spec,
            self.ntuple_base_dir,
            self.ntuple_tag,
            self.shapes_tag,
            self.friend_names,
        )

        # Create the histogram units for the ntuple processor
        np_units = create_ntuple_processor_units(
            process_spec,
            selection_func,
            np_datasets,
            self.analysis_inst,
            self.config_inst,
            self.campaign_inst,
            self.channel_inst,
            self.category_inst,
            self.variable_insts,
            variations=self.variations,
        )

        # Create the unit manager and book actions to perform
        unit_manager = UnitManager()
        for unit, variations in np_units:
            unit_manager.book(
                [unit],
                variations=[v for v_list in variations.values() for v in v_list],
                enable_check=True,
            )

        # Create the graph manager
        graph_manager = GraphManager(unit_manager.booked_units, True)
        graph_manager.optimize(self.optimization_level)
        graphs = graph_manager.graphs

        if self.cut_and_weight_config:
            # Run the graphs to create the configuration
            if not self.output().parent.exists():
                self.output().parent.touch()
            run_manager = RunManager(
                graphs,
                create_histograms=False,
                create_config=True,
                config_formatter=get_config_formatter(era=self.campaign_inst.name),
            )
            run_manager.nthreads = 1

            # Create config for each graph in the manager
            for graph in graphs:
                run_manager.node_to_root(graph)
                add_paths(
                    graph=graph,
                    channel=self.channel_inst.name,
                    era=self.campaign_inst.name,
                    r_manager=run_manager,
                )
            config = run_manager.config.regular

            # Dump the configuration to YAML file
            self.output().dump(
                config,
                formatter="yaml",
                default_flow_style=False,
                Dumper=PreserveROOTPathsAsStrings,
            )

        else:
            # Run the graphs
            if not self.output().parent.exists():
                self.output().parent.touch()
            run_manager = RunManager(graphs)
            run_manager.run_locally(
                self.output().path,
                self.np_workers,
                self.np_threads,
            )
