import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_data(url: str) -> dict:
    """ Extracts data from the given URL and returns it as a dictionary."""

    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error: Unable to access the page. Status code: {response.status_code}")
        return {}    
    
    soup = BeautifulSoup(response.text, "html.parser")
    # print(soup.prettify())

    table = soup.find("table", class_="estandarc")

    product_name = table.find("span", class_="tproducto").text.strip()
    laboratory = table.find_all("span", class_="defecto")[0].text.strip()
    drug = table.find_all("span", class_="defecto")[1].text.strip()
    therapeutic_use = table.find_all("span", class_="defecto")[2].text.strip()
    
    dosage_form_table = table.find_all("table", class_="presentacion")

    records = []
    for dosage_form in dosage_form_table:
        dosage_tag = dosage_form.find("td", class_="tddesc")
        price_tag = dosage_form.find("td", class_="tdprecio")

        if dosage_tag and price_tag:
            dosage_form = dosage_tag.text.strip()
            price = price_tag.text.strip()

        records.append({
            "product": product_name,
            "manufacturer": laboratory,
            "drug": drug,
            "therapeutic_use": therapeutic_use,
            "form_and_dosage": dosage_form,
            "price": price
        })

    df = pd.DataFrame(records)

    return df
