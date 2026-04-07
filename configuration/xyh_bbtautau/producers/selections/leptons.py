from collections import OrderedDict
from itertools import chain
from order import Channel

from configuration.xyh_bbtautau.producers.helpers import requires


@requires(
    metadata={"channel"},
)
def lepton_vetoes(
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Apply vetoes on additional leptons. In the semileptonic channels, a veto
    on dilepton systems constructed from a looser selection is also applied. The
    function returns an ordered dictionary with the filter names as keys and the
    ROOT expressions for the selections as values.
    """

    # Storage for lepton vetoes
    selections = OrderedDict()

    # The extra electron and extra muon vetoes apply to all channels
    selections["extraelec_veto"] = "(extraelec_veto < 0.5)"
    selections["extramuon_veto"] = "(extramuon_veto < 0.5)"

    # The dilepton veto only applies to the semileptonic channels
    if channel.name in ["et", "mt"]:
        selections["dilepton_veto"] = "(dilepton_veto < 0.5)"

    return selections


@requires(
    metadata={"channel"},
)
def electrons(
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Apply electron selection in channels with at least one electron. The
    function returns an ordered dictionary with the filter names as keys and the
    ROOT expressions for the selections as values.
    """

    # Storage for electron selection
    selections = OrderedDict()

    # Construct selection string templates with index as parameter
    electron_eta_tpl = "(abs(eta_{index}) < 2.5)"
    electron_iso_tpl = "(iso_{index} < 0.15)"

    # In the em channel, add a pT requirement, which is symmetric to the
    # muon selection
    # TODO lower threshold in ntuples
    if channel.name == "em":
        electron_pt_tpl = "(pt_{index} > 32)"
        selections["electron1_pt"] = electron_pt_tpl.format(index=1)

    # Add electron selection for
    # - the first lepton in the em and ee channels,
    # - for the second lepton in the ee channel.
    # All other channels do not have a electron candidate in the di-lepton
    # pair.
    indices = {
        "et": [1],
        "em": [1],
        "ee": [1, 2],
    }
    if channel.name in indices:
        for i in indices[channel.name]:
            selections[f"electron{i}_eta"] = electron_eta_tpl.format(index=i)
            selections[f"electron{i}_iso"] = electron_iso_tpl.format(index=i)

    return selections


@requires(
    metadata={"channel"},
)
def muons(
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Apply muon selection in channels with at least one muon. The function
    returns an ordered dictionary with the filter names as keys and the ROOT
    expressions for the selections as values.
    """

    # Storage for all muon selections
    selections = OrderedDict()

    # Construct selection string templates with index as parameter
    muon_eta_tpl = "(abs(eta_{index}) < 2.4)"
    muon_iso_tpl = "(iso_{index} < 0.15)"

    # In the em channel, add a pT requirement as it is not necessarily covered
    # by the trigger
    # TODO lower threshold in ntuples
    if channel.name == "em":
        muon_pt_tpl = "(pt_{index} > 20)"
        selections["muon2_pt"] = muon_pt_tpl.format(index=2)

    # Add muon selection for
    # - the first lepton in the mt and mm channels,
    # - for the second lepton in the em and mm channels.
    # All other channels do not have a muon candidate in the di-lepton pair.
    indices = {
        "mt": [1],
        "em": [2],
        "mm": [1, 2],
    }
    if channel.name in indices:
        for i in indices[channel.name]:
            selections[f"muon{i}_eta"] = muon_eta_tpl.format(index=i)
            selections[f"muon{i}_iso"] = muon_iso_tpl.format(index=i)

    return selections


@requires(
    metadata={"channel"},
)
def hadronic_taus(
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Apply hadronic tau selection in channels with at least one hadronic tau. The
    function returns an ordered dictionary with the filter names as keys and the
    ROOT expressions for the selections as values.
    """

    # Storage for tau selection
    selections = OrderedDict()

    # If this is not a channel with a tau lepton, just return an empty
    # dictionary
    if channel.name not in ["et", "mt", "tt"]:
        return selections

    # Get the working points for the tau ID depending on the channel
    id_vs_jet_wp = channel.x.tau["id_vs_jet_wp"]
    id_vs_e_wp = channel.x.tau["id_vs_e_wp"]
    id_vs_mu_wp = channel.x.tau["id_vs_mu_wp"]

    # Set the tau pt and eta selection criteria depending on the channel
    min_pt, max_abs_eta = 0, 0
    if channel.name in ["et", "mt"]:
        min_pt, max_abs_eta = 20, 2.5
    elif channel.name == "tt":
        min_pt, max_abs_eta = 40, 2.1

    # Construct pt and eta selection string templates with index as parameter
    tau_pt_eta_tpl = (
        f"( (pt_{{index}} > {min_pt}) "
        f"&& (abs(eta_{{index}}) < {max_abs_eta}) )"
    )

    # Construct ID selection string templates with index as parameter
    id_vs_jet_tpl = f"(id_tau_vsJet_{id_vs_jet_wp}_{{index}} > 0.5)"
    id_vs_e_tpl = f"(id_tau_vsEle_{id_vs_e_wp}_{{index}} > 0.5)"
    id_vs_mu_tpl = f"(id_tau_vsMu_{id_vs_mu_wp}_{{index}} > 0.5)"

    # Construct decay mode selection string templates with index as parameter
    tau_dm_tpl = (
        "( "
        + " || ".join(
            f"(tau_decaymode_{{index}} == {dm})" for dm in [0, 1, 10, 11]
        )
        + " )"
    )

    # Add tau selection for
    # - for the first lepton in the tt channels,
    # - the second lepton in the et, mt, and tt channels.
    # All other channels do not have a tau candidate in the di-lepton pair.
    indices = {
        "et": [2],
        "mt": [2],
        "tt": [1, 2],
    }
    if channel.name in indices:
        for i in indices[channel.name]:
            selections[f"tau{i}_pt_eta"] = tau_pt_eta_tpl.format(index=i)
            selections[f"tau{i}_dm"] = tau_dm_tpl.format(index=i)
            selections[f"tau{i}_id_vs_jet"] = id_vs_jet_tpl.format(index=i)
            selections[f"tau{i}_id_vs_e"] = id_vs_e_tpl.format(index=i)
            selections[f"tau{i}_id_vs_mu"] = id_vs_mu_tpl.format(index=i)

    return selections


@requires(
    metadata={"channel"},
)
def ll_pair(
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Lepton selection, built from the single electron, muon, and hadronic tau
    selections, as well as criteria on charge and $\\Delta R$ of the pair. The
    function returns an ordered dictionary with the filter names as keys and the
    ROOT expressions for the selections as values.
    """

    # Collect electron, muon, and tau selection
    selections = OrderedDict(
        chain(
            electrons(channel).items(),
            muons(channel).items(),
            hadronic_taus(channel).items(),
        )
    )

    # Require opposite-sign charge for the two tau candidates
    selections["ll_pair_os"] = "((q_1 * q_2) < 0)"

    # Require a minimum spatial separation of the two tau candidates
    selections["ll_pair_delta_r"] = "(deltaR_ditaupair > 0.5)"

    return selections

