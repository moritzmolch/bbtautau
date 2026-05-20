"""
Mixins for tasks to load analysis metadata object from names provided as
task parameters.
"""

from functools import cached_property
from luigi import Parameter
from law import CSVParameter
from order import (
    Analysis,
    Campaign,
    Category,
    Channel,
    Config,
    Variable,
    UniqueObjectIndex,
)

from bbtautau.util import load_object


class AnalysisMixin():

    analysis = Parameter(
        description="Python module path to analysis metadata object.",
    )

    @cached_property
    def analysis_inst(self) -> Analysis:
        return load_object(self.analysis)


class CampaignMixin(AnalysisMixin):

    campaign = Parameter(
        description="Name of the data-taking campaign.",
    )

    @cached_property
    def config_inst(self) -> Config:
        return self.analysis_inst.get_config(self.campaign)

    @cached_property
    def campaign_inst(self) -> Campaign:
        return self.config_inst.campaign


class ChannelMixin(CampaignMixin):

    channel = Parameter(
        description="Name of the analysis channel.",
    )

    @cached_property
    def channel_inst(self) -> Channel:
        return self.config_inst.get_channel(self.channel)


class CategoryMixin(CampaignMixin):

    category = Parameter(
        description="Name of the analysis category.",
    )

    @cached_property
    def category_inst(self) -> Category:
        return self.config_inst.get_category(self.category)

    @cached_property
    def channel_inst(self) -> Channel:
        return self.category_inst.channel


class VariablesMixin(CategoryMixin):

    variables = CSVParameter(
        description="Comma-seperated list of variable names.",
    )

    @cached_property
    def variable_insts(self) -> UniqueObjectIndex:
        return UniqueObjectIndex(
            Variable,
            [self.channel_inst.get_variable(v) for v in self.variables]
        )

