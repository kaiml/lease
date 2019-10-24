import pandas as pd

# equipment : Ont-Hot Encoding
def pp_equipment(df):
  equipment = df["equipment"]
  equipment = equipment.str.replace("／", "")

  # Create unique values list
  bathroom_unique = pd.Series(
      pd.Series(equipment.str.split("\t", expand=True).values.flatten()).unique()
  )
  # drop None, NaN, and ''
  bathroom_unique = bathroom_unique[~bathroom_unique.isnull()]
  bathroom_unique = bathroom_unique[bathroom_unique != ""]

  # One-Hot Encoding
  for col_name in bathroom_unique:
      df.loc[:, "ohe_equipment_" + col_name] = (
          df["equipment"].fillna("").str.contains(col_name).astype(int)
      )

  return df