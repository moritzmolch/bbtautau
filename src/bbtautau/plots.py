import ROOT
import re
from bbtautau.plot_util import plot as plotutil_plot
from configuration.xyh_bbtautau.metadata.analysis import analysis
from bbtautau.process_spec import ProcessSpec
import matplotlib.pyplot as plt

ROOT.TH1.AddDirectory(False)


def add_th1(th1_list):
    hist_base = th1_list[0]
    if len(th1_list) > 1:
        for hist_add in th1_list[1:]:
            hist_base.Add(hist_add)
    return hist_base


def load_histograms(histogram_file: str):
    histograms = []
    rf = ROOT.TFile.Open(histogram_file, "READ")
    for key in rf.GetListOfKeys():
        key = key.GetTitle()
        match = re.match(r"^([^#]*)#([^#]*)-([^#]*)-([^#]*)#([^#]*)#([^#]*)", key)
        if not match:
            raise Exception()
        dataset = match.group(1)
        category = match.group(2)
        process = match.group(3)
        dataset = match.group(4)
        shift = match.group(5)
        variable = match.group(6)
        histograms.append({
            "key": key,
            "dataset": dataset,
            "category": category,
            "process": process,
            "shift": shift,
            "variable": variable,
            "histogram": rf.Get(key),
        })
    return histograms


def prepare_histograms(
    process_spec,
    histograms,
    category,
    variables,
):
    prepared_histograms = {}
    for variable in variables:
        prepared_histograms[variable.name] = {}
        for process_type, process_groups in [
            ("data", process_spec.data),
            ("signals", process_spec.signals),
            ("backgrounds", process_spec.backgrounds),
        ]:
            prepared_histograms[variable.name][process_type] = []
            for process_group in process_groups:
                # Prepare plotting keyword arguments
                plot_kwargs = {
                    "color": process_group.color,
                    "label": process_group.label,
                }
                if process_type == "signals" and process_group.scale_factor is not None:
                    plot_kwargs["scale_factor"] = process_group.scale_factor[category.channel.name]

                # Sum up all histogram of a process group
                histogram = add_th1([
                    h["histogram"]
                    for h in histograms
                    for process in process_group.processes
                    if (
                        h["category"] == category.name
                        and h["process"] == process.name
                        and h["variable"] == variable.name
                    )
                ])

                # Add information to the full histograms dictionary
                prepared_histograms[variable.name][process_type].append((histogram, plot_kwargs))

    return prepared_histograms


def plot(
    histograms,
    campaign,
    category,
    variable,
):

    fig, ax = plotutil_plot(
        histograms[variable.name]["data"][0],
        histograms[variable.name]["backgrounds"],
        hist_signals=histograms[variable.name]["signals"],
        stack_kwargs=None,
        x_label_top=None,
        y_label_top="Events",
        x_label_bottom=variable.get_full_x_title(),
        y_label_bottom=r"$\dfrac{Data}{Background}$",
        y_limits_top=None,
        y_limits_bottom=(0.5, 1.5),
        category_label=category.label,
        lumi=campaign.x.lumi,
        era=None,
        sqrt_s=campaign.ecm,
        fit_ratio=False,
    )

    return fig, ax

