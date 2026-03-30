from order import Config

from configuration.xyh_bbtautau.metadata.datasets.data import add_data_datasets
from configuration.xyh_bbtautau.metadata.datasets.electroweak import (
    add_electroweak_datasets,
)
from configuration.xyh_bbtautau.metadata.datasets.higgs import add_higgs_datasets
from configuration.xyh_bbtautau.metadata.datasets.top import add_top_datasets
from configuration.xyh_bbtautau.metadata.datasets.xyh import add_xyh_datasets


def add_datasets(
    config: Config,
):
    """
    Add analysis datasets to a given configuration instance.

    Detailed dataset information is obtained from the
    [sample_database](https://github.com/kit-cms/kingmaker_sample_database).

    :param config_inst: The :py:class:`~order.Config` that the datasets are
        added to.
    """

    # Data
    add_data_datasets(config)

    # Signal processes: X -> HY -> bbtautau
    add_xyh_datasets(config)

    # Single top and top quark pair production
    add_top_datasets(config)

    # Z, W boson and diboson pair production
    add_electroweak_datasets(config)

    # Single Higgs and Higgs boson pair production
    add_higgs_datasets(config)

