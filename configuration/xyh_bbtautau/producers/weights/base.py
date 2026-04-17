from collections import OrderedDict
from itertools import chain

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
from configuration.xyh_bbtautau.producers.weights.processes import (
    top_pt_reweighting,
    tt_normalization,
    z_pt_reweighting,
)
from bbtautau.shapes import AnalysisContext


def mc_weights(
    analysis_context: AnalysisContext,
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

    # Do not apply any weights for data
    if analysis_context.process.is_data:
        return OrderedDict()

    # Get the base weights for simulation
    weights = OrderedDict(
        [
            (name, expression)
            for name, expression in chain(
                triggers(analysis_context).items(),
                normalization(analysis_context).items(),
                pileup(analysis_context).items(),
                electrons(analysis_context).items(),
                muons(analysis_context).items(),
                hadronic_taus(analysis_context).items(),
                b_jets(analysis_context).items(),
            )
        ]
    )

    # Add Z pt reweighting for DY samples
    if analysis_context.process.has_tag({"dy"}):
        weights.update(z_pt_reweighting(analysis_context))

    # Add top pt reweighting and tt normalization weights for tt samples
    if analysis_context.process.has_tag({"tt"}):
        weights.update(top_pt_reweighting(analysis_context))
        weights.update(tt_normalization(analysis_context))

    return weights
