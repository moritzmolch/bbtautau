from collections import OrderedDict
from itertools import chain
from order import Category, Campaign, Channel

from configuration.xyh_bbtautau.producers.helpers import requires
from configuration.xyh_bbtautau.producers.selections.triggers import triggers
from configuration.xyh_bbtautau.producers.selections.leptons import lepton_vetoes, ll_pair
from configuration.xyh_bbtautau.producers.selections.jets import jet_vetomap, bb_pair


def modify_selection_for_abcd_categories(
    selections: OrderedDict,
    category: Category,
    channel: Channel,
) -> OrderedDict:
    # If the category has tag "ss", it means that we should apply a
    # same-sign charge selection for the dilepton candidate
    # TODO Rename key
    if category.has_tags({"ss"}):
        selections["ll_pair_os"] = "((q_1 * q_2) > 0)"

    # If the category has tag "antiid", it means that we should apply:
    # - A selection for the leading tau to pass the VVVLoose and to not
    #   pass the Medium WP for the DeepTau ID vs. jets in the et, mt, and
    #   tt channels.
    # - A selection for the leading muon to not pass the tight WP of the
    #   relative muon isolation (< 0.15) in the em and mm channels.
    # - A selection for the leading electron to not pass the MVA-based
    #   electron ID (with isolation variables) at the 90% efficiency WP
    #   in the ee channel.
    if category.has_tags({"antiid"}):

        if channel.name in ["et", "mt", "tt"]:
            # Get the working points for the tau ID depending on the channel
            id_vs_jet_wp = channel.x.tau["id_vs_jet_wp"]
            antiid_vs_jet_wp = channel.x.tau["antiid_vs_jet_wp"]

            # Construct anti-ID selection string templates with index as
            # parameter
            antiid_vs_jet_tpl = f"""
            (
                (id_tau_vsJet_{antiid_vs_jet_wp}_{{index}} > 0.5)
                && (id_tau_vsJet_{id_vs_jet_wp}_{{index}} < 0.5)
            )
            """

            # Add anti-ID tau selection for
            # - for the first lepton in the tt channel,
            # - the second lepton in the et and mt channels.
            # TODO Remove corresponding ID selection, i.e., rename key
            indices = {
                "et": 2,
                "mt": 2,
                "tt": 1,
            }
            i = indices[channel.name]
            selections[f"tau{i}_id_vs_jet"] = antiid_vs_jet_tpl.format(
                index=i
            )

        if channel.name in ["em", "mm"]:
            # Add anti-isolation muon selection for
            # - for the first lepton in the mm channel,
            # - the second lepton in the em channel.
            # TODO Remove corresponding isolation selection, i.e., rename key
            indices = {
                "em": 2,
                "mm": 1,
            }
            i = indices[channel.name]
            selections[f"muon{i}_iso"] = f"(iso_{i} > 0.15) && (iso_{i} < 0.4)"

        if channel.name in ["ee"]:
            # Add anti-isolation electron selection for leading lepton in ee
            # channel.
            # TODO Remove corresponding ID selection, i.e., rename key
            selections[f"electron{i}_iso"] = f"(iso_{i} > 0.15) && (iso_{i} < 0.4)"

    return selections


def modify_selection_for_fake_factor_categories(
    selections: OrderedDict,
    category: Category,
    channel: Channel,
) -> OrderedDict:

    # If the category has tag "antiid", it means that we should apply:
    # - A selection for the leading tau to pass the VVVLoose and to not
    #   pass the Medium WP for the DeepTau ID vs. jets in the et, mt, and
    #   tt channels.
    # - A selection for the leading muon to not pass the tight WP of the
    #   relative muon isolation (< 0.15) in the em and mm channels.
    # - A selection for the leading electron to not pass the MVA-based
    #   electron ID (with isolation variables) at the 90% efficiency WP
    #   in the ee channel.
    if category.has_tags({"antiid"}):

        if channel.name in ["et", "mt", "tt"]:
            # Get the working points for the tau ID depending on the channel
            id_vs_jet_wp = channel.x.tau["id_vs_jet_wp"]
            antiid_vs_jet_wp = channel.x.tau["antiid_vs_jet_wp"]

            # Construct anti-ID selection string templates with index as
            # parameter
            antiid_vs_jet_tpl = f"""
            (
                (id_tau_vsJet_{antiid_vs_jet_wp}_{{index}} > 0.5)
                && (id_tau_vsJet_{id_vs_jet_wp}_{{index}} < 0.5)
            )
            """

            # Add anti-ID tau selection for
            # - for the first lepton in the tt channel,
            # - the second lepton in the et and mt channels.
            # TODO Remove corresponding ID selection, i.e., rename key
            indices = {
                "et": 2,
                "mt": 2,
                "tt": 1,
            }
            i = indices[channel.name]
            selections[f"tau{i}_id_vs_jet"] = antiid_vs_jet_tpl.format(
                index=i
            )

        else:
            # Channels without a hadronic tau do not have such a region
            pass

    return selections


@requires(
    metadata={"campaign", "channel", "category"}
)
def default_selection(
    *,
    campaign: Campaign,
    channel: Channel,
    category: Category,
) -> OrderedDict[str, str]:
    """
    The base selection of the analysis, including:

    - The trigger selection with single-electron, single-muon, or
      double-tau triggers, based on the considered channel. The trigger type
      and thresholds might also depend on the data-taking campaign.

    - The veto selection, including additional-lepton and di-lepton vetoes, as
      well as vetoes on events with jets in regions appearing in the JME
      vetomaps.

    - The selection of the two opposite-sign lepton candidates. Quality
      criteria for electrons, muons, and hadronc taus are included depending
      on the analysis channel.

    - The selection of two viable b-jet candidates.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. Attributes used in this function are
        :py:attr`~shape_producer.operations.AnalysisContext.campaign` and
        :py:class`~shape_producer.operations.AnalysisContext.channel`.

    :return: A collection of filter operations for the base selection.
    """

    # Concatenate selections from sub-steps
    selections = OrderedDict(list(chain(
        # Chain the trigger, veto, dilepton, and di-b jet selections
        triggers(campaign, channel),
        lepton_vetoes(channel),
        ll_pair(channel),
        jet_vetomap(),
        bb_pair(),
    )))

    if category.has_tags({"signal_cat"}):
        # For the base categories, the base selection can be returned
        pass

    elif category.has_tags({"abcd"}):
        # Alter the ID and SS/OS selections for ABCD categories
        selections = modify_selection_for_abcd_categories(
            selections,
            channel,
            category,
        )

    elif category.has_tags({"ff"}):
        # Alter the ID selection for this category
        selections = modify_selection_for_fake_factor_categories(
            selections,
            channel,
            category,
        )

    return selections

