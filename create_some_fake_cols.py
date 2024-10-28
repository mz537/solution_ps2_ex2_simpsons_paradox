# This script is to make the data from calmcode.io on smoking a bit
# more interesting
# by adding some fake columns to it and some null values.
# All are random and not based on any real data. So it should
# not affect the analysis.

import numpy as np
import pandas as pd


def create_some_fake_cols(df: pd.DataFrame) -> pd.DataFrame:
    # create random 0 1 column to indicate gender; 50-50 split
    df["gender"] = np.random.choice([0, 1], df.shape[0], p=[0.5, 0.5])
    df["gender"] = df["gender"].map({0: "female", 1: "male"})
    df["salary"] = np.random.randint(1000, 100000, df.shape[0])
    # random missings in salary column
    df.loc[np.random.choice(df.index, 1000), "salary"] = np.nan
    df.to_csv("data/smoking_data.csv")
    return df


if __name__ == "__main__":
    df = pd.read_csv("data/smoking.csv")
    df = create_some_fake_cols(df)
    print("Done making the data a bit more difficult to work with.")
