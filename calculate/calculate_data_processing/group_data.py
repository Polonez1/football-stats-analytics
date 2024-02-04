import pandas as pd


def group_fixture_by_goals(
    df: pd.DataFrame, by: list = ["goals_result", "league_season", "league_name"]
) -> pd.DataFrame:
    dff = df.groupby(by).agg(count=("goals_result", "count")).reset_index()

    return dff
