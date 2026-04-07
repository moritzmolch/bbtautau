from order import Config

from configuration.xyh_bbtautau.constants import (
    XYH_MASS_POINTS,
    XYH_DECAY_MODES,
)
# from configuration.xyh_bbtautau.producers.weights.processes import (
#     z_pt_reweighting_weights,
#     tt_top_pt_reweighting_weights,
#     tt_normalization_weights,
# )
# from configuration.xyh_bbtautau.producers.weights.dy import (
#     z_ee_mumu_gen_selection,
#     z_tautau_gen_selection,
# )
# from configuration.xyh_bbtautau.producers.selections.gen_taus import (
#     tautau_from_genuine_tau_selection,
#     tautau_from_jet_fake_selection,
#     tautau_from_remaining_selection,
# )


z_pt_reweighting_weights = "DUMMY"
tt_top_pt_reweighting_weights = "DUMMY"
tt_normalization_weights = "DUMMY"
z_ee_mumu_gen_selection = "DUMMY"
z_tautau_gen_selection = "DUMMY"
tautau_from_genuine_tau_selection = "DUMMY"
tautau_from_jet_fake_selection = "DUMMY"
tautau_from_remaining_selection = "DUMMY"


def add_data_processes(config: Config):
    """
    Add data processes to the campaign configuration.

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # Create a process for each data stream
    for name in ["egamma", "muon", "tau"]:
        config.add_process(
            name=name,
            id="+",
            is_data=True,
            datasets=[config.get_dataset(name)],
        )


def add_signal_processes(config_inst: Config):
    """
    Add signal processes to the campaign configuration.
    """

    # Create a process for each mass hypothesis and for each decay mode of Y/H
    for y_decay_mode, h_decay_mode in XYH_DECAY_MODES:
        for m_x, m_y in XYH_MASS_POINTS:
            if y_decay_mode == "2b" and h_decay_mode == "2tau" and m_x == 2500 and m_y == 800:
                continue
            if y_decay_mode == "2tau" and h_decay_mode == "2b" and m_x == 2500 and m_y == 90:
                continue
            name = f"xyh_y{y_decay_mode}_h{h_decay_mode}_mx{m_x}_my{m_y}"
            config_inst.add_process(
                name=name,
                id="+",
                is_data=False,
                datasets=(
                    [config_inst.get_dataset(name)]
                    if config_inst.campaign.name == "2024" else
                    []
                ),
                aux={
                    "is_signal": True,
                    "m_x": m_x,
                    "m_y": m_y,
                    "y_decay_mode": y_decay_mode,
                    "h_decay_mode": h_decay_mode,
                },
            )


def add_tt_processes(config: Config):
    """
    Add top quark pair production processes to the campaign configuration.

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # Input datasets for tt production
    tt_datasets = [
        config.get_dataset(dataset_name)
        for dataset_name in ["tt_2l2nu", "tt_lnu2q", "tt_4q"]
    ]

    # Operations for tt samples
    special_weights = [
        tt_top_pt_reweighting_weights,
        tt_normalization_weights,
    ]

    # tt production -- genuine tau tau pairs
    config.add_process(
        name="tt_tautau",
        id="+",
        is_data=False,
        datasets=tt_datasets,
        aux={
            "special_selections": [tautau_from_genuine_tau_selection],
            "special_weights": special_weights,
        },
    )

    # tt production -- jets faking hadronic taus
    config.add_process(
        name="tt_jetfakes",
        id="+",
        is_data=False,
        datasets=tt_datasets,
        tags={"jetfakes"},
        aux={
            "special_selections": [tautau_from_jet_fake_selection],
            "special_weights": special_weights,
        },
    )

    # tt production -- remaining events (leptons faking hadronic taus, prompt
    # leptons, ...)
    config.add_process(
        name="tt_rem",
        id="+",
        is_data=False,
        datasets=tt_datasets,
        aux={
            "special_selections": [tautau_from_remaining_selection],
            "special_weights": special_weights,
        },
    )


