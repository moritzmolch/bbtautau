from collections import OrderedDict

from bbtautau.shapes import AnalysisContext


def jet_vetomap(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Apply vetoes on events with jets in vetomap regions. The
    function returns an ordered dictionary with the filter names as keys and the
    ROOT expressions for the selections as values.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. This is just a placeholder to provide a consistent
        interface for all selection modules.

    :return: Collection of filter operations.
    """

    # Storage for all vetoes
    selections = OrderedDict()

    # Jet vetomap selection
    selections["jet_vetomap_veto"] = "(jet_vetomap_veto < 0.5)"

    return selections


def bb_pair(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Selection of the bb pair. The function returns an ordered dictionary with
    the filter names as keys and the ROOT expressions for the selections as values.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. This is just a placeholder to provide a consistent
        interface for all selection modules.

    :return: Collection of filter operations.
    """

    # Storage for all bb pair selections
    selections = OrderedDict()

    # Select events with at least one medium b-tagged jet
    selections["nbtag_selection"] = "(n_bjets >= 1)"

    # Select events with at least one b-tagged jets and at least two valid b
    # candidates
    selections["bb_pair_kinematics"] = "(bpair_pt_1 > 20) && (bpair_pt_2 > 20)"

    # Require a minimum spatial separation of the two b candidates
    selections["bb_pair_delta_r"] = "(bpair_deltaR > 0.4)"

    return selections
