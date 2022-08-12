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
# threshold dimension, either percentiles or simple per grid cell scalars
THRESHOLD_COORDINATE = "threshold"
# Units attribute key for DataArray(s)
UNITS_ATTRIBUTE_KEY =  "units"

# Aliases of input variables names.
# Source: clix-meta (modified)
PR = ["pr", "prAdjust","prAdjust", "prec", "rr", "precip", "PREC", "Prec", "RR", "PRECIP", "Precip"]
TAS = ["tas", "tavg", "ta", "tasAdjust","tasAdjust", "tmean", "tm", "tg", "meant", "TMEAN", "Tmean", "TM", "TG", "MEANT", "meanT", "tasmidpoint"]
TAS_MAX = ["tasmax", "tasmaxAdjust","tasmaxAdjust", "tmax", "tx", "maxt", "TMAX", "Tmax", "TX", "MAXT", "maxT"]
TAS_MIN = ["tasmin", "tasminAdjust","tasminAdjust", "tmin", "tn", "mint", "TMIN", "Tmin", "TN", "MINT", "minT"]
HURS = ["hurs", "hursAdjust", "rh", "RH"]
PSL = ["psl", "mslp", "slp", "pp", "MSLP", "SLP", "PP"]
SND = ["snd", "sd", "SD"]
SUND = ["sund", "ss", "SS"]
WSGS_MAX = ["wsgsmax", "fx", "FX"]
SFC_WIND = ["sfcWind", "sfcwind", "fg", "FG"]
SNW = ["snw", "swe", "SW"]


# Aliases of input percentiles variables names
# Source icclim dev
VALID_PERCENTILE_DIMENSION = ["quantile", "percentile", "per", "centile"]

# Source of ECA&D indices definition
ECAD_ATBD = "ECA&D, Algorithm Theoretical Basis Document (ATBD) v11"

# Index qualifiers (needed to generate the API)
QUANTILE_BASED = "QUANTILE_BASED"  # fields: QUANTILE_INDEX_FIELDS
MODIFIABLE_UNIT = "MODIFIABLE_UNIT"  # fields: out_unit
MODIFIABLE_THRESHOLD = "MODIFIABLE_THRESHOLD"  # fields: threshold
MODIFIABLE_QUANTILE_WINDOW = "MODIFIABLE_QUANTILE_WINDOW"  # fields: window_width

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
FREQ_MAPPING = {
    "YS": "annual", "Y": "annual", "AS": "annual", "A": "annual",
    "MS": "monthly", "M": "monthly",
    "QS": "seasonal", "Q": "seasonal",
    "D": "daily",
    "H": "hourly",
    "JAN": "January starting", "FEB": "February starting", "MAR": "March starting", "APR": "April starting", "MAY": "May starting", "JUN": "June starting", "JUL": "July starting", "AUG": "August starting", "SEP": "September starting", "OCT": "October starting", "NOV": "November starting", "DEC": "December starting",
    # Arguments to "indexer"
    "DJF": "wintry", "MAM": "springlong", "JJA": "summery", "SON": "autumnal",
    "norm": "Normal",
    "m1": "january",  "m2": "february",  "m3": "march",  "m4": "april",  "m5": "may",  "m6": "june",  "m7": "july",  "m8": "august",  "m9": "september",  "m10": "october",  "m11": "november",  "m12": "december",
}

# Special CF unit
PART_OF_A_WHOLE_UNIT = "1"
