from collections import OrderedDict
from order import Campaign, Channel

from configuration.xyh_bbtautau.producers.helpers import requires


@requires()
def z_pt_reweighting() -> OrderedDict[str, str]:
    """
    Apply the Z boson $p_{\\text{T}}$ reweighting.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. In this function, the argument only serves as a
        placeholder to fulfill the expected signature required by other parts
        of this code.

    :return: A collection of weight operations for the Z pt reweighting.
    """

    return OrderedDict(
        [
            (
                "z_pt_weight",
                "ZPtMassReweightWeight",
            ),
        ],
    )


@requires()
def tt_top_pt_reweighting_weights() -> OrderedDict[str, str]:
    """
    Apply the top quark $p_{\\text{T}}$ reweighting.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. In this function, the argument only serves as a
        placeholder to fulfill the expected signature required by other parts
        of this code.

    :return: A collection of weight operations for the top pt reweighting.
    """

    return OrderedDict(
        [
            (
                "top_pt_weight",
                "topPtReweightWeight",
            ),
        ],
    )


@requires(
    metadata={"campaign", "channel"},
)
def tt_normalization_weights(
    *,
    campaign: Campaign,
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Weight to scale $\\text{t}\\bar{\\text{t}}$ normalization to value that
    has been observed in an $\\text{e}\\mu$ control region.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. In this function, the argument only serves as a
        placeholder to fulfill the expected signature required by other parts
        of this code.

    :return: A collection of weight operations for the ttbar normalization.
    """

    # tt normalization factors per era
    normalization_factor = {
        "2022preEE": 0.91,
        "2022postEE": 0.89,
        "2023preBPix": 0.85,
        "2023postBPix": 0.83,
        "2024": 0.90,
    }[campaign.name]

    if channel.name == "em":
        return OrderedDict([])

    return OrderedDict(
        [
            (
                "tt_normalization_weight",
                f"{normalization_factor}",
            ),
        ],
    )

