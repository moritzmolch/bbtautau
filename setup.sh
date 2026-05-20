#!/usr/bin/env bash

main () {
    # Local variables containing the shell environment and the current location
    local shell_is_zsh="$( [ -z "${ZSH_VERSION}" ] && echo "false" || echo "true" )"
    local this_file="$( ${shell_is_zsh} && echo "${(%):-%x}" || echo "${BASH_SOURCE[0]}" )"
    local this_dir="$( cd "$( dirname "${this_file}" )" && pwd )"

    # Important paths of this project
    export BBTT_BASE="${this_dir}"
    export BBTT_DATA="${BBTT_BASE}/data/output"

    # Activate the micromamba enviroment
    # TODO temporary solution, could be refined by automatically install the
    # enviroment
    micromamba activate bbtautau
    #source /cvmfs/sft.cern.ch/lcg/views/LCG_109/x86_64-el9-gcc15-opt/setup.sh

    export PYTHONPATH="${BBTT_BASE}/src:${BBTT_BASE}:${PYTHONPATH}"
    # law setup
    export LAW_HOME="${LAW_HOME:-${BBTT_BASE}/.law}"
    export LAW_CONFIG_FILE="${LAW_CONFIG_FILE:-${BBTT_BASE}/law.cfg}"

    # If law binary can be found, enable auto-completion and index tasks
    # silently
    if which law &> /dev/null; then
        source "$( law completion )" ""
        law index -q
    fi
}


main "${@}"

