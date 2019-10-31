import numpy as np

import plotly.graph_objects as go


def plot_result(df, result, n_fold, model_name):
    r = result[result.n_fold == n_fold].reset_index()
    text = (
        df.loc[r["index"]][["area", "address", "layout", "age", "floor_stories"]]
        .astype(str)
        .apply(lambda row: "<br>".join(row), axis=1)
    )
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=r["predicted"],
            y=r["real"],
            hoverinfo="text",
            mode="markers",
            name="pred&real",
            text=text,
        )
    )
    fig.add_trace(
        go.Scatter(
            x=[r["predicted"].min(), r["predicted"].max()],
            y=[r["predicted"].min(), r["predicted"].max()],
            hoverinfo="text",
            mode="lines",
            name="y=x",
        )
    )
    fig.update_layout(
        title="model: {}, n_fold: {}, RMSE: {}".format(
            model_name,
            n_fold,
            np.sqrt((r["difference"] ** 2).sum() / r["difference"].size),
        ),
        xaxis_title="predicted",
        yaxis_title="real",
    )
    fig.show()
