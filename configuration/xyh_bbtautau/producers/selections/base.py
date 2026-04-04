from collections import OrderedDict
from itertools import chain
from order import Campaign, Channel

from configuration.xyh_bbtautau.producers.helpers import requires
from configuration.xyh_bbtautau.producers.selections.triggers import triggers
from configuration.xyh_bbtautau.producers.selections.leptons import lepton_vetoes, ll_pair
from configuration.xyh_bbtautau.producers.selections.jets import jet_vetomap, bb_pair


@requires(
    metadata={"campaign", "channel"}
)
def base_selection(
    *,
    campaign: Campaign,
    channel: Channel,
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

    return selections

