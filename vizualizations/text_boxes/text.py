def add_text_skellam_bars(fig, params):
    annotation_text = "\n".join([f"{key}: {value}" for key, value in params.items()])
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
