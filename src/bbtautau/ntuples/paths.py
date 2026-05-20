import os


def get_ntuple_main_dir(
    ntuple_base_dir: str,
    ntuple_tag: str,
) -> str:
    """
    Get base output path of the main trees of a `NTuple` production for a
    `ntuple_tag`.

    The path `ntuple_base_dir` must end with `.../CROWN/ntuples` for `CROWN`
    outputs.

    :param ntuple_base_dir: Base output path of the `NTuple` production.

    :param ntuple_tag: Production tag of the `NTuple`.

    :returns: Path to `CROWNRun` directory with main trees.
    """
    return os.path.join(
        ntuple_base_dir,
        ntuple_tag,
        "CROWNRun",
    )


def get_ntuple_friend_dir(
    ntuple_base_dir: str,
    ntuple_tag: str,
    friend_name: str,
) -> str:
    """
    Get base output path of the friend trees of a `NTuple` production for a
    `ntuple_tag` and a `friend_name`.

    The path `ntuple_base_dir` must end with `.../CROWN/ntuples` for `CROWN`
    outputs.

    :param ntuple_base_dir: Base output path of the `NTuple` production.

    :param ntuple_tag: Production tag of the `NTuple`.

    :param friend_name: Name of the friend.

    :returns: Path to `CROWNFriends/<friend_name>` directory with main trees.
    """
    return os.path.join(
        ntuple_base_dir,
        ntuple_tag,
        "CROWNFriends",
        friend_name,
    )