def add_single_t_processes(config: Config):
    """
    Add single top quark production processes to the campaign configuration.

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # Get the campaign as the dataset composition differs for 2022+2023 and
    # 2024
    campaign_inst = config.campaign

    # Collect the datasets for the single_t processes
    single_t_datasets = []

    if campaign_inst.x.year in [2022, 2023]:
        # In 2022+2023, inclusive samples are used in the t channel. Only the
        # fulleptonic final state is considered for the s channel. In
        # the tW channel, the fullhadronic final state is not processed.
        single_t_datasets = [
            config.get_dataset(dataset_name)
            for dataset_name in [
                # tW channel
                "twminus_2l2nu",
                "twminus_lnu2q",
                "twplus_2l2nu",
                "twplus_lnu2q",
                # t channel
                "tbq_top_tchannel",
                "tbq_antitop_tchannel",
                # s channel
                "tb_lnu_top_schannel",
                "tb_lnu_antitop_schannel",
            ]
        ]

    elif campaign_inst.x.year in [2024]:
        # In 2024, samples for all channels are split in the final-state
        # composition. All final states are considered.
        single_t_datasets = [
            config.get_dataset(dataset_name)
            for dataset_name in [
                # tW channel
                "twminus_2l2nu",
                "twminus_lnu2q",
                "twplus_2l2nu",
                "twplus_lnu2q",
                # t channel
                "tbq_lnu_top_tchannel",
                "tbq_2q_top_tchannel",
                "tbq_lnu_antitop_tchannel",
                "tbq_2q_antitop_tchannel",
                # s channel
                "tb_lnu_top_schannel",
                "tb_2q_top_schannel",
                "tb_lnu_antitop_schannel",
                "tb_2q_antitop_schannel",
            ]
        ]

    # Single top quark production -- genuine tau tau pairs
    config.add_process(
        name="single_t_tautau",
        id="+",
        is_data=False,
        datasets=single_t_datasets,
        aux={
            "special_selections": [tautau_from_genuine_tau_selection],
        },
    )

    # Single top production -- jets faking hadronic taus
    config.add_process(
        name="single_t_jetfakes",
        id="+",
        is_data=False,
        datasets=single_t_datasets,
        tags={"jetfakes"},
        aux={
            "special_selections": [tautau_from_jet_fake_selection],
        },
    )

    # Single top production -- remaining events (leptons faking hadronic
    # taus, prompt leptons, ...)
    config.add_process(
        name="single_t_rem",
        id="+",
        is_data=False,
        datasets=single_t_datasets,
        tags={"jetfakes"},
        aux={
            "special_selections": [tautau_from_remaining_selection],
        },
    )


def add_dy_processes(config: Config):
    """
    Add DY production processes to the campaign configuration.

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # Get the campaign as the dataset composition differs for 2022+2023 and
    # 2024
    campaign_inst = config.campaign

    # Collect the datasets for the dy_2e_2mu* and the dy_2tau* processes
    dy_2e_2mu_datasets, dy_2tau_datasets = [], []

    if campaign_inst.x.year in [2022, 2023]:
        # In 2022+2023, DY events are taken from inclusive DYto2L samples and
        # a dedicated DYto2Tau sample. The DYto2Tau component is rejected from
        # the DYto2L sample.
        dy_2e_2mu_datasets = [
            config.get_dataset(dataset_name)
            for dataset_name in [
                "dy_2l_m10to50",
                "dy_2l_m50_0j",
                "dy_2l_m50_1j",
                "dy_2l_m50_2j",
            ]
        ]
        dy_2tau_datasets = [
            config.get_dataset(dataset_name)
            for dataset_name in [
                "dy_2tau_m50_0j",
                "dy_2tau_m50_1j",
                "dy_2tau_m50_2j",
            ]
        ]

    elif campaign_inst.x.year in [2024]:
        # In 2024, DY events are taken from DYto2E, DYto2Mu, and DYto2Tau
        # samples, i.e., they are already split in flavors of the final-state
        # particles.
        dy_2e_2mu_datasets = [
            config.get_dataset(dataset_name)
            for dataset_name in [
                "dy_2e_m10to50",
                "dy_2e_m50_0j",
                "dy_2e_m50_1j",
                "dy_2e_m50_2j",
                "dy_2mu_m10to50",
                "dy_2mu_m50_0j",
                "dy_2mu_m50_1j",
                "dy_2mu_m50_2j",
            ]
        ]
        dy_2tau_datasets = [
            config.get_dataset(dataset_name)
            for dataset_name in [
                "dy_2tau_m10to50",
                "dy_2tau_m50_0j",
                "dy_2tau_m50_1j",
                "dy_2tau_m50_2j",
            ]
        ]

    # DY (-> ell ell) production -- genuine tau tau pairs
    config.add_process(
        name="dy_2e_2mu_tautau",
        id="+",
        is_data=False,
        datasets=dy_2e_2mu_datasets,
        aux={
            "special_selections": [
                z_ee_mumu_gen_selection,
                tautau_from_genuine_tau_selection,
            ],
            "special_weights": [z_pt_reweighting_weights],
        },
    )
    config.add_process(
        name="dy_2tau_tautau",
        id="+",
        is_data=False,
        datasets=dy_2tau_datasets,
        aux={
            "special_selections": [
                z_tautau_gen_selection,
                tautau_from_genuine_tau_selection,
            ],
            "special_weights": [
                z_pt_reweighting_weights,
            ],
        },
    )

    # DY (-> ell ell) production -- jets faking hadronic taus
    config.add_process(
        name="dy_2e_2mu_jetfakes",
        id="+",
        is_data=False,
        datasets=dy_2e_2mu_datasets,
        tags={"jetfakes"},
        aux={
            "special_selections": [
                z_ee_mumu_gen_selection,
                tautau_from_jet_fake_selection,
            ],
            "special_weights": [
                z_pt_reweighting_weights,
            ],
        },
    )
    # DY (-> tau tau) production -- jets faking hadronic taus
    config.add_process(
        name="dy_2tau_jetfakes",
        id="+",
        is_data=False,
        datasets=dy_2tau_datasets,
        tags={"jetfakes"},
        aux={
            "special_selections": [
                z_tautau_gen_selection,
                tautau_from_jet_fake_selection,
            ],
            "special_weights": [
                z_pt_reweighting_weights,
            ],
        },
    )

    # DY (-> ell ell) production -- remaining events (leptons faking hadronic
    # taus, prompt leptons, ...)
    config.add_process(
        name="dy_2e_2mu_rem",
        id="+",
        is_data=False,
        datasets=dy_2e_2mu_datasets,
        aux={
            "special_selections": [
                z_ee_mumu_gen_selection,
                tautau_from_remaining_selection,
            ],
            "special_weights": [
                z_pt_reweighting_weights,
            ],
        },
    )

    # DY (-> tau tau) production -- remaining events (leptons faking hadronic
    # taus, prompt leptons, ...)
    config.add_process(
        name="dy_2tau_rem",
        id="+",
        is_data=False,
        datasets=dy_2tau_datasets,
        aux={
            "special_selections": [
                z_tautau_gen_selection,
                tautau_from_remaining_selection,
            ],
            "special_weights": [
                z_pt_reweighting_weights,
            ],
        },
    )


