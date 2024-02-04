import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd


def distribution_by_goals(df: pd.DataFrame):
    df = df.sort_values(by="count", ascending=False)
    df = df.loc[df["count"] > 0]
    fig = px.bar(
        df,
        x="goals_result",
        y="count",
        color="source",
        barmode="group",
        title="Compare by fact and skellam dist.",
    )
    fig.update_xaxes(type="category")

    fig.show()
