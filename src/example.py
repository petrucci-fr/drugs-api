import pandas as pd
from etl.transform import data_types_correction

data = {
    "product": [
        "SAXENDA", "VINTIX", "VINTIX", "VINTIX", "VINTIX", "VINTIX",
        "TRAPAX", "TRAPAX", "TRAPAX", "TRAPAX", "TRAPAX", "TRAPAX",
        "NOVO INSOMNIUM", "NOVO INSOMNIUM"
    ],
    "manufacturer": [
        "Novo Nordisk", "Roemmers", "Roemmers", "Roemmers", "Roemmers", "Roemmers",
        "Pfizer", "Pfizer", "Pfizer", "Pfizer", "Pfizer", "Pfizer",
        "Gador", "Gador"
    ],
    "drug": [
        "liraglutida", "vilazodona clorh.", "vilazodona clorh.", "vilazodona clorh.",
        "vilazodona clorh.", "vilazodona clorh.", "lorazepam", "lorazepam",
        "lorazepam", "lorazepam", "lorazepam", "lorazepam", "eszopiclona", "eszopiclona"
    ],
    "therapeutic_use": [
        "Trat.de la obesidad", "Antidepresivo", "Antidepresivo", "Antidepresivo",
        "Antidepresivo", "Antidepresivo", "Ansiolítico", "Ansiolítico", "Ansiolítico",
        "Ansiolítico", "Ansiolítico", "Ansiolítico", "Hipnótico", "Hipnótico"
    ],
    "form_and_dosage": [
        "lap.prell.x 3", "10 mg comp.x 30", "20 mg comp.x 15", "20 mg comp.x 30",
        "40 mg comp.x 15", "40 mg comp.x 30", "1 mg comp.x 30", "1 mg comp.x 50",
        "1 mg comp.x 60", "2.5 mg comp.x 30", "2.5 mg comp.x 50", "2.5 mg comp.x 60",
        "2 mg comp.x 30", "3 mg comp.x 30"
    ],
    "price": [
        "$504.909,20", "$23.749,01", "$18.842,56", "$42.724,79",
        "$24.735,85", "$53.973,84", "$5.899,36", "$10.214,77",
        "$11.397,16", "$8.284,01", "$13.941,73", "$17.046,98",
        "$14.585,12", "$18.875,98"
    ]
}

df = pd.DataFrame(data)

df = data_types_correction(df)
print(df)