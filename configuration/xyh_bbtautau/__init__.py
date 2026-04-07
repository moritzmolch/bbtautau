from order_util.patches import (
    patch_order_process,
    patch_order_variable,
    patch_order_channel,
)


# Apply patches to order classes
patch_order_process()
patch_order_variable()
patch_order_channel()

