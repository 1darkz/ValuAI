import pandas as pd

def load_raw_data(path: str) -> pd.DataFrame:
    return pd.read_csv(.../data/raw/boston.csv)


def handle_outliers(df: pd.DataFrame) -> pd.DataFrame:
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    print(IQR)

    cols_to_filter = df.columns[df.columns != 'CHAS']

    Q1 = df[cols_to_filter].quantile(0.25)
    Q3 = df[cols_to_filter].quantile(0.75)
    IQR = Q3 - Q1

    df = df[~((df[cols_to_filter] < (Q1 - 1.5 * IQR)) | (df[cols_to_filter] > (Q3 + 1.5 * IQR))).any(axis=1)]
    return df

def detecting_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    return df.isnull().sum()

def save_processed(df: pd.DataFrame):
    df.to_csv(.../data/processed/boston.csv, index=False)