from collections import OrderedDict

from bbtautau.shapes import AnalysisContext


def z_pt_reweighting(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Apply the Z boson $p_{\\text{T}}$ reweighting.

    :param analysis_context: Analysis context, to which the weights should
        be tailored. This is just a placeholder to provide a consistent
        interface for all weight modules.

    :return: Collection of weight definitions.
    """

    return OrderedDict(
        [
            (
                "z_pt_weight",
                "ZPtMassReweightWeight",
            ),
        ],
    )


def top_pt_reweighting(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Apply the top quark $p_{\\text{T}}$ reweighting.

    :param analysis_context: Analysis context, to which the weights should
        be tailored. This is just a placeholder to provide a consistent
        interface for all weight modules.

    :return: A collection of weight definitions.
    """

    return OrderedDict(
        [
            (
                "top_pt_weight",
                "topPtReweightWeight",
            ),
        ],
    )


def tt_normalization(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Weight to scale $\\text{t}\\bar{\\text{t}}$ normalization to value that
    has been observed in an $\\text{e}\\mu$ control region.

    :param analysis_context: Analysis context, to which the weights should
        be tailored. Attributes used in this function are
        :py:attr`~bbtautau.producers.AnalysisContext.campaign` and
        :py:class`~bbtautau.producers.AnalysisContext.channel`.

    :return: A collection of weight definitions.
    """

    # Get the campaign and the channel from the analysis context
    campaign = analysis_context.campaign
    channel = analysis_context.channel

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
