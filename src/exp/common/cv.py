import numpy as np
import pandas as pd

from src.exp.common.train_and_predict import train_and_predict


def cv(cv_df=pd.DataFrame(), model_name="linearRegression", params={}):

    print("----------------", model_name, "----------------")
    result = pd.DataFrame()
    scores = []
    models = []
    for n_fold in cv_df["n_fold"].unique():
        df = cv_df[cv_df["n_fold"] == n_fold]
        train_x = df[df["data_type"] == "train"].drop(
            ["target", "data_type", "index", "n_fold"], axis=1
        )
        val_x = df[df["data_type"] == "val"].drop(
            ["target", "data_type", "index", "n_fold"], axis=1
        )
        train_y = df[df["data_type"] == "train"]["target"].values
        val_y = df[df["data_type"] == "val"]["target"].values

        y_pred, model = train_and_predict(
            train_x=train_x,
            train_y=train_y,
            val_x=val_x,
            model_name=model_name,
            params=params,
        )

        score = np.sqrt(
            ((y_pred.flatten() - val_y.flatten()) ** 2).sum() / len(val_y.flatten())
        )
        scores.append(score)

        print("n_fold: {} Score: {}".format(n_fold, score))

        result = pd.concat(
            [
                result,
                pd.DataFrame(
                    {
                        "index": df[df["data_type"] == "val"]["index"],
                        "predicted": y_pred.flatten(),
                        "real": val_y.flatten(),
                        "difference": y_pred.flatten() - val_y.flatten(),
                        "n_fold": n_fold,
                    }
                ),
            ]
        )
        models.append(model)

    print("----------------", model_name, " END ----------------")
    print()

    return result, scores, models
