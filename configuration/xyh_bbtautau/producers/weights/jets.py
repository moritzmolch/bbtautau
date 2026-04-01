from collections import OrderedDict

from configuration.xyh_bbtautau.producers.helpers import requires


@requires()
def b_jets() -> OrderedDict[str, str]:
    """
    Add b jet identification weight. The function returns an ordered dictionary
    with the weight names as keys and the ROOT expression to define the weight
    as values.
    """
    return OrderedDict([("id_wgt_bjet_shape", "id_wgt_bjet")])

