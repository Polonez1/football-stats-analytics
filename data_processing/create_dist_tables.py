import pandas as pd


def __rename_skellam_dist_data_col(df: pd.DataFrame) -> pd.DataFrame:
    df = df[["result_goal", "exp_counts"]].rename(
        columns={"result_goal": "goals_result", "exp_counts": "count"}
    )
    return df


def __add_source_col(df: pd.DataFrame, source_name: str):
    df["source"] = source_name
    return df


def skellam_dist_processing(df: pd.DataFrame) -> pd.DataFrame:
    df = __rename_skellam_dist_data_col(df)
    df = __add_source_col(df, "skellam dist")
    return df
