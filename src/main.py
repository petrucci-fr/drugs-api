import pandas as pd

from etl.extract import extract_data
from etl.transform import data_types_correction, pivot_drugs
from etl.load import load_data_to_gspread
from settings import BASE_URL, DRUGS_NAMES, COLUMNS_NAMES 


def main():
    drugs_df = pd.DataFrame(columns=COLUMNS_NAMES)

    for drug in DRUGS_NAMES:
        url = f"{BASE_URL}{drug}.html"
        data = extract_data(url)
        drugs_df = pd.concat([drugs_df, pd.DataFrame(data)], ignore_index=True)

    drugs_df = data_types_correction(drugs_df)

    print(drugs_df)

    load_data_to_gspread(drugs_df)

    transposed_df = pivot_drugs(drugs_df)
    load_data_to_gspread(transposed_df, sheet_name="Dropdowns")


if __name__ == "__main__":
    main()
