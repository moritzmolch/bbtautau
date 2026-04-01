from collections import OrderedDict
from order import Campaign, Channel

from configuration.xyh_bbtautau.producers.helpers import requires


@requires(
    metadata={"campaign", "channel"},
)
def triggers(
    *,
    campaign: Campaign,
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Apply trigger weights depending on the trigger used in the respective
    campaign and analysis channel. The function returns an ordered dictionary
    with the weight names as keys and the ROOT expression to define the weight
    as values.
    """

    # Trigger weights are summarized in a nested map, where the first key
    # is an era or a tuple of eras, and the second key is the channel.
    trigger_weights = {
        ("2022preEE", "2022postEE", "2023preBPix", "2023postBPix"): {
            "et": "trg_wgt_single_ele30",
            "mt": "trg_wgt_single_mu24",
            "tt": "trg_wgt_double_tau35_leg1 * trg_wgt_double_tau35_leg2",
            "em": "trg_wgt_single_ele30",
            "ee": "trg_wgt_single_ele30",
            "mm": "trg_wgt_single_mu24",
        },
        "2024": {
            "et": "trg_wgt_single_ele30",
            "mt": "trg_wgt_single_mu24",
            "tt": """
                (
                    trg_wgt_double_tau35_mediumpnet_leg1
                    * trg_wgt_double_tau35_mediumpnet_leg2
                )
            """,
            "em": "trg_wgt_single_ele30",
            "ee": "trg_wgt_single_ele30",
            "mm": "trg_wgt_single_mu24",
        },
    }

    # Get the trigger selection for the given era and channel
    expression = None
    for campaign_tuple, trigger_weights_era in trigger_weights.items():
        if not isinstance(campaign_tuple, tuple):
            campaign_tuple = (campaign_tuple,)
        if campaign.name in campaign_tuple:
            expression = trigger_weights_era[channel.name]
    if expression is None:
        raise ValueError(
            f"No trigger weight for channel {channel.name} in campaign "
            f"{campaign.name} declared"
        )

    return OrderedDict([("trigger_weight", expression)])

