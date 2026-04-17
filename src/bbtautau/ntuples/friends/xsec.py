import os
from ROOT import TFile, TTree, RDataFrame
from XRootD.client import glob as xrd_glob

from bbtautau.ntuples import get_ntuple_friend_dir, get_ntuple_main_dir


class XSecFriendProducer():

    def __init__(
        self,
        ntuple_base_dir,
        ntuple_tag,
        campaign,
        channel,
        dataset,
    ):
        self.ntuple_base_dir = ntuple_base_dir
        self.ntuple_tag = ntuple_tag
        self.campaign = campaign
        self.channel = channel
        self.dataset = dataset

    def get_input_files(self) -> list[str]:
        # List of input files
        input_files = []

        # Find input files for all nicks of the dataset 
        for nick in self.dataset.x.nicks:
            input_files.extend(
                xrd_glob(
                    os.path.join(
                        get_ntuple_main_dir(
                            self.ntuple_base_dir,
                            self.ntuple_tag,
                        ),
                        self.campaign.name,
                        nick,
                        self.channel.name,
                        "*.root",
                    )
                )
            )

        return input_files

    def get_output_dirs(self) -> str:
        # Construct output directories for all nicks of the dataset
        output_dirs = [
            os.path.join(
                get_ntuple_friend_dir(
                    self.ntuple_base_dir,
                    self.ntuple_tag,
                    "xsec",
                ),
                self.campaign.name,
                nick,
                self.channel.name,
            )
            for nick in self.dataset.x.nicks
        ]

        return output_dirs

    def get_output_file(
        self,
        input_file: str,
    ) -> str:
        # Split input file name to get the nick and the basename
        nick = os.path.basename(os.path.dirname(os.path.dirname(input_file)))
        basename = os.path.basename(input_file)

        # Construct output file path
        output_file = os.path.join(
            get_ntuple_friend_dir(
                self.ntuple_base_dir,
                self.ntuple_tag,
                "xsec",
            ),
            self.campaign.name,
            nick,
            self.channel.name,
            basename,
        )

        return output_file

    def input_file_is_empty(
        self,
        input_file: str,
    ) -> bool:
        # Open the file and check if 'ntuple' tree is present in file
        f = TFile.Open(input_file, "READ")
        has_ntuple_tree = "ntuple" not in [
            k.GetTitle() for k in f.GetListOfKeys()
        ]
        f.Close()
        return has_ntuple_tree

    def run_empty_file(
        self,
        input_file: str,
        output_file: str,
    ):
        # Write an empty tree 'ntuple' to the output file
        f = TFile.Open(input_file, "READ")
        tree = TTree("ntuple", "ntuple")
        tree.Write()
        f.Close()

    def run_populated_file(
        self,
        input_file: str,
        output_file: str,
    ):
        # Get the number of events, cross section, and generator weight from
        # the dataset object
        n_events = self.dataset.n_events
        xsec = self.dataset.x.xsec
        generator_weight = self.dataset.x.generator_weight

        # Create a new data frame
        rdf = RDataFrame("ntuple", input_file)

        # Define columns in the RDataFrame
        rdf = rdf.Define(
            "numberGeneratedEventsWeight",
            f"(float) {1 / n_events}",
        )
        rdf = rdf.Define(
            "negative_events_fraction",
            f"(float) {generator_weight}",
        )
        rdf = rdf.Define(
            "crossSectionPerEventWeight",
            f"(float) {xsec}",
        )

        # Write RDataFrame to output location
        rdf.Snapshot(
            "ntuple",
            output_file,
            [
                "numberGeneratedEventsWeight",
                "negative_events_fraction",
                "crossSectionPerEventWeight",
            ],
        )

    def run_single_file(
        self,
        input_file: str,
        output_file: str,
    ):
        # Dispatch to the correct function to write data to the output file
        if self.input_file_is_empty(input_file):
            return self.run_empty_file(input_file, output_file)
        else:
            return self.run_populated_file(input_file, output_file)

    def run(self):
        # Loop through all input files and run friend tree creation
        for input_file in self.get_input_files():
            output_file = self.get_output_file(input_file)
            self.run_single_file(input_file, output_file)

