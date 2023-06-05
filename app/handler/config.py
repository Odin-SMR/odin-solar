from datetime import datetime

URL = "http://celestrak.org/SpaceData/SW-All.csv"
BUCKET = "odin-solar"
FILENAME = "spacedata_observed.parquet"
CUTOFF_DATE = datetime(2001, 1, 1)
PROFILE = "odin-cdk"
