from collections import OrderedDict
from itertools import chain
import ROOT
import ntuple_processor
from ntuple_processor import dataset_from_crownoutput, Histogram, Unit
from ntuple_processor.utils import Selection
from order import (
    Analysis,
    Campaign,
    Config,
    Channel,
    Category,
    Dataset,
    Process,
    Shift,
    UniqueObjectIndex,
)
from shapes.utils import filter_friends
from typing import Callable

from bbtautau.process_spec import ProcessSpec
from bbtautau.ntuples import get_ntuple_friend_dir, get_ntuple_main_dir


class AnalysisContext:
    """
    A class to hold all relevant information about the analysis context,
    which is used to configure the ntuple processor selection.
    """

    def __init__(
        self,
        *,
        analysis: Analysis | None = None,
        config: Config | None = None,
        campaign: Campaign | None = None,
        channel: Channel | None = None,
        category: Category | None = None,
        process: Process | None = None,
        dataset: Dataset | None = None,
        shift: Shift | None = None,
    ):
        self.analysis = analysis
        self.config = config
        self.campaign = campaign
        self.channel = channel
        self.category = category
        self.process = process
        self.dataset = dataset
        self.shift = shift


def create_ntuple_processor_dataset(
    ntuple_main_dir: str,
    ntuple_friend_dirs: dict[str, str],
    shapes_tag: str,
    campaign: Campaign,
    channel: Channel,
    dataset: Dataset,
) -> ntuple_processor.utils.Dataset:
    """
    Use information from the :py:class:`order.Dataset` object to construct the
    corresponding :py:class:`ntuple_processor.utils.Dataset` object for the
    :py:module:`ntuple_processor` module.
    """
    # Get nicks of all samples in the dataset 
    dataset_nicks = [
        nick
        for nick in dataset.x.nicks
    ]

    # Construct the ntuple processor dataset
    np_dataset = dataset_from_crownoutput(
        dataset.name,
        dataset_nicks,
        campaign.name,
        channel.name,
        f"{channel}_nominal",
        ntuple_main_dir,
        [
            friend_dir
            for friend_name, friend_dir in ntuple_friend_dirs.items()
            if filter_friends(dataset.name, friend_name)
        ],
        validation_tag=shapes_tag,
        validate_samples=False,
        xrootd=ntuple_main_dir.startswith("root://"),
    )

    return np_dataset


def create_ntuple_processor_datasets(
    campaign: Campaign,
    channel: Channel,
    process_spec: ProcessSpec,
    ntuple_base_dir: str,
    ntuple_tag: str,
    shapes_tag: str,
    friend_names: list[str] | None = None,
) -> dict[str, ntuple_processor.utils.Dataset]:
    # If the friend_names argument is not provided, turn the object into an
    # empty list
    friend_names = friend_names if friend_names is not None else []

    # Get the ntuple directories for the main and friend trees
    main_dir = get_ntuple_main_dir(ntuple_base_dir, ntuple_tag)
    friend_dirs = {
        friend_name: get_ntuple_friend_dir(
            ntuple_base_dir,
            ntuple_tag,
            friend_name,
        )
        for friend_name in friend_names
    }

    # Store for the ntuple processor datasets in a dictionary mapping the
    # dataset name to the `ntuple_processor.utils.Dataset` object

    np_datasets = {}
    for dataset in chain.from_iterable(
        (
            p.datasets.values()
            for g in process_spec.get_all_process_groups()
            for p in g.processes.values()
        )
    ):
        if dataset.name in np_datasets:
            continue
        np_datasets[dataset.name] = create_ntuple_processor_dataset(
            main_dir,
            friend_dirs,
            shapes_tag,
            campaign,
            channel,
            dataset,
        )

    return np_datasets


def create_ntuple_processor_selection(
    selection_func: Callable[[AnalysisContext], list[Selection]],
    config: Config,
    analysis: Analysis,
    campaign: Campaign,
    channel: Channel,
    category: Category,
    process: Process,
    dataset: Dataset,
):
    """
    Use information from the :py:class:`order.Dataset` object to construct the
    corresponding :py:class:`ntuple_processor.utils.Dataset` object for the
    :py:module:`ntuple_processor` module.
    """

    # Create the analysis context
    analysis_context = AnalysisContext(
        analysis=analysis,
        config=config,
        campaign=campaign,
        channel=channel,
        category=category,
        process=process,
        dataset=dataset,
    )

    # Get dictionaries with selections and weights for the given analysis
    # context
    selections = selection_func(analysis_context)

    return selections


def create_ntuple_processor_unit(
    selection_func: Callable[[AnalysisContext], OrderedDict[str, str]],
    np_datasets: dict[str, ntuple_processor.utils.Dataset],
    analysis: Analysis,
    config: Config,
    campaign: Campaign,
    channel: Channel,
    category: Category,
    process: Process,
    dataset: Dataset,
    variables: UniqueObjectIndex,
    shifts: UniqueObjectIndex | None = None,
):
    # Create the ntuple processor selection object from the selection and
    # weight functions
    # TODO Add systematic variations
    np_selection = create_ntuple_processor_selection(
        selection_func,
        analysis,
        config,
        campaign,
        channel,
        category,
        process,
        dataset,
    )

    # Get the ntuple processor dataset for the current dataset
    np_dataset = np_datasets[dataset.name]

    # Create the histogram objects from the variable objects
    histograms = [
        Histogram(
            variable.name,
            variable.name,
            variable.binning,
        )
        for variable in variables.values()
    ]

    # Create the analysis unit for the ntuple processor
    unit = Unit(
        dataset=np_dataset,
        selections=np_selection,
        actions=histograms,
    )

    return unit


def create_ntuple_processor_units(
    process_spec: ProcessSpec,
    selection_func: Callable[[AnalysisContext], OrderedDict[str, str]],
    np_datasets: dict[str, ntuple_processor.utils.Dataset],
    analysis: Analysis,
    config: Config,
    campaign: Campaign,
    channel: Channel,
    category: Category,
    variables: UniqueObjectIndex,
    shifts: UniqueObjectIndex | None = None,
):
    units = [
        create_ntuple_processor_unit(
            selection_func,
            np_datasets,
            analysis,
            config,
            campaign,
            channel,
            category,
            process,
            dataset,
            variables,
            shifts=shifts,
        )
        for process in chain.from_iterable(
            (
                g.processes.values()
                for g in process_spec.get_all_process_groups()
            )
        )
        for dataset in process.datasets.values()
    ]

    return units


def has_all_shapes(
    shapes_file: str,
    process_spec,
    campaign,
    category,
    variables,
    shifts=None,
):
    f = ROOT.TFile.Open(shapes_file, "READ")
    keys = [k.GetTitle() for k in f.GetListOfKeys()]
    all_exist = all(
        [
            (
                dataset.name
                + f"#{category.name}-{process.name}-{dataset.name}"
                + "#Nominal"
                + f"#{variable.name}"
            ) in keys
            for process in chain.from_iterable(
                (
                    g.processes.values()
                    for g in process_spec.get_all_process_groups()
                )
            )
            for dataset in process.datasets.values()
            for variable in variables.values()
        ]
    )
    f.Close()
    return all_exist

