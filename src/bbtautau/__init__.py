import warnings


# Supress warnings on use of distributed RDFs (not used in this package)
warnings.filterwarnings(
    "ignore",
    category=FutureWarning,
    module="DistRDF"
)

