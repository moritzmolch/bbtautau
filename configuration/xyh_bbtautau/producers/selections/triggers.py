from collections import OrderedDict
from order import Campaign, Channel

from configuration.xyh_bbtautau.producers.helpers import requires


@requires(
    metadata={"campaign", "channel"},
)
def triggers(
    campaign: Campaign,
    channel: Channel,
) -> OrderedDict[str, str]:
    """
    Apply trigger selection depending on the data-taking campaign and the
    analysis channel. The function returns an ordered dictionary with the
    filter names as keys and the ROOT expressions for the filters as values.
    """

    # Trigger selections are summarized in a nested map, where the first key
    # is an era or a tuple of eras, and the second key is the channel.
    trigger_selections = {
        ("2022preEE", "2022postEE", "2023preBPix", "2023postBPix"): {
            "et": "(pt_1 >= 32) && (trg_single_ele30 > 0.5)",
            "mt": "(pt_1 >= 26) && (trg_single_mu24 > 0.5)",
            "tt": """
                (pt_1 >= 40)
                && (pt_2 >= 40)
                && (trg_double_tau35 > 0.5)
            """,
            "em": "(pt_1 > 32) && (trg_single_ele30 > 0.5)",
            "ee": "(pt_1 >= 32) && (trg_single_ele30 > 0.5)",
            "mm": "(pt_1 >= 26) && (trg_single_mu24 > 0.5)",
        },
        "2024": {
            "et": "(pt_1 >= 32) && (trg_single_ele30 > 0.5)",
            "mt": "(pt_1 >= 26) && (trg_single_mu24 > 0.5)",
            "tt": """
                (pt_1 >= 40)
                && (pt_2 >= 40)
                && (trg_double_tau35_mediumpnet > 0.5)
            """,
            "em": "(pt_1 > 32) && (trg_single_ele30 > 0.5)",
            "ee": "(pt_1 >= 32) && (trg_single_ele30 > 0.5)",
            "mm": "(pt_1 >= 26) && (trg_single_mu24 > 0.5)",
        },
    }

    # Get the trigger selection for the given era and channel
    expression = None
    for campaign_tuple, trigger_selections_era in trigger_selections.items():
        if not isinstance(campaign_tuple, tuple):
            campaign_tuple = (campaign_tuple,)
        if campaign.name in campaign_tuple:
            expression = trigger_selections_era[channel.name]
    if expression is None:
        raise ValueError(
            f"No trigger selection for channel {channel.name} in "
            f"campaign {campaign.name} declared"
        )

    return OrderedDict([("trigger_selection", expression)])

