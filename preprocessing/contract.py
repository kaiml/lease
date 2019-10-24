# contract : to contract, periodic
def pp_contract(df):
    contract = df["contract"].str.replace("※この物件は\t定期借家\tです。", "").str.replace("\t", "")
    contract[contract.str.contains("まで").fillna(True)] = "2年間"
    year = contract.str.extract(r"(\d)年間").fillna(0).astype(int)
    month = contract.str.extract(r"(\d)ヶ月間").fillna(0).astype(int)
    contract = year + (month / 12)
    contract = contract.iloc[:, 0]

    periodic = df["contract"].str.contains("定期借家").fillna(0).astype(int)

    df.loc[:, "contract"] = contract
    df.loc[:, "periodic"] = periodic

    return df
