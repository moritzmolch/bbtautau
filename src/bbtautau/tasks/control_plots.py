from law import CSVParameter
from luigi import Parameter

from bbtautau.plots import load_histograms, prepare_histograms, plot
from bbtautau.process_spec import ProcessSpec
from bbtautau.tasks.base.mixins import VariablesMixin
from bbtautau.tasks.base.tasks import BaseTask
from bbtautau.tasks.shapes import Shapes


class ControlPlots(BaseTask, VariablesMixin):

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

    extensions = CSVParameter(
        description="Image extensions of the output plots.",
        default=["pdf", "png"],
    )

    def requires(self):
        return {
            "Shapes": Shapes.req(self),
        }

    def output(self):
        return {
            (v, ext): self.local_target(
                self.shapes_tag,
                self.campaign_inst.name,
                self.category_inst.name,
                f"{v}.{ext}",
            )
            for v in self.variables
            for ext in self.extensions
        }

    def run(self):
        # Load the process specification
        process_spec = ProcessSpec(
            process_spec_file=self.process_spec,
            config=self.config_inst,
            channel=self.channel_inst,
        )

        # Load the individual process histograms and prepare them for plots
        histograms = load_histograms(self.input()["Shapes"].path)
        histograms = prepare_histograms(
            process_spec,
            histograms,
            self.category_inst,
            self.variable_insts,
        )

        # Create plots for all variables and extensions
        for variable_inst in self.variable_insts.values():
            fig, ax = plot(
                histograms,
                self.campaign_inst,
                self.category_inst,
                variable_inst,
            )
            for ext in self.extensions:
                output = self.output()[(variable_inst.name, ext)]
                if not output.parent.exists():
                    output.parent.touch()
                fig.savefig(output.path)

