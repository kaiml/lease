from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

sample_submit = pd.read_csv("input/sample_submit.csv")
df_train = pd.read_csv("data/example_train.csv", index_col=False)
df_test = pd.read_csv("data/example_test.csv", index_col=False)


# Train Test Split
X_train, X_val, y_train, y_val = train_test_split(
    df_train.iloc[:, :5], df_train.loc[:, "target"], test_size=0.33, random_state=42
)


def rmse(y, y_pred):
    return -np.sqrt(mean_squared_error(y, y_pred))


# Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=0)

model.fit(X_train, y_train)

y_pred = model.predict(X_val)
RMSE = np.sqrt(mean_squared_error(y_val.values, y_pred))
print("RMSE:", RMSE)

y_test = model.predict(df_test.iloc[:, :5])

pd.concat([sample_submit.iloc[:, 0], pd.Series(y_test)], axis=1).to_csv(
    "output/example_01.csv",
    header=False,
    index=False,
)
