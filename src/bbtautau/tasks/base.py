"""
Base tasks of the `bbtautau` workflow.
"""

from law import LocalDirectoryTarget, LocalFileTarget, Task
from luigi import Parameter
import os


class BaseTask(Task):
    """
    Base class of all `bbtautau` tasks.
    """

    tag = Parameter(
        default="DEFAULT",
        description=(
            "Tag to identify the version of the output files. Optional."
        ),
    )

    def task_parts(self):
        return ()

    def parts_before(self):
        return (
            self.task_family,
            self.tag,
        )

    def parts_after(self):
        return ()

    def local_path(self, *parts: str):
        return os.path.join(
            *self.parts_before(),
            *self.task_parts(),
            *self.parts_after(),
            *parts,
        )

    def local_target(self, *parts: str, **kwargs):
        is_dir = kwargs.pop("is_dir", False)
        target_cls = LocalDirectoryTarget if is_dir else LocalFileTarget
        return target_cls(self.local_path(*parts, **kwargs))

