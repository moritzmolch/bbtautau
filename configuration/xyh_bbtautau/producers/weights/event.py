from collections import OrderedDict

from bbtautau.shapes import AnalysisContext


def normalization(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Calculate weights to normalize MC histograms to the integrated luminosity
    and the expected theory cross section. The function returns an ordered
    dictionary with the weight names as keys and the ROOT expression to define
    the weight as values.

    :param analysis_context: Analysis context, to which the weights should
        be tailored. The attribute used in this function is 
        :py:attr`~shape_producer.operations.AnalysisContext.campaign`.
    
    :return: Collection of weight definitions.
    """

    # Get the campaign from the analysis context
    campaign = analysis_context.campaign

    # Empty storage for new weights
    weights = OrderedDict()

    # TODO make this function dataset-dependent to be able to inject cross
    # section from dataset object.

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
        ( 1.0 / negative_events_fraction) * (
            (genWeight > 0) - (genWeight < 0)
        )
    """
    weights["xsec_weight"] = "crossSectionPerEventWeight"

    return weights


def pileup(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Add pileup weights. The function returns an ordered dictionary
    with the weight names as keys and the ROOT expression to define the weight
    as values.

    :param analysis_context: Analysis context, to which the weights should
        be tailored. This is just a placeholder to provide a consistent
        interface for all weight modules.
    
    :return: Collection of weight definitions.
    """
    return OrderedDict([("pileup_weight", "puweight")])
