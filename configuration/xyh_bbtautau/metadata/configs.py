from order import Analysis, Campaign
from typing import Literal

from configuration.xyh_bbtautau.metadata.categories import add_categories
from configuration.xyh_bbtautau.metadata.channels import add_channels


def _add_config(
    analysis_inst: Analysis,
    name: str,
    id: int | Literal["+"],
    ecm: float,
    year: int,
    lumi: float,
    postfix: str | None,
    runs: dict[str, tuple[int, int]],
    nano_version: str,
):
    """
    Create the campaign instance and add it to the analysis to create the
    config instance.
    """

    campaign_inst = Campaign(
        name=name,
        id=id,
        ecm=ecm,
        aux={
            "year": year,
            "lumi": lumi,
            "postfix": postfix,
            "runs": runs,
            "nano_version": nano_version,
        },
    )
    config_inst = analysis_inst.add_config(campaign=campaign_inst)

    # Add configuration objects to the campaign's config instance
    add_channels(config_inst)
    add_categories(config_inst)
    # add_dataset_insts(config_inst)
    # add_process_insts(config_inst)
    # add_variable_insts(config_inst)


def add_configs(analysis_inst: Analysis):
    """
    Add configurations related to specific data-taking campaigns to the
    :py:class:`~order.Analysis` instance.

    :param analysis_inst: The :py:class:~order.Analysis` that the configuration
        is added to.
    """

    # 2022preEE
    _add_config(
        analysis_inst,
        name="2022preEE",
        id="+",
        year=2022,
        postfix="preEE",
        ecm=13.6,
        lumi=7.9804,  # fb^-1
        runs={"C": [355794, 357486], "D": [357487, 359021]},
        nano_version="v12",
    )

    # 2022postEE
    _add_config(
        analysis_inst,
        name="2022postEE",
        id="+",
        year=2022,
        postfix="postEE",
        ecm=13.6,
        lumi=26.6717,  # fb^-1
        runs={
            "E": [359022, 360331],
            "F": [360332, 362180],
            "G": [362350, 362760],
        },
        nano_version="v12",
    )

    # 2023preBPix
    _add_config(
        analysis_inst,
        name="2023preBPix",
        id="+",
        year=2023,
        postfix="preBPix",
        ecm=13.6,
        lumi=18.063,  # fb^-1
        runs={
            "C": [367080, 369802],
        },
        nano_version="v12",
    )

    # 2023postBPix
    _add_config(
        analysis_inst,
        name="2023postBPix",
        id="+",
        year=2023,
        postfix="postBPix",
        ecm=13.6,
        lumi=9.693,  # fb^-1
        runs={
            "D": [369803, 372415],
        },
        nano_version="v12",
    )

    # 2024
    _add_config(
        analysis_inst,
        name="2024",
        id="+",
        year=2024,
        postfix=None,
        ecm=13.6,
        lumi=108.83,  # fb^-1
        runs={
            "C": [378971, 379411],
            "D": [379412, 380252],
            "E": [380948, 381943],
            "F": [381944, 383779],
            "G": [383780, 385813],
            "H": [385814, 386408],
            "I": [386409, 387121],
        },
        nano_version="v15",
    )

