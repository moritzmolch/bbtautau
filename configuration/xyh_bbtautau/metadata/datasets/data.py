from order import Config

from order_util.datasets import add_dataset_from_sample_database


def add_data_datasets(
    config: Config,
):
    """
    Add data samples to a given configuration instance.

    Detailed dataset information is obtained from the
    [sample_database](https://github.com/kit-cms/kingmaker_sample_database).

    :param config_inst: The :py:class:`~order.Config` that the datasets are
        added to.
    """

    add_dataset_from_sample_database(
        config,
        name="egamma",
        nicks={
            "2022postEE": [
                "EGamma_Run2022E-22Sep2023-v1",
                "EGamma_Run2022F-22Sep2023-v1",
                "EGamma_Run2022G-22Sep2023-v2",
            ],
            "2022preEE": [
                "EGamma_Run2022C-22Sep2023-v1",
                "EGamma_Run2022D-22Sep2023-v1",
            ],
            "2023preBPix": [
                "EGamma0_Run2023C-22Sep2023_v1-v1",
                "EGamma0_Run2023C-22Sep2023_v2-v1",
                "EGamma0_Run2023C-22Sep2023_v3-v1",
                "EGamma0_Run2023C-22Sep2023_v4-v1",
                "EGamma1_Run2023C-22Sep2023_v1-v1",
                "EGamma1_Run2023C-22Sep2023_v2-v1",
                "EGamma1_Run2023C-22Sep2023_v3-v1",
                "EGamma1_Run2023C-22Sep2023_v4-v1",
            ],
            "2023postBPix": [
                "EGamma0_Run2023D-22Sep2023_v1-v1",
                "EGamma0_Run2023D-22Sep2023_v2-v1",
                "EGamma1_Run2023D-22Sep2023_v1-v1",
                "EGamma1_Run2023D-22Sep2023_v2-v1",
            ],
            "2024": [
                "EGamma0_Run2024C-MINIv6NANOv15-v1",
                "EGamma0_Run2024D-MINIv6NANOv15-v1",
                "EGamma0_Run2024E-MINIv6NANOv15-v1",
                "EGamma0_Run2024F-MINIv6NANOv15-v1",
                "EGamma0_Run2024G-MINIv6NANOv15-v2",
                "EGamma0_Run2024H-MINIv6NANOv15-v2",
                "EGamma0_Run2024I-MINIv6NANOv15-v1",
                "EGamma0_Run2024I-MINIv6NANOv15_v2-v1",
                "EGamma1_Run2024C-MINIv6NANOv15-v1",
                "EGamma1_Run2024D-MINIv6NANOv15-v1",
                "EGamma1_Run2024E-MINIv6NANOv15-v1",
                "EGamma1_Run2024F-MINIv6NANOv15-v1",
                "EGamma1_Run2024G-MINIv6NANOv15-v2",
                "EGamma1_Run2024H-MINIv6NANOv15-v1",
                "EGamma1_Run2024I-MINIv6NANOv15-v1",
                "EGamma1_Run2024I-MINIv6NANOv15_v2-v1",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="muon",
        nicks={
            "2022postEE": [
                "Muon_Run2022E-22Sep2023-v1",
                "Muon_Run2022F-22Sep2023-v2",
                "Muon_Run2022G-22Sep2023-v1",
            ],
            "2022preEE": [
                "Muon_Run2022C-22Sep2023-v1",
                "Muon_Run2022D-22Sep2023-v1",
            ],
            "2023preBPix": [
                "Muon0_Run2023C-22Sep2023_v1-v1",
                "Muon0_Run2023C-22Sep2023_v2-v1",
                "Muon0_Run2023C-22Sep2023_v3-v1",
                "Muon0_Run2023C-22Sep2023_v4-v1",
                "Muon1_Run2023C-22Sep2023_v1-v1",
                "Muon1_Run2023C-22Sep2023_v2-v1",
                "Muon1_Run2023C-22Sep2023_v3-v1",
                "Muon1_Run2023C-22Sep2023_v4-v2",
            ],
            "2023postBPix": [
                "Muon0_Run2023D-22Sep2023_v1-v1",
                "Muon0_Run2023D-22Sep2023_v2-v1",
                "Muon1_Run2023D-22Sep2023_v1-v1",
                "Muon1_Run2023D-22Sep2023_v2-v1",
            ],
            "2024": [
                "Muon0_Run2024C-MINIv6NANOv15-v1",
                "Muon0_Run2024D-MINIv6NANOv15-v1",
                "Muon0_Run2024E-MINIv6NANOv15-v1",
                "Muon0_Run2024F-MINIv6NANOv15-v1",
                "Muon0_Run2024G-MINIv6NANOv15-v1",
                "Muon0_Run2024H-MINIv6NANOv15-v1",
                "Muon0_Run2024I-MINIv6NANOv15-v1",
                "Muon0_Run2024I-MINIv6NANOv15_v2-v1",
                "Muon1_Run2024C-MINIv6NANOv15-v1",
                "Muon1_Run2024D-MINIv6NANOv15-v1",
                "Muon1_Run2024E-MINIv6NANOv15-v1",
                "Muon1_Run2024F-MINIv6NANOv15-v1",
                "Muon1_Run2024G-MINIv6NANOv15-v2",
                "Muon1_Run2024H-MINIv6NANOv15-v2",
                "Muon1_Run2024I-MINIv6NANOv15-v1",
                "Muon1_Run2024I-MINIv6NANOv15_v2-v1",
            ]
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tau",
        nicks={
            "2022postEE": [
                "Tau_Run2022E-22Sep2023-v1",
                "Tau_Run2022F-22Sep2023-v1",
                "Tau_Run2022G-22Sep2023-v1",
            ],
            "2022preEE": [
                "Tau_Run2022C-22Sep2023-v1",
                "Tau_Run2022D-22Sep2023-v1",
            ],
            "2023preBPix": [
                "Tau_Run2023C-22Sep2023_v1-v2",
                "Tau_Run2023C-22Sep2023_v2-v1",
                "Tau_Run2023C-22Sep2023_v3-v1",
                "Tau_Run2023C-22Sep2023_v4-v1",
            ],
            "2023postBPix": [
                "Tau_Run2023D-22Sep2023_v1-v1",
                "Tau_Run2023D-22Sep2023_v2-v1",
            ],
            "2024": [
                "Tau_Run2024C-MINIv6NANOv15-v1",
                "Tau_Run2024D-MINIv6NANOv15-v1",
                "Tau_Run2024E-MINIv6NANOv15-v1",
                "Tau_Run2024F-MINIv6NANOv15-v1",
                "Tau_Run2024G-MINIv6NANOv15-v1",
                "Tau_Run2024H-MINIv6NANOv15-v1",
                "Tau_Run2024I-MINIv6NANOv15-v1",
                "Tau_Run2024I-MINIv6NANOv15_v2-v1",
            ]
        },
    )
