from order import Config

from configuration.xyh_bbtautau.metadata.variables import add_variables

def add_channels(
    config: Config,
):
    """
    Add analysis channels to the :py:class:~order.Config`.

    :param config: The configuration of the channel.
    """

    # electron-tau_h channel
    config.add_channel(
        name="et",
        id="+",
        label=r"$\text{e}\tau_{\text{h}}$",
        aux={
            "tau": {
                "id_vs_e_wp": "Tight",
                "id_vs_mu_wp": "VLoose",
                "id_vs_jet_wp": "Medium",
                "antiid_vs_jet_wp": "VVVLoose",
            }
        },
    )

    # muon-tau_h channel
    config.add_channel(
        name="mt",
        id="+",
        label=r"$\mu\tau_{\text{h}}$",
        aux={
            "tau": {
                "id_vs_e_wp": "VVLoose",
                "id_vs_mu_wp": "Tight",
                "id_vs_jet_wp": "Medium",
                "antiid_vs_jet_wp": "VVVLoose",
            }
        },
    )

    # tau_h-tau_h channel
    config.add_channel(
        name="tt",
        id="+",
        label=r"$\tau_{\text{h}}\tau_{\text{h}}$",
        aux={
            "tau": {
                "id_vs_e_wp": "VVLoose",
                "id_vs_mu_wp": "VLoose",
                "id_vs_jet_wp": "Medium",
                "antiid_vs_jet_wp": "VVVLoose",
            }
        },
    )

    # electron-muon channel
    config.add_channel(
        name="em",
        id="+",
        label=r"$\text{e}\mu$",
    )

    # electron-electron channel
    config.add_channel(
        name="ee",
        id="+",
        label=r"$\text{e}\text{e}$",
    )

    # muon-muon channel
    config.add_channel(
        name="mm",
        id="+",
        label=r"$\mu\mu$",
    )

    # Add variables
    for channel in config.channels.values():
        add_variables(channel)

