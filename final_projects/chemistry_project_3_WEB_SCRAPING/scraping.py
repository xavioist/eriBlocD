import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import requests


def get_thermo_info(material):
    """Carries out query from NIST Chemistry WebBook for thermodynamic properties of a chemical compound
    Args:
        material (str): Name of compound to get thermodynamic info for

    Returns:
        Pandas dataframe containing query results

    Raises:
        If table is not found, then dataframe is filled with NaNs.
    """
    # Replace commas with %2C for proper querying (this is the HEX code to represent a comma)
    mat_corr = (
        material.replace(",", "%2C")
        .replace("(", "%28")
        .replace(")", "%29")
        .replace("+", "%2B")
    )
    # Establish URL to be scraped (SI = SI units TG = Gas Phase Thermodynamics)
    url = f"https://webbook.nist.gov/cgi/cbook.cgi?Name={mat_corr}&Units=SI&cTG=on"
    # Request the URL and parse it as raw text
    raw_html = requests.get(url).text
    # Initiate Beautiful Soup to read the raw html data
    soup = BeautifulSoup(raw_html, "html.parser")
    # Initiate dataframe to contain query results
    df = pd.DataFrame(columns=["Quantity", "Value", "Units"])
    # Look for the table containing the thermodynamic data
    try:
        table = soup.find("table", attrs={"aria-label": "One dimensional data"})
    except:  # Table doesn't exist. Not all compounds have desired thermodynamic info.
        print("Except bloc executed. Table does not exist. Exiting.")
        df = df.append(
            {"Quantity": np.nan, "Value": np.nan, "Units": np.nan}, ignore_index=True
        )
        return 0
    # Get the rows present in the table

    rows = table.findAll("tr")

    # Get info for each row in table
    data = []
    for row in rows:
        cols = row.find_all("td")
        cols = [x.text.strip() for x in cols]
        if len(cols) > 0:
            data.append(cols)

    # Save the results into these variables and place them into the dataframe
    quantity = data[0][0]  # This is the value I want

    value = data[0][1].split("±", 1)[0].rstrip()  # Remove uncertainty in measurement

    units = data[0][2]  # These are the units. Usually in kj/mol

    df1 = pd.DataFrame(["Quantity", quantity])

    df2 = pd.DataFrame(["Value", value])

    df3 = pd.DataFrame(["Units", units])

    df = pd.concat([df1, df2, df3], axis=1, ignore_index=True)  # FALTA AQUESTA LINEA

    return df


material = "2,4,6-trinitrotoluene"
df = get_thermo_info(material)
print(df)

""" material = "2,4,6-trinitrotoluene"
    df = get_thermo_info(material)
    print(df)"""

"""if __name__ == "__main__":
    materials = ["2,4,6-trinitrotoluene", "methane", "ethane"]
    enthalp = {}
    for material in materials:
        df = get_thermo_info(material)
        enthalp[material] = df[1][1]
        # print(df)
    print(enthalp)"""
