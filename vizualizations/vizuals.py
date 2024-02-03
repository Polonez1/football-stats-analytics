import plotly.express as px
import pandas as pd


def distribution_by_goals(df: pd.DataFrame):
    fig = px.histogram(
        df, x="goals_result", y="count", histfunc="sum", barmode="group", height=400
    )

    fig.show()
