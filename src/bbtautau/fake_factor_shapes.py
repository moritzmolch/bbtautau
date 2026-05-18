from itertools import groupby

from order import (
    Category,
    Process,
    UniqueObjectIndex,
)

from bbtautau.plots import add_th1, load_histograms


def get_fake_factor_histograms(
    histogram_file: str,
    category: Category,
    jetfakes_process: Process,
    data_process: Process,
    subtract_processes: UniqueObjectIndex,
    fake_factor_variation: str,
    variables: list[str],
):
    # Load histograms from file
    histograms = load_histograms(histogram_file)

    # Get all histograms needed for the fake factor shape creation
    histogram_groups = groupby(
        sorted(
            (
                h
                for h in histograms
                if (
                    h["category"] == category.name
                    and (
                        h["process"]
                        in ([data_process.name] + subtract_processes.names())
                    )
                    and h["variation"] == fake_factor_variation
                    and h["variable"] in variables
                )
            ),
            key=lambda x: x["variable"],
        ),
        key=lambda x: x["variable"],
    )

    # Container for the resulting fake factor histograms
    fake_factor_histograms = []

    for variable, selected_histograms in histogram_groups:
        # Materialize the generator to a reusable list
        selected_histograms = list(selected_histograms)

        # Add the data histograms and the histograms of processes to subtract
        h_data = add_th1(
            [
                h["histogram"]
                for h in selected_histograms
                if h["process"] == data_process.name
            ]
        )
        h_subtract = add_th1(
            [
                h["histogram"]
                for h in selected_histograms
                if h["process"] in subtract_processes.names()
            ]
        )

        # Subtract non-jet-fake backgrounds from data
        h_ff = h_data.Clone()
        h_ff.Add(h_subtract, -1)

        # Rename the histogram
        info_data = next(
            (h for h in selected_histograms if h["process"] == data_process)
        )
        name = (
            f"{info_data['dataset']}#"
            + "-".join(
                (
                    info_data["channel"],
                    info_data["category"],
                    jetfakes_process.name,
                    info_data["dataset"],
                )
            )
            + f"#Nominal#{variable}"
        )
        h_ff.SetName(name)
        h_ff.SetTitle(name)

        # Append fake factor histogram to the result list
        fake_factor_histograms.append(h_ff)

    return fake_factor_histograms
