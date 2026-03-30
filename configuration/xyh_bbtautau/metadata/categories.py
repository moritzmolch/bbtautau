from order import Config

# from configuration.xyh_bbtautau.producers.selections.base import base_selection


def _add_base_signal_categories(
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
            aux={
                "default_selection": [], # [base_selection],
            },
        )


def add_categories(
    config_inst: Config,
):
    """
    Add the analysis categories to the :py:class:`~order.Config`.

    :param config: The configuration of the campaign.
    """

    # Base signal categories (after event selection and before NN
    # classification)
    _add_base_signal_categories(config_inst)

