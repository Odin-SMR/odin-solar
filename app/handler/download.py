import pandas as pd  # type: ignore
import s3fs  # type: ignore

from config import BUCKET, CUTOFF_DATE, FILENAME, URL


def download():
    df_new = pd.read_csv(URL)
    df_new.columns = df_new.columns.str.replace("F10.7_", "")
    df_new["DATE"] = pd.to_datetime(df_new["DATE"])
    df_new.set_index(["DATE"], inplace=True)
    df_new = df_new[
        (df_new.index > CUTOFF_DATE) & (df_new["DATA_TYPE"] == "OBS")
    ]
    s3 = s3fs.S3FileSystem()

    df_existing = pd.DataFrame()
    # Load existing data
    if s3.exists(f"{BUCKET}/{FILENAME}"):
        with s3.open(f"{BUCKET}/{FILENAME}", "rb") as f:
            df_existing = pd.read_parquet(f)

    # Append new data to existing data
    df_comb = df_existing._append(df_new)

    # Drop duplicates, keeping the version from the new data
    # if a row is duplicated
    df_comb = df_comb.drop_duplicates(keep="last")

    # Write back to S3
    with s3.open(f"{BUCKET}/{FILENAME}", "wb") as f:
        df_comb.to_parquet(f, engine="pyarrow")


if __name__ == "__main__":
    download()
