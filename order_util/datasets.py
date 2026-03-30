from functools import cache
import json
from order import Config, Dataset
from pathlib import Path
from typing import Any


@cache
def get_sample_database(
    sample_database_dir: Path,
    nano_version: str,
) -> dict[str, dict[str, Any]]:
    """
    Load the sample database for a given NANOAOD version.

    The sample database for a given `nano_version` is loaded once. When
    loaded, a cached version of the database is returned by this function.

    :param sample_database_dir: Path to the sample database.

    :param nano_version: NANOAOD version of the target database.

    :returns: A dictionary with the sample nicks as keys and related
        information as value, also structured as a dictionary.
    """

    # Load the content of the sample database
    database_file = sample_database_dir.joinpath(
        f"nanoAOD_{nano_version}",
        "datasets.json",
    )
    with open(database_file, "r") as f:
        sample_database = json.load(f)

    return sample_database


def create_dataset_from_sample_database(
    name: str,
    nicks: str | list[str],
    sample_database_dir: str,
    nano_version: str,
) -> Dataset:
    """
    Create a :py:class:`~order.Dataset` object from sample database
    information.

    The dataset information is loaded based on the `nicks`, which are looked up
    in the sample database. The dictionary must contain campaign names, stored
    in the `campaigns` list, as keys, and corresponding nicks as values. The
    nicks can be provided as a string or, if the dataset consists of multiple
    partial samples, as a list of strings, e.g.:

    ```python
    {
        "2022preEE": [
            "DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            "DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X_ext1",
        ],
        ...
    }

    :param name: Name of the dataset.

    :param nicks: Either a single nick or a dictionary that maps each 
        campaign name to a specific nick.

    :param sample_database_dir: Path to the sample database.

    :param nano_version: NANOAOD version of the target database.

    :returns: The created :py:class:`~order.Dataset` object.
    """

    # Get the sample database object
    sample_database = get_sample_database(sample_database_dir, nano_version)

    # Convert nicks to a list if it is a string
    if isinstance(nicks, str):
        nicks = [nicks]

    # Skeleton for the dataset information to be stored in the dataset object
    dataset_info = {
        "name": name,
        "id": "+",
        "keys": [],
        "n_events": 0,
        "n_files": 0,
        "is_data": set(),
        "aux": {
            "nicks": nicks,
            "instance": set(),
            "sample_type": set(),
            "xsec": set(),
            "generator_weight": set(),
        },
    }

    for nick in nicks:
        # Load dataset information from the sample database
        if nick not in sample_database:
            raise ValueError(f"Nick '{nick}' not found in sample database.")

        # Get the entry
        db_entry = sample_database[nick]

        # Add the DBS key and instance information
        dataset_info["keys"].append(db_entry["dbs"])
        dataset_info["aux"]["instance"].add(db_entry["instance"])

        # Sum number of events and files of this nick
        dataset_info["n_events"] += db_entry["nevents"]
        dataset_info["n_files"] += db_entry["nfiles"]

        # Add the sample type information
        dataset_info["aux"]["sample_type"].add(db_entry["sample_type"])

        # Add cross section and generator weight info
        dataset_info["aux"]["xsec"].add(db_entry["xsec"])
        dataset_info["aux"]["generator_weight"].add(
            db_entry["generator_weight"]
        )

        # Add is_data flag
        # - For samples of type `data`, set the flag to `True`.
        # - For samples of type `embedding`, set the flag to `None`.
        # - For all other samples, set the flag to `False` (corresponds to MC).
        dataset_info["is_data"].add(
            (db_entry["sample_type"] == "data")
            if not db_entry["sample_type"] == "embedding"
            else None
        )

    # Check if all nicks have the same value for is_data and instance
    if len(dataset_info["is_data"]) != 1:
        raise ValueError(
            "All parts of the dataset must have the same value for is_data, found "
            f"{dataset_info['is_data']}."
        )
    if len(dataset_info["aux"]["instance"]) != 1:
        raise ValueError(
            "All parts of the dataset must have the same value for aux.instance, found "
            f"{dataset_info['aux']['instance']}."
        )
    if len(dataset_info["aux"]["sample_type"]) != 1:
        raise ValueError(
            "All parts of the dataset must have the same value for aux.sample_type, found "
            f"{dataset_info['aux']['sample_type']}."
        )

    # Calculate cross sections and generator weights as mean values of
    # considered samples
    if not any(x is None for x in dataset_info["aux"]["xsec"]):
        dataset_info["aux"]["xsec"] = sum(dataset_info["aux"]["xsec"]) / len(
            dataset_info["aux"]["xsec"]
        )
    else:
        dataset_info["aux"]["xsec"] = None
    if not any(x is None for x in dataset_info["aux"]["generator_weight"]):
        dataset_info["aux"]["generator_weight"] = sum(
            dataset_info["aux"]["generator_weight"]
        ) / len(dataset_info["aux"]["generator_weight"])
    else:
        dataset_info["aux"]["generator_weight"] = None

    # If checks have been passed, set is_data, instance and sample_type to single values
    dataset_info["is_data"] = dataset_info["is_data"].pop()
    dataset_info["aux"]["instance"] = dataset_info["aux"]["instance"].pop()
    dataset_info["aux"]["sample_type"] = dataset_info["aux"][
        "sample_type"
    ].pop()

    # Create the new dataset object
    dataset = Dataset(**dataset_info)

    return dataset


def add_dataset_from_sample_database(
    config: Config,
    name: str,
    nicks: dict[str, str | list[str]],
):
    """
    Add dataset to :py:class:`~order.Config` instances using information from
    the sample database.

    The dataset information is loaded based on the `nicks`, which are looked up
    in the sample database. The dictionary must contain campaign names, stored
    in the `campaigns` list, as keys, and corresponding nicks as values. The
    nicks can be provided as a string or, if the dataset consists of multiple
    partial samples, as a list of strings, e.g.:

    ```python
    {
        "2022preEE": [
            "DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X",
            "DYto2L-2Jets_MLL-50_TuneCP5_13p6TeV_amcatnloFXFX-pythia8_Run3Summer22NanoAODv12-130X_ext1",
        ],
        ...
    }
    ```

    :param config_inst: The :py:class:`~order.Config` that the datasets are
        added to.

    :param name: name of the dataset.

    :param nicks: Either a single nick or a dictionary that maps each 
        campaign name to a specific nick.

    :param sample_database_dir: Path to the sample database.
    """

    # Get the campaign's name, sample database directory, and NANOAOD version
    # to access the correct and to extract the correct nicks from the dictionary
    campaign_name = config.campaign.name
    sample_database_dir = config.x.sample_database_dir
    nano_version = config.campaign.x.nano_version

    # Add the dataset object to the config
    if campaign_name in nicks and len(nicks[campaign_name]) > 0:
        config.add_dataset(
            create_dataset_from_sample_database(
                name,
                nicks[campaign_name],
                sample_database_dir,
                nano_version,
            )
        )