def add_w_processes(config: Config):
    """
    Add W production processes to the campaign configuration.

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # Get the campaign as the dataset composition differs for 2022+2023 and
    # 2024
    campaign_inst = config.campaign

    # Collect the datasets for the w_lnu* processes
    w_lnu_datasets = []

    if campaign_inst.x.year in [2022, 2023]:
        # In 2022+2023, W events are taken from WtoLNu samples, binned in the
        # number of jets.
        w_lnu_datasets = [
            config.get_dataset(dataset_name)
            for dataset_name in [
                "w_lnu_0j",
                "w_lnu_1j",
                "w_lnu_2j",
            ]
        ]

    elif campaign_inst.x.year in [2024]:
        # In 2024, W events are taken from WtoENu, WtoMuNu, and WtoTauNu
        # samples and they are inclusive in the number of jets.
        w_lnu_datasets = [
            config.get_dataset(dataset_name)
            for dataset_name in [
                "w_enu",
                "w_munu",
                "w_taunu",
            ]
        ]

    # W (-> ell nu) production -- genuine tau tau pairs
    config.add_process(
        name="w_lnu_tautau",
        id="+",
        is_data=False,
        datasets=w_lnu_datasets,
        aux={
            "special_selections": [
                tautau_from_genuine_tau_selection,
            ],
        },
    )

    # W (-> ell nu) production -- jets faking hadronic taus
    config.add_process(
        name="w_lnu_jetfakes",
        id="+",
        is_data=False,
        datasets=w_lnu_datasets,
        tags={"jetfakes"},
        aux={
            "special_selections": [
                tautau_from_jet_fake_selection,
            ],
        },
    )

    # W (-> ell nu) production -- remaining events (leptons faking hadronic
    # taus, prompt leptons, ...)
    config.add_process(
        name="w_lnu_rem",
        id="+",
        is_data=False,
        datasets=w_lnu_datasets,
        aux={
            "special_selections": [
                tautau_from_remaining_selection,
            ],
        },
    )


def add_vv_processes(config: Config):
    """
    Add double vector boson production processes to the campaign configuration.

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # Construct list of diboson datasets used for these processes
    vv_datasets = [
        config.get_dataset(dataset_name)
        for dataset_name in ["ww", "wz", "zz"]
    ]

    # VV production -- genuine tau tau pairs
    config.add_process(
        name="vv_tautau",
        id="+",
        is_data=False,
        datasets=vv_datasets,
        aux={
            "special_selections": [
                tautau_from_genuine_tau_selection,
            ],
        },
    )

    # VV production -- jets faking hadronic taus
    config.add_process(
        name="vv_jetfakes",
        id="+",
        is_data=False,
        datasets=vv_datasets,
        tags={"jetfakes"},
        aux={
            "special_selections": [
                tautau_from_jet_fake_selection,
            ],
        },
    )

    # VV production -- remaining events (leptons faking hadronic taus, prompt
    # leptons, ...)
    config.add_process(
        name="vv_rem",
        id="+",
        is_data=False,
        datasets=vv_datasets,
        aux={
            "special_selections": [
                tautau_from_remaining_selection,
            ],
        },
    )


