from collections import OrderedDict

from bbtautau.shapes import AnalysisContext


__all__ = [
    "z_ee_mumu_gen_selection",
    "z_tautau_gen_selection",
    "tautau_from_genuine_tau_selection",
    "tautau_from_jet_fake_selection",
    "tautau_from_remaining_selection",
]


def z_ee_mumu_gen_selection(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Add selection for for Drell-Yan events with an electron or a muon pair in
    the generator-level final state.

    This selection is needed for the Drell-Yan samples in Run 3, generated with
    `MadGraph5_aMC@NLO`. The full `"DYto2L*"` samples have a bug in the
    generation of $Z \\to \\tau\\tau$ events, which need to be removed in the
    selection. For Drell-Yan processes with tau leptons in the final state,
    dedicated `"DYto2Tau*"` samples exist.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. This is just a placeholder to provdide a consistent
        interface for all selection modules.

    :return: Collection of filter operations.
    """

    # Add the generator-level selection for Drell-Yan decays into electrons
    # (PDG ID 11) or muons (PDG ID 13)
    selections = OrderedDict([
        (
            "gen_z_ee_mumu_selection",
            """
            (
                (lhe_drell_yan_decay_flavor == 11)
                || (lhe_drell_yan_decay_flavor == 13)
            )
            """,
        )
    ])

    return selections


def z_tautau_gen_selection(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Add selection for for Drell-Yan events with a tau lepton pair in the
    generator-level final state.

    This selection is needed for the Drell-Yan samples in Run 3, generated with
    `MadGraph5_aMC@NLO`. The full `"DYto2L*"` samples have a bug in the
    generation of $Z \\to \\tau\\tau$ events, which need to be removed in the
    selection. For Drell-Yan processes with tau leptons in the final state,
    dedicated `"DYto2Tau*"` samples exist.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. This is just a placeholder to provdide a consistent
        interface for all selection modules.

    :return: Collection of filter operations.
    """

    # Add the generator-level selection for Drell-Yan decays into taus (PDG ID
    # 15)
    selections = OrderedDict([
        (
            "gen_tautau_selection",
            """
            (lhe_drell_yan_decay_flavor == 15)
            """,
        ),
    ])

    return selections


def tautau_from_genuine_tau_selection(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Create selection for events with genuine tau lepton pairs at generator
    level based on the matching of the di-tau pair candidates to
    generator-level particles.

    The generator matching results for each candidate (`"gen_match_1"`,
    `"gen_match_2"`) are encoded as integers:

    | code | meaning                                       |
    |:----:|:---------------------------------------------:|
    | 0    | not matched / unknown                         |
    | 1    | prompt electron (e.g. from $Z \\to \\mu\\mu$) |
    | 2    | prompt muon (e.g. from $Z \\to \\mu\\mu$)     |
    | 3    | tau decay into electron                       |
    | 4    | tau decay into muon                           |
    | 5    | hadronic tau decay                            |
    | 6    | hadronic tau faked by a jet                   |

    In each channel, the selection requires that both reconstructed tau
    candidates match the corresponding tau decays at generator level, e.g., in
    the $e\\tau_{\\text{h}}$ channel, the first candidate must match to a tau
    decay into an electron, and the second candidate must match to a hadronic
    tau decay.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. The attribute used in this function is
        :py:attr:`~shape_producer.operations.AnalysisContext.channel`.

    :return: Collection of filter operations.
    """

    # Get the channel from the analysis context
    channel = analysis_context.channel

    # Select genuine tau pairs based on the generator matching results
    # depending on the channel
    expression = ""
    if channel.name == "et":
        expression = "(gen_match_1 == 3) && (gen_match_2 == 5)"
    elif channel.name == "mt":
        expression = "(gen_match_1 == 4) && (gen_match_2 == 5)"
    elif channel.name == "tt":
        expression = "(gen_match_1 == 5) && (gen_match_2 == 5)"
    if channel.name == "em":
        expression = "(gen_match_1 == 3) && (gen_match_2 == 4)"
    elif channel.name == "ee":
        expression = "(gen_match_1 == 3) && (gen_match_2 == 3)"
    elif channel.name == "mm":
        expression = "(gen_match_1 == 4) && (gen_match_2 == 4)"

    return OrderedDict([("tautau_from_genuine_tau", expression)])


def tautau_from_jet_fake_selection(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Create selection for events with at least one
    $\\text{jet} \\to \\tau_{\\text{h}}$ fake at generator level based on the
    matching of the di-tau pair candidates to generator-level particles.

    The generator matching results for each candidate (`"gen_match_1"`,
    `"gen_match_2"`) are encoded as integers:

    | code | meaning                                       |
    |:----:|:---------------------------------------------:|
    | 0    | not matched / unknown                         |
    | 1    | prompt electron (e.g. from $Z \\to \\mu\\mu$) |
    | 2    | prompt muon (e.g. from $Z \\to \\mu\\mu$)     |
    | 3    | tau decay into electron                       |
    | 4    | tau decay into muon                           |
    | 5    | hadronic tau decay                            |
    | 6    | hadronic tau faked by a jet                   |

    In the fullhadronic and semileptonic channels, the selection requires that
    no genuine di-tau pair is found and that at least one hadronic tau is not
    matched to any lepton or tau lepton decay (i.e., it has generator matching
    code 6). In the dileptonic channels, $\\text{jet} \\to \\tau_{\\text{h}}$
    cannot occur.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. The attribute used in this function is
        :py:attr:`~shape_producer.operations.AnalysisContext.channel`.

    :return: Collection of filter operations.
    """

    # Get the channel from the analysis context
    channel = analysis_context.channel

    # Get the selection for genuine tau pairs to veto them here
    genuine_tau_selections = tautau_from_genuine_tau_selection(analysis_context)

    # Select jet -> tau_h  fakes based on the generator matching results
    # depending on the channel. For channels without hadronic taus, no jet ->
    # tau_h fakes can occur.
    expression = ""
    expression_tautau = " && ".join(genuine_tau_selections.values())
    if channel.name in ["et", "mt"]:
        expression = f"""
            !({expression_tautau})
            && (gen_match_2 == 6)
        """

    elif channel.name == "tt":
        expression = f"""
            !({expression_tautau})
            && ( (gen_match_1 == 6) || (gen_match_2 == 6) )
        """

    else:
        expression = "false"

    return OrderedDict([("tautau_from_jet_fake", expression)])


def tautau_from_remaining_selection(
    analysis_context: AnalysisContext,
) -> OrderedDict[str, str]:
    """
    Create selection for events with $\\ell \\to \\tau_{\\text{h}}$ fakes or
    lepton fakes at generator level based on the matching of the di-tau pair
    candidates to generator-level particles. This selection includes all
    events, that are not covered by the genuine tau pair selection or the
    $\\text{jet} \\to \\tau_{\\text{h}}$ fake selection in
    :py:func:`tautau_from_genuine_tau_selection` and
    :py:func:`tautau_from_jet_fake_selection`.

    The generator matching results for each candidate (`"gen_match_1"`,
    `"gen_match_2"`) are encoded as integers:

    | code | meaning                                       |
    |:----:|:---------------------------------------------:|
    | 0    | not matched / unknown                         |
    | 1    | prompt electron (e.g. from $Z \\to \\mu\\mu$) |
    | 2    | prompt muon (e.g. from $Z \to \\mu\\mu$)      |
    | 3    | tau decay into electron                       |
    | 4    | tau decay into muon                           |
    | 5    | hadronic tau decay                            |
    | 6    | hadronic tau faked by a jet                   |

    In all channels, the selection requires that no genuine di-tau pair and no
    $\\text{jet} \\to \\tau_{\\text{h}}$ fake is found in the event.

    :param analysis_context: Analysis context, to which the selections should
        be tailored. The attribute used in this function is
        :py:attr:`~shape_producer.operations.AnalysisContext.channel`.

    :return: Collection of filter operations.
    """

    # Get the selections for genuine tau pairs and jet -> tau_h fakes to veto
    # them here
    genuine_tau_selections = tautau_from_genuine_tau_selection(analysis_context)
    jet_fake_selections = tautau_from_jet_fake_selection(analysis_context)
    expression_tautau = " && ".join(genuine_tau_selections.values())
    expression_jet_fake = " && ".join(jet_fake_selections.values())

    # Select genuine tau pairs based on the generator matching results
    # depending on the channel. Select events that do not have a genuine tau
    # pair and that do not have a jet -> tau_h fake.
    selections = OrderedDict(
        [
            (
                "tautau_from_lepton_fake",
                f"""
                (
                    !({expression_tautau})
                    && !({expression_jet_fake})
                )
                """,
            ),
        ],
    )

    return selections
