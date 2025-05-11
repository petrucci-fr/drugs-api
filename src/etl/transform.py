import pandas as pd


def data_types_correction(df: pd.DataFrame) -> dict:
    """
    Corrects the data types of the columns in the dataframe.
    """
    df["price"] = (
        df["price"]
        .str.replace("$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

    return df


def pivot_drugs(df: pd.DataFrame) -> pd.DataFrame:
    """
    Converts a drug/presentation dataframe into a table-style dataframe
    where each column is a drug and rows are the corresponding form and dosage.
    """
    pivot = (
        df.groupby("drug")["form_and_dosage"]
        .apply(list)
        .to_dict()
    )

    # Make all presentation lists the same length (fill with empty strings)
    max_len = max(len(p) for p in pivot.values())
    padded = {
        drug: form_and_dosage + [""] * (max_len - len(form_and_dosage))
        for drug, form_and_dosage in pivot.items()
    }

    return pd.DataFrame(padded)
