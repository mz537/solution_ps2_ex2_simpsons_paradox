import numpy as np
import pandas as pd


def create_some_fake_cols(df: pd.DataFrame) -> pd.DataFrame:
    # create random 0 1 column to indicate gener
    df["gender"] = np.random.choice([0, 1], df.shape[0], p=[0.5, 0.5])
    df["gender"] = df["gender"].map({0: "female", 1: "male"})
    df["salary"] = np.random.randint(1000, 100000, df.shape[0])
    df.to_csv("data/smoking_data.csv")
    return df


if __name__ == "__main__":
    df = pd.read_csv("data/smoking.csv")
    df = create_some_fake_cols(df)
