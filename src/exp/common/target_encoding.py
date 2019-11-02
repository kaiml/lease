import numpy as np
import pandas as pd


def target_encoding(
    tr_df=pd.DataFrame(), te_df=pd.DataFrame(), col_name="", methods={"mean": np.mean}
):
    for method_name, method in methods.items():
        target_map = tr_df.groupby(col_name)["target"].agg(method)
        tr_df.loc[:, "target_" + col_name + "_" + method_name] = tr_df[col_name].map(
            target_map
        )
        te_df.loc[:, "target_" + col_name + "_" + method_name] = te_df[col_name].map(
            target_map
        )
    return tr_df, te_df
