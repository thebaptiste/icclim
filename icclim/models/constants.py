from __future__ import annotations

# fmt: off
# flake8: noqa

ICCLIM_VERSION = "5.4.0"

# placeholders for user_index
PERCENTILE_THRESHOLD_STAMP = "p"
WET_DAY_THRESHOLD = 1  # 1mm
PRECIPITATION = "p"
TEMPERATURE = "t"

# percentiles dimension from percentile_doy
PERCENTILES_COORD = "percentiles"
# attribut holding the in_base time bounds
IN_BASE_IDENTIFIER = "reference_epoch"
# coordinate of day of year values (usually from 1 to 365/366)
DOY_COORDINATE = "dayofyear"
# Units attribute key for DataArray(s)
UNITS_ATTRIBUTE_KEY =  "units"


# Aliases of input percentiles variables names
# Source icclim dev
VALID_PERCENTILE_DIMENSION = ["quantile", "percentile", "per", "centile"]

# Source of ECA&D indices definition
ECAD_ATBD = "ECA&D, Algorithm Theoretical Basis Document (ATBD) v11"

# Index qualifiers (needed to generate the API)
QUANTILE_BASED = "QUANTILE_BASED"  # fields: QUANTILE_INDEX_FIELDS
MODIFIABLE_UNIT = "MODIFIABLE_UNIT"  # fields: out_unit

# Map of months index to their short name, used to get a pandas frequency anchor
MONTHS_MAP = {1:"JAN",  2:"FEB", 3:"MAR", 4:"APR", 5:"MAY", 6:"JUN", 7:"JUL", 8:"AUG", 9:"SEP", 10:"OCT", 11:"NOV", 12:"DEC" }

# Season defined by their month numbers
AMJJAS_MONTHS:list[int] = [*range(4, 9)]
ONDJFM_MONTHS:list[int] = [10, 11, 12, 1, 2, 3]
DJF_MONTHS:list[int] = [12, 1, 2]
MAM_MONTHS:list[int] = [*range(3, 6)]
JJA_MONTHS:list[int] = [*range(6, 9)]
SON_MONTHS:list[int] = [*range(9, 12)]

# pseudo units used with Threshold class (not in Pint)
PERIOD_PERCENTILE_UNIT = "period_per"
DOY_PERCENTILE_UNIT = "doy_per"

# Mapping of frequencies to generate metadata
# copied from xclim and updated.
# todo: it's weird to group in the same dictionary things that have different purposes.
EN_FREQ_MAPPING = {
    "YS": "year(s)", "Y": "year(s)", "AS": "year(s)", "A": "year(s)",
    "QS": "season(s)", "Q": "season(s)",
    "MS": "month(s)", "M": "month(s)",
    "W": "week(s)",
    "D": "day(s)",
    "H": "hour(s)",
    "JAN": "January starting", "FEB": "February starting", "MAR": "March starting", "APR": "April starting", "MAY": "May starting", "JUN": "June starting", "JUL": "July starting", "AUG": "August starting", "SEP": "September starting", "OCT": "October starting", "NOV": "November starting", "DEC": "December starting",
    # Arguments to "indexer"
    "DJF": "wintry", "MAM": "springlong", "JJA": "summery", "SON": "autumnal",
    "norm": "Normal",
    "m1": "january",  "m2": "february",  "m3": "march",  "m4": "april",  "m5": "may",  "m6": "june",  "m7": "july",  "m8": "august",  "m9": "september",  "m10": "october",  "m11": "november",  "m12": "december",
    "MON": "monday starting", "TUE": "tuesday starting", "WED": "wednesday starting", "THU": "thursday starting", "FRI": "friday starting", "SAT": "saturday starting", "SUN": "sunday starting"
}

# Special CF unit
PART_OF_A_WHOLE_UNIT = "1"
