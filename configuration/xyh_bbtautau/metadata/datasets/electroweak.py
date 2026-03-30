from order import Config

from order_util.datasets import add_dataset_from_sample_database


def add_electroweak_datasets(
    config: Config,
):
    """
    Add W, Z, and diboson production datasets to a given configuration instance.

    Detailed dataset information is obtained from the
    [sample_database](https://github.com/kit-cms/kingmaker_sample_database).

    :param config: The :py:class:`~order.Config` that the datasets are
        added to.
    """

    add_dataset_from_sample_database(
        config,
        name="dy_2l_m10to50",
        nicks={
            "2022postEE": [
                "DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
                "DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
                "DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [
                "DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X_ext1",
            ],
            "2023postBPix": [
                "DYto2L-2Jets_MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X_ext1",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2e_m10to50",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2E-2Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2mu_m10to50",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2Mu-2Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2tau_m10to50",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2Tau-2Jets_Bin-MLL-10to50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2l_m50_0j",
        nicks={
            "2022postEE": [
                "DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "DYto2L-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2l_m50_1j",
        nicks={
            "2022postEE": [
                "DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "DYto2L-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2l_m50_2j",
        nicks={
            "2022postEE": [
                "DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "DYto2L-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2e_m50_0j",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2E-2Jets_Bin-0J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2e_m50_1j",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2E-2Jets_Bin-1J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2e_m50_2j",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2E-2Jets_Bin-2J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2mu_m50_0j",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2Mu-2Jets_Bin-0J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2mu_m50_1j",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2Mu-2Jets_Bin-1J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2mu_m50_2j",
        nicks={
            "2022preEE": [],
            "2022postEE": [],
            "2022preBPix": [],
            "2022postBPix": [],
            "2024": [
                "DYto2Mu-2Jets_Bin-2J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2tau_m50_0j",
        nicks={
            "2022postEE": [
                "DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "DYto2Tau-2Jets_MLL-50_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "DYto2Tau-2Jets_Bin-0J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2tau_m50_1j",
        nicks={
            "2022postEE": [
                "DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "DYto2Tau-2Jets_MLL-50_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "DYto2Tau-2Jets_Bin-1J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="dy_2tau_m50_2j",
        nicks={
            "2022postEE": [
                "DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "DYto2Tau-2Jets_MLL-50_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "DYto2Tau-2Jets_Bin-2J-MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="w_lnu_0j",
        nicks={
            "2022postEE": [
                "WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "WtoLNu-2Jets_0J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="w_lnu_1j",
        nicks={
            "2022postEE": [
                "WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "WtoLNu-2Jets_1J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="w_lnu_2j",
        nicks={
            "2022postEE": [
                "WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "WtoLNu-2Jets_2J_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="w_enu",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "WtoENu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="w_munu",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "WtoMuNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="w_taunu",
        nicks={
            "2022postEE": [],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [
                "WtoTauNu-2Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="ww",
        nicks={
            "2022postEE": [
                "WW_TuneCP5_13p6TeV_pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "WW_TuneCP5_13p6TeV_pythia8_Run3Summer22NanoAODv12-130X"
            ],
            "2023preBPix": [
                "WW_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "WW_TuneCP5_13p6TeV_pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "WW_TuneCP5_13p6TeV_pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="wz",
        nicks={
            "2022postEE": [
                "WZ_TuneCP5_13p6TeV_pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "WZ_TuneCP5_13p6TeV_pythia8_Run3Summer22NanoAODv12-130X"
            ],
            "2023preBPix": [
                "WZ_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "WZ_TuneCP5_13p6TeV_pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "WZ_TuneCP5_13p6TeV_pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="zz",
        nicks={
            "2022postEE": [
                "ZZ_TuneCP5_13p6TeV_pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "ZZ_TuneCP5_13p6TeV_pythia8_Run3Summer22NanoAODv12-130X"
            ],
            "2023preBPix": [
                "ZZ_TuneCP5_13p6TeV_pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "ZZ_TuneCP5_13p6TeV_pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "ZZ_TuneCP5_13p6TeV_pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="ww_2l2nu",
        nicks={
            "2022postEE": [
                "WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [],
            "2023preBPix": [],
            "2023postBPix": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="wz_3lnu",
        nicks={
            # "2022preEE": [
            #    "WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            #    "WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            # ],
            "2022postEE": [
                "WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="wz_lnu2q",
        nicks={
            # "2022preEE": [
            #    "WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            #    "WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            # ],
            "2022postEE": [
                "WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

