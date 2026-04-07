from order import Config

from order_util.datasets import add_dataset_from_sample_database


def add_top_datasets(
    config: Config,
):
    """
    Add single top and top quark pair production samples to a given
    configuration instance.

    Detailed dataset information is obtained from the
    [sample_database](https://github.com/kit-cms/kingmaker_sample_database).

    :param config: The :py:class:`~order.Config` that the datasets are added to.
    """

    add_dataset_from_sample_database(
        config,
        name="tt_2l2nu",
        nicks={
            "2022postEE": [
                "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [
                "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tt_4q",
        nicks={
            "2022postEE": [
                "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [
                "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TTto4Q_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tt_lnu2q",
        nicks={
            "2022postEE": [
                "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [
                "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tbq_top_tchannel",
        nicks={
            "2022postEE": [
                "TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TBbarQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tbq_lnu_top_tchannel",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tbq_2q_top_tchannel",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tbq_antitop_tchannel",
        nicks={
            "2022postEE": [
                "TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TbarBQ_t-channel_4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tbq_lnu_antitop_tchannel",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tbq_2q_antitop_tchannel",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tb_lnu_top_schannel",
        nicks={
            "2022postEE": [
                "TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TBbartoLplusNuBbar-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TBbartoLNu-s-channel_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tb_2q_top_schannel",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "TBbarto2Q-s-channel_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tb_lnu_antitop_schannel",
        nicks={
            "2022postEE": [
                "TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TbarBtoLminusNuB-s-channel-4FS_TuneCP5_13p6TeV_amcatnlo-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TbarBtoLNu-s-channel_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tb_2q_antitop_schannel",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "TbarBto2Q-s-channel_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="twminus_2l2nu",
        nicks={
            "2022postEE": [
                "TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="twminus_lnu2q",
        nicks={
            "2022postEE": [
                "TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="twminus_4q",
        nicks={
            "2022postEE": [
            ],
            "2022preEE": [
            ],
            "2023preBPix": [
            ],
            "2023postBPix": [
            ],
            "2024": [
                "TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="twplus_2l2nu",
        nicks={
            "2022postEE": [
                "TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="twplus_lnu2q",
        nicks={
            "2022postEE": [
                "TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="twplus_4q",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

