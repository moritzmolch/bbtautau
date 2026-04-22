import law
from law.contrib.wlcg import WLCGDirectoryTarget, WLCGFileSystem
from luigi import Parameter
import os

from bbtautau.process_spec import ProcessSpec
from bbtautau.tasks.base.tasks import BaseTask
from bbtautau.tasks.base.mixins import ChannelMixin
from bbtautau.ntuples.friends import XSecFriendProducer


class XSecFriend(BaseTask, law.LocalWorkflow, ChannelMixin):

    ntuple_tag = Parameter(
        description="Version tag for the ntuple production.",
    )

    ntuple_base_dir = Parameter(
        description="Base directory of the ntuples.",
    )

    process_spec = Parameter(
        description="Path to the process specification file.",
    )

    def create_branch_map(self):
        # Load the process specification
        process_spec = ProcessSpec(
            process_spec_file=self.process_spec,
            config=self.config_inst,
            channel=self.channel_inst,
        )

        # Get flat list of all datasets required by the process specs, only
        # include simulated samples
        dataset_insts_gen = (
            d
            for g in process_spec.get_all_process_groups()
            for p in g.processes.values()
            for d in p.datasets.values()
            if not d.is_data
        )

        # Create a branch for each dataset
        branch_map = {
            i: {
                "dataset": dataset_inst,
                "friend_producer": XSecFriendProducer(
                    self.ntuple_base_dir,
                    self.ntuple_tag,
                    self.campaign_inst,
                    self.channel_inst,
                    dataset_inst,
                )
            }
            for i, dataset_inst in enumerate(dataset_insts_gen)
        }

        return branch_map

    def get_ntuple_wlcg_fs(self):
        # Construct a WLCGFileSystem for ntuple location
        fs = WLCGFileSystem(base=self.ntuple_base_dir)

        return fs

    def output(self):
        # Get the friend producer object from the branch data
        friend_producer = self.branch_data["friend_producer"]

        # Use output folders of friends for all nicks of the dataset in the
        # considered branch
        output = [
            WLCGDirectoryTarget(
                os.path.relpath(
                    output_dir,
                    start=self.ntuple_base_dir,
                ),
                fs=self.get_ntuple_wlcg_fs(),
            )
            for output_dir in friend_producer.get_output_dirs()
        ]

        return output

    def run(self):
        # Get the friend producer and dataset metadata from the branch data
        friend_producer = self.branch_data["friend_producer"]
        dataset_inst = self.branch_data["dataset"]

        # Run the friend production
        with self.publish_step(
            "\n".join(
                (
                    "Run 'xsec' friend production",
                    f"    campaign: {self.campaign_inst.name}",
                    f"    channel:  {self.channel_inst.name}",
                    f"    dataset:  {dataset_inst.name}",
                )
            )
        ):
            friend_producer.run()

