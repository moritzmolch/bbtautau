from order import Config


def add_base_signal_categories(
    config: Config,
):
    """
    Add the base signal region categories after the base event selection and
    before the NN classification to the :py:class:`order.Config` object.
    """

    # Get the analysis channels
    channels = config.channels

    # Add a base signal category for each channel
    for channel_name, _, channel_inst in channels.items():
        config.add_category(
            name=f"{channel_name}_base_sr",
            label=channel_inst.label,
            id="+",
            channel=channel_inst,
            tags={"signal_cat"},
        )


# def _add_jet_category_insts(
#     config_inst: Config,
# ):
#     """
#     Add categories with jet (or b jet) selection on top of the base signal
#     region selection.
#     """

#     # Get the analysis channels
#     channel_insts = config_inst.channels

#     # Add categories with exactly and at least n jets for each channel
#     for channel_name, _, channel_inst in channel_insts.items():
#         for n_jets in range(1, 5):
#             # At least n jets
#             config_inst.add_category(
#                 name=f"{channel_name}_geq{n_jets}j",
#                 id="+",
#                 channel=channel_inst,
#                 tags={"signal_cat", f"geq{n_jets}j"},
#                 aux={
#                     "operation_constructors": [jet_category_selection],
#                 },
#             )

#             # Exactly n jets
#             config_inst.add_category(
#                 name=f"{channel_name}_eq{n_jets}j",
#                 id="+",
#                 channel=channel_inst,
#                 tags={"signal_cat", f"eq{n_jets}j"},
#                 aux={
#                     "operation_constructors": [jet_category_selection],
#                 },
#             )

#         if n_jets >= 1:
#             # At least n b jets
#             config_inst.add_category(
#                 name=f"{channel_name}_geq{n_jets}b",
#                 id="+",
#                 channel=channel_inst,
#                 tags={"signal_cat", f"geq{n_jets}b"},
#                 aux={
#                     "operation_constructors": [jet_category_selection],
#                 },
#             )

#             # Exactly n b jets
#             config_inst.add_category(
#                 name=f"{channel_name}_eq{n_jets}b",
#                 id="+",
#                 channel=channel_inst,
#                 tags={"signal_cat", f"eq{n_jets}b"},
#                 aux={
#                     "operation_constructors": [jet_category_selection],
#                 },
#             )


def add_abcd_categories(
    config_inst: Config,
):
    """
    Add additional categories for QCD estimation with the ABCD method.
    """

    # Get the analysis channels
    channel_insts = config_inst.channels

    # Add (OS, anti-ID), (SS, ID), and (SS, anti-ID) categories for each
    # channel
    for channel_name, _, channel_inst in channel_insts.items():
        # opposite-sign, anti-ID region
        config_inst.add_category(
            name=f"{channel_name}_abcd_os_antiid",
            id="+",
            channel=channel_inst,
            tags={"abcd", "os", "antiid"},
        )

        # same-sign, ID region
        config_inst.add_category(
            name=f"{channel_name}_abcd_ss_id",
            id="+",
            channel=channel_inst,
            tags={"abcd", "os", "id"},
        )

        # same-sign, anti-ID region
        config_inst.add_category(
            name=f"{channel_name}_abcd_ss_antiid",
            id="+",
            channel=channel_inst,
            tags={"abcd", "os", "antiid"},
        )


def add_fake_factor_categories(
    config: Config,
):
    """
    Add additional categories for applying the fake factor method to this
    analysis.
    """

    # Get the analysis channels
    channels = config.channels

    # Add anti-ID category for each channel, representing the AR of the fake
    # factor method
    for channel_name, _, channel_inst in channels.items():
        if channel_name in ["et", "mt", "tt"]:
            config.add_category(
                name=f"{channel_name}_ff_antiid",
                id="+",
                channel=channel_inst,
                tags={"ff", "antiid"},
            )


def add_categories(
    config: Config,
):
    """
    Add the analysis categories to the :py:class:`~order.Config`.

    :param config: The configuration of the campaign.
    """

    # Base signal categories (after event selection and before NN
    # classification)
    add_base_signal_categories(config)

    # ABCD categories (for estimation of QCD multijet production)
    add_abcd_categories(config)

    # Fake factor categories (for estimation of jet -> tau_h fakes)
    add_fake_factor_categories(config)


