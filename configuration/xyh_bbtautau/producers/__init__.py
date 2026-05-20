from configuration.xyh_bbtautau.producers.weights.base import mc_weights
from configuration.xyh_bbtautau.producers.selections.base import (
    gen_selection,
    channel_selection,
)
from ntuple_processor.utils import Selection
from bbtautau.shapes import AnalysisContext


def default_selection(
    analysis_context: AnalysisContext,
):
    # Channel and category selection
    ch_selection = channel_selection(analysis_context)

    # MC weights
    proc_weights = mc_weights(analysis_context)

    # Generator-level process selections
    proc_selection = gen_selection(analysis_context)

    selections = [
        Selection(
            name=analysis_context.category.name,
            cuts=[(expression, name) for name, expression in ch_selection.items()],
        ),
        Selection(
            name=f"{analysis_context.process.name}-{analysis_context.dataset.name}",
            cuts=[(expression, name) for name, expression in proc_selection.items()],
            weights=[(expression, name) for name, expression in proc_weights.items()],
        ),
    ]

    return selections

