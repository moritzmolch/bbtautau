from order import Channel
from numpy import arange, concatenate, linspace, pi


def cat(*args):
    """
    Shortcut to the `np.concatenate` function for merging arrays along
    `axis=0`.
    """
    return concatenate(args, axis=0)


def add_variables(
    channel: Channel,
):
    """
    Add variables to an :py:class:~order.Channel`.

    :param channel: The analysis channel instance.
    """

    labels = {
        "pt_1": {
            "et": r"Electron $p_{\text{T}}$",
            "mt": r"Muon $p_{\text{T}}$",
            "tt": r"Leading hadronic $\tau$ $p_{\text{T}}$",
            "em": r"Electron $p_{\text{T}}$",
            "ee": r"Leading electron $p_{\text{T}}$",
            "mm": r"Leading muon $p_{\text{T}}$",
        },
        "pt_2": {
            "et": r"Hadronic $\tau$ $p_{\text{T}}$",
            "mt": r"Hadronic $\tau$ $p_{\text{T}}$",
            "tt": r"Subleading hadronic $\tau$ $p_{\text{T}}$",
            "em": r"Muon $p_{\text{T}}$",
            "ee": r"Subleading electron $p_{\text{T}}$",
            "mm": r"Subleading muon $p_{\text{T}}$",
        },
        "eta_1": {
            "et": r"Electron $\eta$",
            "mt": r"Muon $\eta$",
            "tt": r"Leading hadronic $\tau$ $\eta$",
            "em": r"Electron $\eta$",
            "ee": r"Leading electron $\eta$",
            "mm": r"Leading muon $\eta$",
        },
        "eta_2": {
            "et": r"Hadronic $\tau$ $\eta$",
            "mt": r"Hadronic $\tau$ $\eta$",
            "tt": r"Subeading hadronic $\tau$ $\eta$",
            "em": r"Muon $\eta$",
            "ee": r"Subleading electron $\eta$",
            "mm": r"Subleading muon $\eta$",
        },
        "phi_1": {
            "et": r"Electron $\phi$",
            "mt": r"Muon $\phi$",
            "tt": r"Leading hadronic $\tau$ $\phi$",
            "em": r"Electron $\phi$",
            "ee": r"Leading electron $\phi$",
            "mm": r"Leading muon $\phi$",
        },
        "phi_2": {
            "et": r"Hadronic $\tau$ $\phi$",
            "mt": r"Hadronic $\tau$ $\phi$",
            "tt": r"Subeading hadronic $\tau$ $\phi$",
            "em": r"Muon $\phi$",
            "ee": r"Subleading electron $\phi$",
            "mm": r"Subleading muon $\phi$",
        },
        "mass_1": {
            "et": r"Electron mass",
            "mt": r"Muon mass",
            "tt": r"Leading hadronic $\tau$ mass",
            "em": r"Electron mass",
            "ee": r"Leading electron mass",
            "mm": r"Leading muon mass",
        },
        "mass_2": {
            "et": r"Hadronic $\tau$ mass",
            "mt": r"Hadronic $\tau$ mass",
            "tt": r"Subeading hadronic $\tau$ mass",
            "em": r"Muon mass",
            "ee": r"Subleading electron mass",
            "mm": r"Subleading muon mass",
        },
        "iso_1": {
            "et": r"Electron $I_{\text{rel}}^{\text{e}}$",
            "mt": r"Muon $I_{\text{rel}}^{\mu}$",
            "tt": r"Leading hadronic $\tau$ DeepTau vs. jets score",
            "em": r"Electron $I_{\text{rel}}^{\text{e}}$",
            "ee": r"Leading electron $I_{\text{rel}}^{\text{e}}$",
            "mm": r"Leading muon $I_{\text{rel}}^{\mu}$",
        },
        "iso_2": {
            "et": r"Hadronic $\tau$ DeepTau vs. jets score",
            "mt": r"Hadronic $\tau$ DeepTau vs. jets score",
            "tt": r"Subleading hadronic $\tau$ DeepTau vs. jets score",
            "em": r"Muon $I_{\text{rel}}^{\mu}$",
            "ee": r"Subleading electron $I_{\text{rel}}^{\text{e}}$",
            "mm": r"Subleading muon $I_{\text{rel}}^{\mu}$",
        },
        "tau_decaymode_1": {
            "et": "",
            "mt": "",
            "tt": r"Leading hadronic $\tau$ decay mode",
            "em": "",
            "ee": "",
            "mm": "",
        },
        "tau_decaymode_2": {
            "et": r"Hadronic $\tau$ decay mode",
            "mt": r"Hadronic $\tau$ decay mode",
            "tt": r"Subleading hadronic $\tau$ decay mode",
            "em": "",
            "ee": "",
            "mm": "",
        },
        "m_vis": {
            "et": r"Visible di-$\tau$ mass $m_{\text{vis}}$",
            "mt": r"Visible di-$\tau$ mass $m_{\text{vis}}$",
            "tt": r"Visible di-$\tau$ mass $m_{\text{vis}}$",
            "em": r"Dilepton mass $m_{\ell\ell}$",
            "ee": r"Dilepton mass $m_{\ell\ell}$",
            "mm": r"Dilepton mass $m_{\ell\ell}$",
        },
        "pt_vis": {
            "et": r"Visible di-$\tau$ $p_{\text{T}}$",
            "mt": r"Visible di-$\tau$ $p_{\text{T}}$",
            "tt": r"Visible di-$\tau$ $p_{\text{T}}$",
            "em": r"Dilepton $p_{\text{T}}$",
            "ee": r"Dilepton $p_{\text{T}}$",
            "mm": r"Dilepton $p_{\text{T}}$",
        },
        "deltaR_ditaupair": {
            "et": r"$\Delta R(\text{e}, \tau_{\text{h}})$",
            "mt": r"$\Delta R(\mu, \tau_{\text{h}})$",
            "tt": r"$\Delta R(\tau_{\text{h}}^{\text{lead}}, \tau_{\text{h}}^{\text{sub}})$",
            "em": r"$\Delta R(\text{e}, \mu)$",
            "ee": r"$\Delta R(\text{e}^{\text{lead}}, \text{e}^{\text{sub}})$",
            "mm": r"$\Delta R(\mu^{\text{lead}}, \mu^{\text{sub}})$",
        },
        "met": {
            "et": r"PUPPI MET $p_{\mathrm{T}}^{\mathrm{miss}}$",
            "mt": r"PUPPI MET $p_{\mathrm{T}}^{\mathrm{miss}}$",
            "tt": r"PUPPI MET $p_{\mathrm{T}}^{\mathrm{miss}}$",
            "em": r"PUPPI MET $p_{\mathrm{T}}^{\mathrm{miss}}$",
            "ee": r"PUPPI MET $p_{\mathrm{T}}^{\mathrm{miss}}$",
            "mm": r"PUPPI MET $p_{\mathrm{T}}^{\mathrm{miss}}$",
        },
        "metphi": {
            "et": r"PUPPI MET $\phi$",
            "mt": r"PUPPI MET $\phi$",
            "tt": r"PUPPI MET $\phi$",
            "em": r"PUPPI MET $\phi$",
            "ee": r"PUPPI MET $\phi$",
            "mm": r"PUPPI MET $\phi$",
        },
        "mt_1": {
            "et": r"Transverse mass $m_{\text{T}}(\text{e}, p_{\text{T}}^{\text{miss}})$",
            "mt": r"Transverse mass $m_{\text{T}}(\mu, p_{\text{T}}^{\text{miss}})$",
            "tt": r"Transverse mass $m_{\text{T}}(\tau_{\text{h}}^{\text{lead}}, p_{\text{T}}^{\text{miss}})$",
            "em": "",
            "ee": "",
            "mm": "",
        },
        "mt_2": {
            "et": r"Transverse mass $m_{\text{T}}(\tau_{\text{h}}, p_{\text{T}}^{\text{miss}})$",
            "mt": r"Transverse mass $m_{\text{T}}(\tau_{\text{h}}, p_{\text{T}}^{\text{miss}})$",
            "tt": r"Transverse mass $m_{\text{T}}(\tau_{\text{h}}^{\text{sub}}, p_{\text{T}}^{\text{miss}})$",
            "em": "",
            "ee": "",
            "mm": "",
        },
        "mt_tot": {
            "et": r"Transverse mass $m_{\text{T}}^{\text{tot}}$",
            "mt": r"Transverse mass $m_{\text{T}}^{\text{tot}}$",
            "tt": r"Transverse mass $m_{\text{T}}^{\text{tot}}$",
            "em": "",
            "ee": "",
            "mm": "",
        },
        "jpt_1": {
            c: r"Leading jet $p_{\text{T}}$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "jpt_2": {
            c: r"Subleading jet $p_{\text{T}}$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "jeta_1": {
            c: r"Leading jet $\eta$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "jeta_2": {
            c: r"Subleading jet $\eta$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "jphi_1": {
            c: r"Leading jet $\phi$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "jphi_2": {
            c: r"Subleading jet $\phi$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_pt_1": {
            c: r"First b candidate $p_{\text{T}}$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_pt_2": {
            c: r"Second b candidate $p_{\text{T}}$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_eta_1": {
            c: r"First b candidate $\eta$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_eta_2": {
            c: r"Second b candidate $\eta$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_phi_1": {
            c: r"First b candidate $\phi$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_phi_2": {
            c: r"Second b candidate $\phi$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_btag_value_1": {
            c: r"First b candidate tagging score"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_btag_value_2": {
            c: r"Second b candidate tagging score"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_m_inv": {
            c: r"bb candidate mass"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "bpair_deltaR": {
            c: r"$\Delta R(\text{b}_1, \text{b}_2)$"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "n_jets": {
            c: r"Number of jets" for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "n_bjets": {
            c: r"Number of b-tagged jets"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_0": {
            c: r"Y(bb)H($\tau\tau$) discriminant"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_1": {
            c: r"Y($\tau\tau$)H(bb) discriminant"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_2": {
            c: r"DY+diboson discriminant"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_3": {
            c: r"$\text{Jet} \to \tau_{\text{h}}$ discriminant"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_4": {
            c: r"t$\bar{t}$+single t discriminant"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_5": {
            c: r"Higgs discriminant"
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
    }

    binnings = {
        "pt_1": {
            "et": cat([0, 32], arange(35, 185, 5)).tolist(),
            "mt": cat([0, 26], arange(30, 185, 5)).tolist(),
            "tt": cat([0, 40], arange(50, 190, 10)).tolist(),
            "em": cat([0, 32], arange(35, 185, 5)).tolist(),
            "ee": cat([0, 32], arange(35, 185, 5)).tolist(),
            "mm": cat([0, 26], arange(30, 185, 5)).tolist(),
        },
        "pt_2": {
            "et": cat([0, 20], arange(30, 185, 5)).tolist(),
            "mt": cat([0, 20], arange(30, 185, 5)).tolist(),
            "tt": cat([0, 40], arange(50, 190, 10)).tolist(),
            "em": cat([0, 26], arange(30, 185, 5)).tolist(),
            "ee": cat([0, 20], arange(25, 185, 5)).tolist(),
            "mm": cat([0, 20], arange(25, 185, 5)).tolist(),
        },
        "eta_1": {
            "et": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "mt": linspace(-2.4, 2.4, 41, endpoint=True).tolist(),
            "tt": linspace(-2.5, 2.5, 21, endpoint=True).tolist(),
            "em": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "ee": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "mm": linspace(-2.4, 2.4, 41, endpoint=True).tolist(),
        },
        "eta_2": {
            "et": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "mt": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "tt": linspace(-2.5, 2.5, 21, endpoint=True).tolist(),
            "em": linspace(-2.4, 2.4, 41, endpoint=True).tolist(),
            "ee": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "mm": linspace(-2.4, 2.4, 41, endpoint=True).tolist(),
        },
        "phi_1": {
            "et": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mt": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "tt": linspace(-pi, pi, 21, endpoint=True).tolist(),
            "em": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "ee": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mm": linspace(-pi, pi, 41, endpoint=True).tolist(),
        },
        "phi_2": {
            "et": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mt": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "tt": linspace(-pi, pi, 21, endpoint=True).tolist(),
            "em": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "ee": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mm": linspace(-pi, pi, 41, endpoint=True).tolist(),
        },
        "mass_1": {
            "et": linspace(0, 0.001, 40, endpoint=True).tolist(),
            "mt": linspace(0, 0.2, 40, endpoint=True).tolist(),
            "tt": linspace(0, 2, 20, endpoint=True).tolist(),
            "em": linspace(0, 0.001, 40, endpoint=True).tolist(),
            "ee": linspace(0, 0.001, 40, endpoint=True).tolist(),
            "mm": linspace(0, 0.2, 40, endpoint=True).tolist(),
        },
        "mass_2": {
            "et": linspace(0, 2, 40, endpoint=True).tolist(),
            "mt": linspace(0, 2, 40, endpoint=True).tolist(),
            "tt": linspace(0, 2, 20, endpoint=True).tolist(),
            "em": linspace(0, 0.2, 40, endpoint=True).tolist(),
            "ee": linspace(0, 0.001, 40, endpoint=True).tolist(),
            "mm": linspace(0, 0.2, 40, endpoint=True).tolist(),
        },
        "iso_1": {
            "et": arange(0, 0.155, 0.005).tolist(),
            "mt": arange(0, 0.155, 0.005).tolist(),
            "tt": arange(0.9, 1.005, 0.005).tolist(),
            "em": arange(0, 0.155, 0.005).tolist(),
            "ee": arange(0, 0.155, 0.005).tolist(),
            "mm": arange(0, 0.155, 0.005).tolist(),
        },
        "iso_2": {
            "et": arange(0.9, 1.005, 0.005).tolist(),
            "mt": arange(0.9, 1.005, 0.005).tolist(),
            "tt": arange(0.9, 1.005, 0.005).tolist(),
            "em": arange(0, 0.155, 0.005).tolist(),
            "ee": arange(0, 0.155, 0.005).tolist(),
            "mm": arange(0, 0.155, 0.005).tolist(),
        },
        "tau_decaymode_1": {
            "et": [],
            "mt": [],
            "tt": arange(-0.5, 12.5, 1.0).tolist(),
            "em": [],
            "ee": [],
            "mm": [],
        },
        "tau_decaymode_2": {
            "et": arange(-0.5, 12.5, 1.0).tolist(),
            "mt": arange(-0.5, 12.5, 1.0).tolist(),
            "tt": arange(-0.5, 12.5, 1.0).tolist(),
            "em": [],
            "ee": [],
            "mm": [],
        },
        "m_vis": {
            "et": arange(0, 205, 5).tolist(),
            "mt": arange(0, 205, 5).tolist(),
            "tt": arange(0, 210, 10).tolist(),
            "em": arange(0, 205, 5).tolist(),
            "ee": arange(0, 205, 5).tolist(),
            "mm": arange(0, 205, 5).tolist(),
        },
        "pt_vis": {
            "et": arange(0, 185, 5).tolist(),
            "mt": arange(0, 185, 5).tolist(),
            "tt": arange(0, 190, 10).tolist(),
            "em": arange(0, 185, 5).tolist(),
            "ee": arange(0, 185, 5).tolist(),
            "mm": arange(0, 185, 5).tolist(),
        },
        "deltaR_ditaupair": {
            "et": arange(0, 6.2, 0.2).tolist(),
            "mt": arange(0, 6.2, 0.2).tolist(),
            "tt": arange(0, 6.4, 0.4).tolist(),
            "em": arange(0, 6.2, 0.2).tolist(),
            "ee": arange(0, 6.2, 0.2).tolist(),
            "mm": arange(0, 6.2, 0.2).tolist(),
        },
        "met": {
            "et": arange(0, 185, 5).tolist(),
            "mt": arange(0, 185, 5).tolist(),
            "tt": arange(0, 190, 10).tolist(),
            "em": arange(0, 185, 5).tolist(),
            "ee": arange(0, 185, 5).tolist(),
            "mm": arange(0, 185, 5).tolist(),
        },
        "metphi": {
            "et": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mt": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "tt": linspace(-pi, pi, 21, endpoint=True).tolist(),
            "em": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "ee": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mm": linspace(-pi, pi, 41, endpoint=True).tolist(),
        },
        "mt_1": {
            "et": arange(0, 185, 5).tolist(),
            "mt": arange(0, 185, 5).tolist(),
            "tt": arange(0, 190, 10).tolist(),
            "em": [],
            "ee": [],
            "mm": [],
        },
        "mt_2": {
            "et": arange(0, 185, 5).tolist(),
            "mt": arange(0, 185, 5).tolist(),
            "tt": arange(0, 190, 10).tolist(),
            "em": [],
            "ee": [],
            "mm": [],
        },
        "mt_tot": {
            "et": arange(0, 410, 10).tolist(),
            "mt": arange(0, 410, 10).tolist(),
            "tt": arange(0, 420, 20).tolist(),
            "em": [],
            "ee": [],
            "mm": [],
        },
        "jpt_1": {
            "et": arange(0, 185, 5).tolist(),
            "mt": arange(0, 185, 5).tolist(),
            "tt": arange(0, 190, 10).tolist(),
            "em": arange(0, 185, 5).tolist(),
            "ee": arange(0, 185, 5).tolist(),
            "mm": arange(0, 185, 5).tolist(),
        },
        "jpt_2": {
            "et": arange(0, 185, 5).tolist(),
            "mt": arange(0, 185, 5).tolist(),
            "tt": arange(0, 190, 10).tolist(),
            "em": arange(0, 185, 5).tolist(),
            "ee": arange(0, 185, 5).tolist(),
            "mm": arange(0, 185, 5).tolist(),
        },
        "jeta_1": {
            "et": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "mt": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "tt": linspace(-4.7, 4.7, 21, endpoint=True).tolist(),
            "em": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "ee": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "mm": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
        },
        "jeta_2": {
            "et": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "mt": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "tt": linspace(-4.7, 4.7, 21, endpoint=True).tolist(),
            "em": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "ee": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "mm": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
        },
        "jphi_1": {
            "et": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mt": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "tt": linspace(-pi, pi, 21, endpoint=True).tolist(),
            "em": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "ee": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mm": linspace(-pi, pi, 41, endpoint=True).tolist(),
        },
        "jphi_2": {
            "et": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mt": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "tt": linspace(-pi, pi, 21, endpoint=True).tolist(),
            "em": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "ee": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mm": linspace(-pi, pi, 41, endpoint=True).tolist(),
        },
        "bpair_pt_1": {
            "et": arange(0, 265, 5).tolist(),
            "mt": arange(0, 265, 5).tolist(),
            "tt": arange(0, 270, 10).tolist(),
            "em": arange(0, 265, 5).tolist(),
            "ee": arange(0, 265, 5).tolist(),
            "mm": arange(0, 265, 5).tolist(),
        },
        "bpair_pt_2": {
            "et": arange(0, 265, 5).tolist(),
            "mt": arange(0, 265, 5).tolist(),
            "tt": arange(0, 270, 10).tolist(),
            "em": arange(0, 265, 5).tolist(),
            "ee": arange(0, 265, 5).tolist(),
            "mm": arange(0, 265, 5).tolist(),
        },
        "bpair_eta_1": {
            "et": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "mt": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "tt": linspace(-2.5, 2.5, 21, endpoint=True).tolist(),
            "em": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "ee": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
            "mm": linspace(-2.5, 2.5, 41, endpoint=True).tolist(),
        },
        "bpair_eta_2": {
            "et": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "mt": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "tt": linspace(-4.7, 4.7, 21, endpoint=True).tolist(),
            "em": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "ee": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
            "mm": linspace(-4.7, 4.7, 41, endpoint=True).tolist(),
        },
        "bpair_phi_1": {
            "et": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mt": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "tt": linspace(-pi, pi, 21, endpoint=True).tolist(),
            "em": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "ee": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mm": linspace(-pi, pi, 41, endpoint=True).tolist(),
        },
        "bpair_phi_2": {
            "et": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mt": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "tt": linspace(-pi, pi, 21, endpoint=True).tolist(),
            "em": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "ee": linspace(-pi, pi, 41, endpoint=True).tolist(),
            "mm": linspace(-pi, pi, 41, endpoint=True).tolist(),
        },
        "bpair_btag_value_1": {
            "et": arange(0.0, 1.025, 0.025).tolist(),
            "mt": arange(0.0, 1.025, 0.025).tolist(),
            "tt": arange(0.0, 1.05, 0.05).tolist(),
            "em": arange(0.0, 1.025, 0.025).tolist(),
            "ee": arange(0.0, 1.025, 0.025).tolist(),
            "mm": arange(0.0, 1.025, 0.025).tolist(),
        },
        "bpair_btag_value_2": {
            "et": arange(0.0, 1.025, 0.025).tolist(),
            "mt": arange(0.0, 1.025, 0.025).tolist(),
            "tt": arange(0.0, 1.05, 0.05).tolist(),
            "em": arange(0.0, 1.025, 0.025).tolist(),
            "ee": arange(0.0, 1.025, 0.025).tolist(),
            "mm": arange(0.0, 1.025, 0.025).tolist(),
        },
        "bpair_m_inv": {
            "et": arange(0, 1050, 50).tolist(),
            "mt": arange(0, 1050, 50).tolist(),
            "tt": arange(0, 1100, 100).tolist(),
            "em": arange(0, 1050, 50).tolist(),
            "ee": arange(0, 1050, 50).tolist(),
            "mm": arange(0, 1050, 50).tolist(),
        },
        "bpair_deltaR": {
            "et": arange(0, 6.2, 0.2).tolist(),
            "mt": arange(0, 6.2, 0.2).tolist(),
            "tt": arange(0, 6.4, 0.4).tolist(),
            "em": arange(0, 6.2, 0.2).tolist(),
            "ee": arange(0, 6.2, 0.2).tolist(),
            "mm": arange(0, 6.2, 0.2).tolist(),
        },
        "n_jets": {
            c: arange(-0.5, 8.5, 1.0).tolist()
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "n_bjets": {
            c: arange(-0.5, 5.5, 1.0).tolist()
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_0": {
            c: linspace(0.0, 1.0, 10, endpoint=True).tolist()
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_1": {
            c: linspace(0.0, 1.0, 10, endpoint=True).tolist()
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_2": {
            c: linspace(0.0, 1.0, 10, endpoint=True).tolist()
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_3": {
            c: linspace(0.0, 1.0, 10, endpoint=True).tolist()
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_4": {
            c: linspace(0.0, 1.0, 10, endpoint=True).tolist()
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
        "output_score_5": {
            c: linspace(0.0, 1.0, 10, endpoint=True).tolist()
            for c in ["et", "mt", "tt", "em", "ee", "mm"]
        },
    }
    

    units = {
        "pt_1": "GeV",
        "pt_2": "GeV",
        "eta_1": None,
        "eta_2": None,
        "phi_1": None,
        "phi_2": None,
        "mass_1": "GeV",
        "mass_2": "GeV",
        "iso_1": None,
        "iso_2": None,
        "tau_decaymode_1": None,
        "tau_decaymode_2": None,
        "m_vis": "GeV",
        "pt_vis": "GeV",
        "deltaR_ditaupair": None,
        "met": "GeV",
        "metphi": None,
        "mt_1": "GeV",
        "mt_2": "GeV",
        "mt_tot": "GeV",
        "jpt_1": "GeV",
        "jpt_2": "GeV",
        "jeta_1": None,
        "jeta_2": None,
        "jphi_1": None,
        "jphi_2": None,
        "bpair_pt_1": "GeV",
        "bpair_pt_2": "GeV",
        "bpair_eta_1": None,
        "bpair_eta_2": None,
        "bpair_phi_1": None,
        "bpair_phi_2": None,
        "bpair_btag_value_1": None,
        "bpair_btag_value_2": None,
        "bpair_m_inv": "GeV",
        "bpair_deltaR": None,
        "n_jets": None,
        "n_bjets": None,
        "output_score_0": None,
        "output_score_1": None,
        "output_score_2": None,
        "output_score_3": None,
        "output_score_4": None,
        "output_score_5": None,
    }

    for name in labels:
        # If an empty list of bin edges is provided, the variable is not
        # considered for this channel.
        if len(binnings[name][channel.name]) == 0:
            continue

        # Add variable with values given in the dictionaries above.
        channel.add_variable(
            name=name,
            id="+",
            x_title=labels[name][channel.name],
            unit=units[name],
            unit_format="{title} ({unit})",
            binning=binnings[name][channel.name],
        )

