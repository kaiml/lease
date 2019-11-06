import requests
import pandas as pd
import json


def get_code(address):
    response = requests.get("http://zipcoda.net/api", params={"address": address})
    response_dict = json.loads(response.text)
    zipcode = response_dict["items"][0]["zipcode"]
    return zipcode


def fe_postal(df, verbose=False):
    address = df["address"]
    postal_code = pd.Series([])
    for i, a in enumerate(address):
        if i % 100 == 0 and verbose:
            print(i)
            print(postal_code)
        postal_code = postal_code.append(pd.Series(get_code(a)), ignore_index=True)
    #     df.loc[:, "postal_code"] = postal_code
    return postal_code
