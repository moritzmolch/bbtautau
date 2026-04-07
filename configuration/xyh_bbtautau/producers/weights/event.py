from collections import OrderedDict
from order import Campaign

from configuration.xyh_bbtautau.producers.helpers import requires


@requires(
    metadata={"campaign"},
)
def normalization(
    *,
    campaign: Campaign,
) -> OrderedDict[str, str]:
    """
    Calculate weights to normalize MC histograms to the integrated luminosity
    and the expected theory cross section. The function returns an ordered
    dictionary with the weight names as keys and the ROOT expression to define
    the weight as values.
    """

    # Empty storage for new weights
    weights = OrderedDict()

    # TODO make this function dataset-dependent to be able to inject cross

    # Set the luminosity weight depending on the era
    lumi = campaign.x.lumi

    # xsec = dataset_inst.x.xsec
    # generator_weight = dataset_inst.x.generator_weight
    # n_events = dataset_inst.n_events

    # Set normalization, cross section, and lumi weights
    # section value right here
    # weights["norm_weight"] = f"""
    #     (1 / ({generator_weight} * {n_events}) )
    #     * ( (genWeight < 0) * (-1) + (genWeight >= 0) * (1) )
    # """
    # weights["xsec_weight"] = str(xsec)
    weights["lumi_weight"] = str(lumi * 1000)

    weights["n_gen_weight"] = "numberGeneratedEventsWeight"
    weights["gen_weight"] = """
        (
            ( 1.0 / negative_events_fraction) * (
                ((genWeight<0) * -1) + ((genWeight > 0 * 1))
            )
        )
    """
    weights["xsec_weight"] = "crossSectionPerEventWeight"

    return weights


def pileup() -> OrderedDict[str, str]:
    """
    Add pileup weights. The function returns an ordered dictionary
    with the weight names as keys and the ROOT expression to define the weight
    as values.
    """
    return OrderedDict([("pileup_weight", "puweight")])

