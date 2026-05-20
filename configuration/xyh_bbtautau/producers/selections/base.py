from collections import OrderedDict
from itertools import chain

from order import Category, Channel

from bbtautau.shapes import AnalysisContext
from configuration.xyh_bbtautau.producers.selections.gen import (
    tautau_from_genuine_tau_selection,
    tautau_from_jet_fake_selection,
    tautau_from_remaining_selection,
)
from configuration.xyh_bbtautau.producers.selections.jets import bb_pair, jet_vetomap
from configuration.xyh_bbtautau.producers.selections.leptons import (
    lepton_vetoes,
    ll_pair,
)
from configuration.xyh_bbtautau.producers.selections.triggers import triggers


def modify_selection_for_abcd_categories(
    selections: OrderedDict,
    category: Category,
    channel: Channel,
) -> OrderedDict:
    # If the category has tag "ss", it means that we should apply a
    # same-sign charge selection for the dilepton candidate
    # TODO Rename key
    if category.has_tag({"ss"}):
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
    if category.has_tag({"antiid"}):
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
            selections[f"tau{i}_id_vs_jet"] = antiid_vs_jet_tpl.format(index=i)

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
    if category.has_tag({"antiid"}):
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
            selections[f"tau{i}_id_vs_jet"] = antiid_vs_jet_tpl.format(index=i)

        else:
            # Channels without a hadronic tau do not have such a region
            pass

    return selections


def gen_selection(
    analysis_context: AnalysisContext,
):
    # Store for process-specific generator-level selections
    selections = OrderedDict()

    # # Add generator-level selection for DY -> ee and DY -> mumu processes
    # if (
    #     analysis_context.process.has_tag({"dy", "ee"}, mode=all)
    #     or analysis_context.process.has_tag({"dy", "mumu"}, mode=all)
    # ):
    #     selections.update(z_ee_mumu_gen_selection(analysis_context))

    # # Add generator-level selection for DY -> tautau processes
    # if analysis_context.process.has_tag({"dy", "tautau"}, mode=all):
    #     selections.update(z_tautau_gen_selection(analysis_context))

    # Add generator-level selections for the different tau decay modes for processes with hadronic taus
    if analysis_context.process.has_tag({"tautau_genuine"}):
        selections.update(tautau_from_genuine_tau_selection(analysis_context))
    if analysis_context.process.has_tag({"tautau_jetfakes"}):
        selections.update(tautau_from_jet_fake_selection(analysis_context))
    if analysis_context.process.has_tag({"tautau_remaining"}):
        selections.update(tautau_from_remaining_selection(analysis_context))

    return selections


def channel_selection(
    analysis_context: AnalysisContext,
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
        be tailored. The attributes used in this function are
        :py:attr:`~shape_producer.operations.AnalysisContext.campaign` and
        :py:attr:`~shape_producer.operations.AnalysisContext.channel`.

    :return: Collection of filter operations.
    """

    # Concatenate base selections from sub-steps
    selections = OrderedDict(
        list(
            chain(
                # Chain the trigger, veto, dilepton, and di-b jet selections
                triggers(analysis_context).items(),
                lepton_vetoes(analysis_context).items(),
                ll_pair(analysis_context).items(),
                jet_vetomap(analysis_context).items(),
                bb_pair(analysis_context).items(),
            )
        )
    )

    # Category-specific modifications
    if analysis_context.category.has_tag({"signal_cat"}):
        # For the base categories, the base selection can be returned
        pass

    elif analysis_context.category.has_tag({"abcd"}):
        # Alter the ID and SS/OS selections for ABCD categories
        selections = modify_selection_for_abcd_categories(
            selections,
            analysis_context.channel,
            analysis_context.category,
        )

    elif analysis_context.category.has_tag({"ff"}):
        # Alter the ID selection for this category
        selections = modify_selection_for_fake_factor_categories(
            selections,
            analysis_context.channel,
            analysis_context.category,
        )

    return selections
