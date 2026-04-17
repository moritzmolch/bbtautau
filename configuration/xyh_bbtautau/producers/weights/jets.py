from collections import OrderedDict

from bbtautau.shapes import AnalysisContext


def b_jets(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Add b jet identification weight. The function returns an ordered dictionary
    with the weight names as keys and the ROOT expression to define the weight
    as values.

    :param analysis_context: Analysis context, to which the weights should
        be tailored. This is just a placeholder to provide a consistent
        interface for all weight modules.
    
    :return: Collection of weight definitions.
    """
    return OrderedDict([("id_wgt_bjet_shape", "id_wgt_bjet")])
