from order import Analysis

from configuration.xyh_bbtautau.metadata.configs import add_configs


def create_analysis(
    name: str,
) -> Analysis:
    """
    Create a new analysis instance for this configuration.

    :param name: Name of the analysis

    :returns: the full analysis metadata index
    """

    # Create the main analysis instance
    analysis_inst = Analysis(
        name=name,
        id="+",
    )

    # Add the individual campaign configurations
    add_configs(analysis_inst)

    return analysis_inst


analysis = create_analysis("xyh_bbtautau")

