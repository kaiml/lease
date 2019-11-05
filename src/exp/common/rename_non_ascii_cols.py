def rename_non_ascii_cols(df):
    # rename columns as lightGBM doesn't support japanese column names.
    rename_cols = {}
    i = 1
    for col_name in df.filter(like="ohe_").columns:
        rename_cols[col_name] = "_".join(col_name.split("_")[:2]) + "_{}".format(i)
        i += 1
    df = df.rename(columns=rename_cols)
    return df, rename_cols
