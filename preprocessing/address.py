import pandas as pd

# address: split into address_1, 2, 3
def pp_address(df):
  address = df["address"]
  address = address.str.replace("東京都", "")

  address_1 = address.str.split("区", expand=True).iloc[:, 0]
  address_2_3 = address.str.split("区", expand=True).iloc[:, 1]

  def to_hankaku(text):
      return text.translate(
          str.maketrans({chr(0xFF01 + i): chr(0x21 + i) for i in range(94)})
      )

  # 全角 -> 半角
  address_2_3 = address_2_3.map(to_hankaku)

  # split into address_2
  address_2 = address_2_3.str.split(r"\d", n=1, expand=True).iloc[:, 0]

  # "滝野川3丁目23" -> "3丁目23"
  address_3 = pd.DataFrame(
      {"address_2": address_2, "address_2_3": address_2_3}
  ).apply(lambda x: x.address_2_3.replace(x.address_2, ""), axis=1)

  df.loc[:, "address_1"] = address_1
  df.loc[:, "address_2"] = address_2
  df.loc[:, "address_3"] = address_3
  return df