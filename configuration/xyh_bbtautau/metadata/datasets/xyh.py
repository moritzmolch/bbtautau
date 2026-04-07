from order import Config

from configuration.xyh_bbtautau.constants import (
    XYH_DECAY_MODES,
    XYH_MASS_POINTS,
)
from order_util.datasets import add_dataset_from_sample_database


def add_xyh_datasets(
    config: Config,
):
    """
    Add X &rightarrow; HY &rightarrow; bb&tau;&tau; signal samples to a given
    configuration instance.

    Detailed dataset information is obtained from the
    [sample_database](https://github.com/kit-cms/kingmaker_sample_database).

    :param config_inst: The :py:class:`~order.Config` that the datasets are
        added to.
    """

    for y_decay_mode, h_decay_mode in XYH_DECAY_MODES:
        for m_x, m_y in XYH_MASS_POINTS:
            y_decay_mode_upper = f"2{y_decay_mode[1].upper()}{y_decay_mode[2:]}"
            h_decay_mode_upper = f"2{h_decay_mode[1].upper()}{h_decay_mode[2:]}"
            if y_decay_mode == "2b" and h_decay_mode == "2tau" and m_x == 2500 and m_y == 800:
                continue
            if y_decay_mode == "2tau" and h_decay_mode == "2b" and m_x == 2500 and m_y == 90:
                continue
            add_dataset_from_sample_database(
                config,
                name=f"xyh_y{y_decay_mode}_h{h_decay_mode}_mx{m_x}_my{m_y}",
                nicks={
                    "2022preEE": [],
                    "2022postEE": [],
                    "2023preBPix": [],
                    "2023postBPix": [],
                    "2024": [
                        f"NMSSM-XtoYHto{y_decay_mode_upper}{h_decay_mode_upper}_Par-MX-{m_x}-MY-{m_y}_TuneCP5_13p6TeV_madgraph-pythia8_RunIII2024Summer24NanoAODv15-150X",
                    ],
                },
            )

