from functools import cache


@cache
def patch_order_process():
    """
    Extend the :py:class:`order.Process` class with a :py:attr:`datasets`
    attribute that holds the index of associated :py:class:`order.Dataset`
    instances.

    The :py:func:`order.unique_tree` function is used to attach the dataset
    index to the process class, which also adds convenience methods to access
    the index.
    """

    import order
    from order import CopyMixin, Dataset, UniqueObjectIndex, unique_tree

    # Get the original process class
    process_cls_orig = order.Process
    process_cls_copy_specs_orig = order.Process.copy_specs
    process_cls_init_orig = order.Process.__init__

    # Add datasets copy specs
    copy_specs = [
        {
            "attr": "_datasets",
            "skip_shallow": True,
            "skip_value": CopyMixin.Deferred(
                lambda inst: UniqueObjectIndex(cls=Dataset),
            ),
        }
    ] + process_cls_copy_specs_orig

    # Add the datasets parameter to the constructor of the process class
    def init(self, *args, **kwargs):
        # Get the datasets parameter
        datasets = kwargs.pop("datasets", None)

        # Perform original initialization
        process_cls_init_orig(self, *args, **kwargs)

        # Extend the list of datasets of this process instance
        if datasets is not None:
            self.extend_datasets(datasets)

    # Patch the copy_specs attribute and constructor
    process_cls_orig.copy_specs = copy_specs
    process_cls_orig.__init__ = init

    # Attach tree of dataset objects to the process
    process_cls = unique_tree(
        cls=Dataset,
        deep_children=False,
        deep_parents=False,
        parents=False,
    )(process_cls_orig)

    # Store the patched process class back to order module
    order.Process = process_cls


@cache
def patch_order_variable():
    """
    Extend the :py:class:`order.Variable` class with a :py:attr:`channels`
    attribute that holds the index of associated analysis
    :py:class:`order.Channel` instances.

    The :py:func:`order.unique_tree` function is used to attach the channel
    index to the variable class, which also adds convenience methods to access
    the index.
    """

    import order
    from order import Channel, CopyMixin, UniqueObjectIndex, unique_tree

    # Get the original variable class
    variable_cls_orig = order.Variable
    variable_cls_copy_specs_orig = order.Variable.copy_specs
    variable_cls_init_orig = order.Variable.__init__

    # Add datasets copy specs
    copy_specs = [
        {
            "attr": "_channels",
            "skip_shallow": True,
            "skip_value": CopyMixin.Deferred(
                lambda inst: UniqueObjectIndex(cls=Channel),
            ),
        }
    ] + variable_cls_copy_specs_orig

    # Add the channels parameter to the constructor of the variable class
    def init(self, *args, **kwargs):
        # Get the channels parameter
        channels = kwargs.pop("channels", None)

        # Perform original initialization
        variable_cls_init_orig(self, *args, **kwargs)

        # Extend the list of channels of this variable instance
        if channels is not None:
            self.extend_channels(channels)

    # Patch the copy_specs attribute and constructor
    variable_cls_orig.copy_specs = copy_specs
    variable_cls_orig.__init__ = init

    # Attach tree of channel objects to the process
    variable_cls = unique_tree(
        cls=Channel,
        deep_children=False,
        deep_parents=False,
        parents=False,
    )(variable_cls_orig)

    # Store the patched variable class back to order module
    order.Variable = variable_cls


@cache
def patch_order_channel():
    """
    Extend the :py:class:`order.Channel` class with a :py:attr:`variables`
    attribute that holds the index of associated :py:class:`order.Variable`
    instances.

    The :py:func:`order.unique_tree` function is used to attach the variable
    index to the process class, which also adds convenience methods to access
    the index.
    """

    import order
    from order import CopyMixin, UniqueObjectIndex, unique_tree

    # Get the original variable class
    channel_cls_orig = order.Channel
    channel_cls_copy_specs_orig = order.Channel.copy_specs
    channel_cls_init_orig = order.Channel.__init__

    # Add datasets copy specs
    copy_specs = [
        {
            "attr": "_variables",
            "skip_shallow": True,
            "skip_value": CopyMixin.Deferred(
                lambda inst: UniqueObjectIndex(cls=order.Variable),
            ),
        }
    ] + channel_cls_copy_specs_orig

    # Add the variables parameter to the constructor of the channel class
    def init(self, *args, **kwargs):
        # Get the variables parameter
        variables = kwargs.pop("variables", None)

        # Perform original initialization
        channel_cls_init_orig(self, *args, **kwargs)

        # Extend the list of variables of this process instance
        if variables is not None:
            self.extend_variables(variables)

    # Patch the copy_specs attribute and constructor
    channel_cls_orig.copy_specs = copy_specs
    channel_cls_orig.__init__ = init

    # Attach tree of variable objects to the channel
    channel_cls = unique_tree(
        cls=order.Variable,
        deep_children=False,
        deep_parents=False,
        parents=False,
    )(channel_cls_orig)

    # Store the patched channel class back to order module
    order.Channel = channel_cls

