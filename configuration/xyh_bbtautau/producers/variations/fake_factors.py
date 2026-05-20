from ntuple_processor.utils import Cut, Weight
from ntuple_processor.variations import Variation, ReplaceCutAndAddWeight

from bbtautau.shapes import AnalysisContext


def fake_factors(
    analysis_context: AnalysisContext,
) -> list[Variation]:

    # Get the channel instance from the analysis context
    channel = analysis_context.channel

    # Raise an error if the channel does not contain a hadronic tau, since
    # fake factor method is not used in these channels
    if channel.name not in ["et", "mt", "tt"]:
        raise RuntimeError(
            "Fake factors can only be applied in the et, mt, and tt channels."
        )

    # Get the working points for the tau ID depending on the channel
    id_vs_jet_wp = channel.x.tau["id_vs_jet_wp"]
    antiid_vs_jet_wp = channel.x.tau["antiid_vs_jet_wp"]

    # Construct ID and anti-ID selection string templates with index as
    # parameter
    id_vs_jet_tpl = f"(id_tau_vsJet_{id_vs_jet_wp}_{{index}} > 0.5)"
    antiid_vs_jet_tpl = f"""
    (
        (id_tau_vsJet_{antiid_vs_jet_wp}_{{index}} > 0.5)
        && (id_tau_vsJet_{id_vs_jet_wp}_{{index}} < 0.5)
    )
    """

    # Define the modification for the AR selection and the fake factor weight
    ar_selection = None
    ff_weight = None
    if channel.name in ["et", "mt"]:
        ar_selection = antiid_vs_jet_tpl.format(index=2)
        ff_weight = "fake_factor_raw"

    elif channel.name == "tt":
        ar_selection = f"""
        (
            {antiid_vs_jet_tpl.format(index=1)}
            && {id_vs_jet_tpl.format(index=2)}
        ) || (
            {id_vs_jet_tpl.format(index=1)}
            && {antiid_vs_jet_tpl.format(index=2)}
        )
        """
        ff_weight = f"""
        0.5 * (
            {antiid_vs_jet_tpl.format(index=1)} * fake_factor_1
            + {antiid_vs_jet_tpl.format(index=2)} * fake_factor_2
        )
        """

    # Construct the fake factor variation by replacing the ID selection
    variation = ReplaceCutAndAddWeight(
        "tau_antiid_vs_jet",
        "tau_id_vs_jet",
        Cut(ar_selection, "tau_antiid_vs_jet"),
        Weight(ff_weight, "fake_factor"),
    )

    return [
        variation
    ]
