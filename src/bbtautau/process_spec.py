from dataclasses import dataclass, field
from order import Config, Channel, Process, UniqueObjectIndex
import tomllib
from typing import Any


@dataclass(kw_only=True)
class ProcessGroup:
    """
    Group of processes merged together in output plots.

    :attr processes: List of :py:class:`order.Process` objects forming
        the process group.

    :attr label: Label of the group in plots.

    :attr color: Color of the group in plots.

    :attr channels: List of channels, in which this process group is
        considered. If no value is passed, it is considered in all channels.
        (_optional_)
    """

    processes: list[Process]
    label: str
    color: str
    channels: list[str] | None = field(default=None)
    scale_factor: dict[str, float] | None = field(default=None)

    def __post_init__(self):
        # Convert list of processes into a unique object index
        if not isinstance(self.processes, UniqueObjectIndex):
            self.processes = UniqueObjectIndex(Process, self.processes)


class ProcessSpec:
    def __init__(
        self,
        process_spec_file: str,
        config: Config,
        channel: Channel,
    ):
        # Load analysis and configuration instance
        self._config_inst = config
        self._channel_inst = channel

        # Extract and sanitize data from the loaded TOML file
        raw_data = self._load(process_spec_file)
        self.metadata = self._init_metadata(raw_data)
        self.data = self._parse_process_groups(raw_data, "data")
        self.signals = self._parse_process_groups(raw_data, "signals")
        self.backgrounds = self._parse_process_groups(raw_data, "backgrounds")

    def get_all_process_groups(self):
        return self.data + self.signals + self.backgrounds

    def _init_metadata(self, raw_data: dict[str, Any]):
        return raw_data["metadata"].copy()

    def _parse_process_groups(
        self, raw_data: dict[str, Any], process_type: str
    ):
        # Return an empty dictionary if the data type has not been found
        if process_type not in raw_data:
            return []

        process_groups = []
        for process_spec in raw_data[process_type]:
            # If a 'channels' list is specified, check if the process is
            # considered in the current channel.
            channels = process_spec.get("channels", None)
            if channels is not None:
                if self._channel_inst.name not in channels:
                    continue

            # keyword arguments to construct the process group
            process_group_kwargs = {
                "processes": [],
                "label": process_spec.get("label", None),
                "color": process_spec.get("color", None),
                "scale_factor": process_spec.get("scale_factor", None),
            }

            # Convert the strings in 'processes' to `order.Process` objects
            for process in process_spec["processes"]:
                process_group_kwargs["processes"].append(
                    self._config_inst.get_process(process),
                )

            # Create the object and append it to the process group list
            process_groups.append(ProcessGroup(**process_group_kwargs))

        return process_groups

    @staticmethod
    def _load(
        process_spec_file: str,
    ) -> dict[str, Any]:
        with open(process_spec_file, mode="rb") as f:
            settings = tomllib.load(f)
        return settings
