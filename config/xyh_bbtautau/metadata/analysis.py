from order import Analysis

from config.xyh_bbtautau.metadata import add_configs


def create_analysis_inst(
    name: str,
) -> Analysis:
    """
    Create a new analysis instance for this configuration.
    """

    # Create the main analysis instance
    analysis_inst = Analysis(
        name=name,
        id="+",
    )

    # Add the individual campaign configurations
    add_configs(analysis_inst)

    return analysis_inst


analysis_inst = create_analysis_inst("xyh_bbtautau")

