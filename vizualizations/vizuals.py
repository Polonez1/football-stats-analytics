import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from plotly.subplots import make_subplots

from dash.dependencies import Input, Output
from vizualizations.text_boxes import text

import dash
from dash import dcc, html


def distribution_by_goals(df: pd.DataFrame, params: dict = None):
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
    if params is not None:
        text.add_text_skellam_bars(fig=fig, params=params)

    fig.show()


def distribution_by_final_result(df: pd.DataFrame):
    pass


# def test(df: pd.DataFrame, params: dict = None):
#    # Pierwszy wykres
#    df1 = df.sort_values(by="count", ascending=False)
#    df1 = df1.loc[df1["count"] > 0]
#    fig1 = px.bar(
#        df1,
#        x="goals_result",
#        y="count",
#        color="source",
#        barmode="group",
#        title="Compare by fact and skellam dist.",
#    )
#    fig1.update_xaxes(type="category")
#    if params is not None:
#        text.add_text_skellam_bars(fig=fig1, params=params)
#
#    # Drugi niezależny wykres
#    fig2 = go.Figure()
#    fig2.add_trace(
#        go.Bar(
#            x=["Category A", "Category B", "Category C"],
#            y=[10, 20, 15],
#            name="Example Bar Chart",
#        )
#    )
#    fig2.update_layout(
#        title="Example Independent Bar Chart",
#        xaxis_title="X-axis Title",
#        yaxis_title="Y-axis Title",
#    )
#
#    # Tworzenie subplotu z dwoma wierszami i jedną kolumną
#    fig_combined = make_subplots(rows=2, cols=1, shared_xaxes=False)
#
#    # Dodanie pierwszego wykresu do subplotu
#    for trace in fig1.data:
#        fig_combined.add_trace(trace, row=1, col=1)
#
#    # Dodanie drugiego wykresu do subplotu
#    for trace in fig2.data:
#        fig_combined.add_trace(trace, row=2, col=1)
#
#    # Zaktualizowanie układu subplotu
#    fig_combined.update_layout(title_text="Combined Subplots")
#    fig_combined.show()
