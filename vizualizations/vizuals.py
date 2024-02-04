import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from dash.dependencies import Input, Output
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
        annotation_text = "\n".join(
            [f"{key}: {value}" for key, value in params.items()]
        )
        fig.update_layout(
            annotations=[
                dict(
                    text=annotation_text,
                    xref="paper",
                    yref="paper",
                    x=0.5,
                    y=1,
                    showarrow=False,
                    align="left",
                    font=dict(size=10),
                )
            ]
        )
    fig.show()


# def distribution_graph(df: pd.DataFrame = px.data.tips()):
#    app = dash.Dash(__name__)
#    app.layout = html.Div(
#        [
#            # Rozwijane menu (Dropdown) do wyboru wartości filtra
#            dcc.Dropdown(
#                id="filter-dropdown",
#                options=[
#                    {"label": "Total Bill > 20", "value": 20},
#                    {"label": "Total Bill > 30", "value": 30},
#                ],
#                value=20,  # Wartość domyślna
#                style={"width": "50%"},
#            ),
#            # Wykres Histogram
#            dcc.Graph(id="histogram-plot"),
#        ]
#    )
#
#    # Funkcja do aktualizacji wykresu na podstawie wartości filtra
#    @app.callback(
#        Output("histogram-plot", "figure"), [Input("filter-dropdown", "value")]
#    )
#    def update_histogram(selected_value):
#        filtered_data = df[df["total_bill"] > selected_value]
#        fig = px.histogram(filtered_data, x="total_bill", nbins=30, title="Histogram")
#        return fig
#
#    app.run_server(debug=True)