def add_single_h_processes(config: Config):
    """
    Add single Higgs boson production processes to the campaign configuration.

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # Construct list of single Higgs boson datasets used for these processes
    single_h_datasets = [
        config.get_dataset(dataset_name)
        for dataset_name in [
            # H -> tau tau
            "gluglu_h_2tau",
            "vbf_h_2tau",
            # # H -> WW
            # "gluglu_h_2w_2l2nu",
            # "vbf_h_2w_2l2nu",
            # "gluglu_h_2w_lnu2q",
            # "vbf_h_2w_lnu2q",
            # H -> bb
            "gluglu_h_2b",
            "vbf_h_2b",
            # "wminush_h2b_w2q",
            # "wminush_h2b_wlnu",
            # "wplush_h2b_w2q",
            # "wplush_h2b_wlnu",
            # "zh_h_2b_z2l",
            # "zh_h_2b_z2q
            # # H -> ZZ
            # "gluglu_h_2z_2l2q",
            # "gluglu_h_2z_4l",
            # "vbf_h_2z_4l"
            # ttH
            "tth_h_2b",
            "tth_h_non2b",
        ]
    ]

    # Single H production -- genuine tau tau pairs
    config.add_process(
        name="single_h_tautau",
        id="+",
        is_data=False,
        datasets=single_h_datasets,
        aux={
            "special_selections": [tautau_from_genuine_tau_selection],
        },
    )

    # Single H production -- jets faking hadronic taus
    config.add_process(
        name="single_h_jetfakes",
        id="+",
        is_data=False,
        datasets=single_h_datasets,
        tags={"jetfakes"},
        aux={
            "special_selections": [tautau_from_jet_fake_selection],
        },
    )

    # Single H production -- remaining events (leptons faking hadronic taus,
    # prompt leptons, ...)
    config.add_process(
        name="single_h_rem",
        id="+",
        is_data=False,
        datasets=single_h_datasets,
        aux={
            "special_selections": [tautau_from_remaining_selection],
        },
    )


def add_hh_processes(config: Config):
    """
    Add SM Higgs pair production processes to the campaign configuration.

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # SM Higgs pair production, b b tau tau final state, gg fusion
    config.add_process(
        name="gluglu_hh_2b2tau",
        id="+",
        is_data=False,
        datasets=[config.get_dataset("gluglu_hh_2b2tau")],
    )

    # Remaining SM Higgs pair production processes
    # config_inst.add_process(
    #    name="hh_rem",
    #    id="+",
    #    label=r"$\text{H}\text{H}$ (other)",
    #    is_data=False,
    #    datasets=[
    #        config_inst.get_dataset(dataset_name)
    #        for dataset_name in [
    #            "vbf_hh_2b2tau",
    #            "gluglu_hh_4b",
    #            "vbf_hh_4b",
    #            "gluglu_hh_4v",
    #            "vbf_hh_4v",
    #        ]
    #    ],
    #    aux={
    #        "filter_funcs": [],
    #        "weight_funcs": [
    #            "xyh_bbtautau.lib.weight_funcs.base_mc_weights",
    #        ],
    #    },
    # )


def add_data_driven_processes(config: Config):
    """
    Add processes representing data-driven estimates (e.g. jet fakes,
    QCD multijet production).

    :param config: The :py:class:`order.Config` object to add the process.
    """

    # Processes exhibiting jet -> tau_h misidentification
    config.add_process(
        name="jetfakes",
        id="+",
        is_data=False,
        datasets=[],
        aux={
            "is_data_driven": True,
        },
    )


def add_processes(config: Config):
    """
    Add analysis processes to a given configuration instance.

    :param config_inst: The :py:class:`~order.Config` that the processes are
        added to.
    """

    # Data
    add_data_processes(config)

    # X -> YH signals
    add_signal_processes(config)

    # tt production
    add_tt_processes(config)

    # Single t production
    add_single_t_processes(config)

    # DY (-> ell ell) + jets production
    add_dy_processes(config)

    # W (-> ell nu) + jets production
    add_w_processes(config)

    # Diboson production
    add_vv_processes(config)

    # Single H production
    add_single_h_processes(config)

    # HH production
    add_hh_processes(config)

    # Processes representing data-driven estimates
    add_data_driven_processes(config)

