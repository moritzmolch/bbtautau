from order import Config

from order_util.datasets import add_dataset_from_sample_database


def add_higgs_datasets(
    config: Config,
):
    """
    Add single Higgs and Higgs pair production samples to a given configuration
    instance.

    Detailed dataset information is obtained from the
    [sample_database](https://github.com/kit-cms/kingmaker_sample_database).

    :param config_inst: The :py:class:`~order.Config` that the datasets are
        added to.
    """

    add_dataset_from_sample_database(
        config,
        name="gluglu_h_2tau",
        nicks={
            "2022preEE": [
                "GluGluHToTauTau_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2022postEE": [
                "GluGluHTo2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2023preBPix": [
                "GluGluHTo2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "GluGluHTo2TauUncorrelatedDecay_M-125_CP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "GluGluH-Hto2TauUncorrelatedDecay_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="gluglu_h_2b",
        nicks={
            "2022postEE": [
                "GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "GluGluHto2B_M-125_TuneCP5_13p6TeV_powheg-minlo-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "GluGluH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8_RunIII2024Summer24NanoAODv15-150X",
                "GluGluH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8_RunIII2024Summer24NanoAODv15-150X_ext1",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="gluglu_h_2w_2l2nu",
        nicks={
            "2022postEE": [
                "GluGluHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "GluGluHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="gluglu_h_2w_lnu2q",
        nicks={
            "2022postEE": [
                "GluGluHto2WtoLNu2Q_M-125_TuneCP5_13p6TeV_powheg-JHUGenV752-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "GluGluHto2WtoLNu2Q_M-125_TuneCP5_13p6TeV_powheg-JHUGenV752-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="gluglu_h_2z_2l2q",
        nicks={
            "2022postEE": [
                "GluGluHto2Zto2L2Q_M-125_TuneCP5_13p6TeV_powheg-jhugenv7520-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "GluGluHto2Zto2L2Q_M-125_TuneCP5_13p6TeV_powheg-jhugenv7520-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="gluglu_h_2z_4l",
        nicks={
            "2022postEE": [
                "GluGluHtoZZto4L_M-125_TuneCP5_13p6TeV_powheg2-JHUGenV752-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "GluGluHtoZZto4L_M-125_TuneCP5_13p6TeV_powheg2-JHUGenV752-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="vbf_h_2tau",
        nicks={
            "2022preEE": [
                "VBFHToTauTau_M125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2022postEE": [
                "VBFHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2023preBPix": [
                "VBFHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "VBFHTo2TauUncorrelatedDecay_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "VBFH-Hto2TauUncorrelatedDecay_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="vbf_h_2b",
        nicks={
            "2022postEE": [
                "VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [
                "VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "VBFHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "VBFH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
                # "VBFH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X_ext1",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="vbf_h_2w_2l2nu",
        nicks={
            "2022postEE": [
                "VBFHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "VBFHto2Wto2L2Nu_M-125_TuneCP5_13p6TeV_powheg-jhugen752-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="vbf_h_2w_lnu2q",
        nicks={
            "2022postEE": [
                "VBFHto2WtoLNu2Q_M-125_TuneCP5_13p6TeV_powheg-JHUGenV752-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2022preEE": [
                "VBFHto2WtoLNu2Q_M-125_TuneCP5_13p6TeV_powheg-JHUGenV752-pythia8_Run3Summer22NanoAODv12-130X",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="vbf_h_2z_4l",
        nicks={
            # "2022preEE": [
            #    "VBFHtoZZto4L_M125_TuneCP5_13p6TeV_powheg2-JHUGenV752-pythia8_Run3Summer22NanoAODv12-130X",
            # ],
            "2022postEE": [
                "VBFHto2Zto4L_M125_TuneCP5_13p6TeV_powheg-jhugenv752-pythia8_Run3Summer22EENanoAODv12-130X",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tth_h_2b",
        nicks={
            "2022postEE": [
                "TTH_Hto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "TTH_Hto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X"
            ],
            "2023preBPix": [
                "TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TTHto2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TTH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="tth_h_non2b",
        nicks={
            "2022postEE": [
                "TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X"
            ],
            "2023preBPix": [
                "TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-130X",
            ],
            "2023postBPix": [
                "TTHtoNon2B_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-130X",
            ],
            "2024": [
                "TTH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-150X",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="gluglu_hh_2b2tau",
        nicks={
            "2022postEE": [
                "GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X"
            ],
            "2023preBPix": [
                "GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23NanoAODv12-tsg",
            ],
            "2023postBPix": [
                "GluGlutoHHto2B2Tau_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer23BPixNanoAODv12-tsg",
            ],
            "2024": [
                "GluGluHHto2B2Tau_Par-c2-0p00-kl-1p00-kt-1p00_TuneCP5_13p6TeV_powheg-pythia8_RunIII2024Summer24NanoAODv15-PowhegBugFix",
            ],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="gluglu_hh_4b",
        nicks={
            "2022postEE": [
                "GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "GluGlutoHHto4B_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X"
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="gluglu_hh_4v",
        nicks={
            "2022postEE": [
                "GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "GluGlutoHHto4V_kl-1p00_kt-1p00_c2-0p00_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="vbf_hh_2b2tau",
        nicks={
            # "2022preEE": [
            #    "VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8_Run3Summer22NanoAODv12-130X",
            # ],
            "2022postEE": [
                "VBFHHto2B2Tau_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="vbf_hh_4b",
        nicks={
            # "2022preEE": [
            #    "VBFHHto4B_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8_Run3Summer22NanoAODv12-130X",
            # ],
            "2022postEE": [
                "VBFHHto4B_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="vbf_hh_4v",
        nicks={
            "2022postEE": [
                "VBFHHto4V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8_Run3Summer22EENanoAODv12-130X"
            ],
            "2022preEE": [
                "VBFHHto4V_CV_1_C2V_1_C3_1_TuneCP5_13p6TeV_madgraph-pythia8_Run3Summer22NanoAODv12-130X"
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="wminush_h2b_w2q",
        nicks={
            "2022postEE": [
                "WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "WminusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="wminush_h2b_wlnu",
        nicks={
            "2022postEE": [
                "WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "WminusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="wplush_h2b_w2q",
        nicks={
            "2022postEE": [
                "WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "WplusH_Hto2B_Wto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="wplush_h2b_wlnu",
        nicks={
            "2022postEE": [
                "WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "WplusH_Hto2B_WtoLNu_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="zh_h2b_z2l",
        nicks={
            "2022postEE": [
                "ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "ZH_Hto2B_Zto2L_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

    add_dataset_from_sample_database(
        config,
        name="zh_h2b_z2q",
        nicks={
            "2022postEE": [
                "ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X",
                "ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22EENanoAODv12-130X_ext1",
            ],
            "2022preEE": [
                "ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X",
                "ZH_Hto2B_Zto2Q_M-125_TuneCP5_13p6TeV_powheg-pythia8_Run3Summer22NanoAODv12-130X_ext1",
            ],
            "2023preBPix": [],
            "2023postBPix": [],
            "2024": [],
        },
    )

