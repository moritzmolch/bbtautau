from collections import OrderedDict
from itertools import chain
from order import Campaign, Channel

from configuration.xyh_bbtautau.producers.helpers import requires
from configuration.xyh_bbtautau.producers.weights.event import (
    pileup,
    normalization,
)

from configuration.xyh_bbtautau.producers.weights.jets import b_jets
from configuration.xyh_bbtautau.producers.weights.leptons import (
    electrons,
    muons,
    hadronic_taus,
)
from configuration.xyh_bbtautau.producers.weights.triggers import triggers


@requires(
    metadata={"campaign", "channel"}
)
def default_weights(
    *,
    campaign: Campaign,
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Base weights to be applied to events in all MC samples.

    The application of the weights satisfies the following purposes:

    - Weights for trigger efficiency corrections.

    - Weights for correction of the pileup profile.

    - Weights for correction of the electron identification and isolation
      efficiencies (only needed in channels with electrons).

    - Weights for correction of the muon identification and isolation
      efficiencies (only needed in channels with muons).

    - Weights for correction of the tau identification efficiencies with the
      `DeepTau` neural network
      - of genuine taus for the vs. jets discriminator,
      - of genuine electrons for the vs electrons discriminator,
      - of genuine muons for the vs muons discriminator
      (only needed in channels with hadronic taus).

    - Weights for correction of the shape of the b jet score distribution.

    - Normalization weights to match the recored luminosity and the expected
      total cross section of the process.

    :param analysis_context: Analysis context, to which the weights should
        be tailored. Attributes used in this function are
        :py:attr`~shape_producer.operations.AnalysisContext.campaign` and
        :py:class`~shape_producer.operations.AnalysisContext.channel`.

    :return: A collection of weight operations for the base weights for MC
        processes.
    """

    weights = OrderedDict(
        [
            (name, expression)
            for name, expression in chain(
                triggers(campaign, channel).items(),
                pileup().items(),
                electrons(channel).items(),
                muons(channel).items(),
                hadronic_taus(channel).items(),
                b_jets().items(),
                normalization(campaign).items(),
            )
        ]
    )

    return weights

