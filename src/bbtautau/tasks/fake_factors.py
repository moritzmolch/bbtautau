import ROOT
from law import CSVParameter
from luigi import IntParameter, Parameter
from order import Process, UniqueObjectIndex

from bbtautau.fake_factor_shapes import get_fake_factor_histograms
from bbtautau.process_spec import ProcessSpec
from bbtautau.tasks.base.mixins import VariablesMixin
from bbtautau.tasks.base.tasks import BaseTask
from bbtautau.tasks.shapes import Shapes


class FakeFactorShapes(BaseTask, VariablesMixin):
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

    def requires(self):
        return {
            "Shapes": Shapes.req(self),
        }

    def output(self):
        return self.local_target(
            self.shapes_tag,
            self.campaign_inst.name,
            self.category_inst.name,
            "shapes.root",
        )

    def run(self):
        # Load the process specification
        process_spec = ProcessSpec(
            process_spec_file=self.process_spec,
            config=self.config_inst,
            channel=self.channel_inst,
        )

        # Get the data and all background processes from the process
        # specification that are _not_ jet fakes
        background_processes = [
            p for g in process_spec.backgrounds for p in g.processes.values()
        ]

        # Get
        # - the data process (for the base estimate)
        # - the jet fakes process (for final fake factor shape)
        # - all background processes that are not jet fakes (for the
        #   subtraction of non-jet-fake contamination)
        data_process = next(iter(process_spec.data[0].processes.values()))
        jetfakes_process = next(
            (p for p in background_processes if p.name == "jetfakes")
        )
        subtract_processes = UniqueObjectIndex(
            Process,
            [
                p
                for p in background_processes
                if not p.has_tag("tautau_jetfakes") and p != jetfakes_process
            ],
        )

        # Get the name of the fake factor variation TODO make this an argument
        variation = "tau_antiid_vs_jet"

        # Get the fake factor histograms with non-jet-fake subtraction
        histograms = get_fake_factor_histograms(
            self.input()["Shapes"].path,
            self.category_inst,
            jetfakes_process,
            data_process,
            subtract_processes,
            variation,
            [v.name for v in self.variable_insts],
        )

        # Dump all histograms into a single output file
        if not self.output().parent.exists():
            self.output().parent.touch()
        rf = ROOT.TFile.Open(self.output().path, "RECREATE")
        for h in histograms:
            h.Write()
        rf.Close()
