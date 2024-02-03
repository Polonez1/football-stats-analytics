from scipy.stats import poisson
import pandas as pd
import numpy as np


def calculate_poisson_dist(avg: int):
    goals_list = list(range(0, 11))
    data = {
        "goal": goals_list,
        "p": [poisson.pmf(k=goal, mu=avg).round(2) for goal in goals_list],
    }
    df = pd.DataFrame(data)
    return df


def skellam_dist_matrix(avg_1, avg_2):
    distribution_1 = calculate_poisson_dist(avg=avg_1)
    distribution_2 = calculate_poisson_dist(avg=avg_2)
    matrix = np.outer(distribution_1["p"], distribution_2["p"])
    result_df = pd.DataFrame(
        matrix, index=distribution_1["goal"], columns=distribution_2["goal"]
    ).reset_index(drop=True)
    return result_df


def goals_matrix_melt(avg_1, avg_2):
    result_df = skellam_dist_matrix(avg_1=avg_1, avg_2=avg_2)
    result_df_melt = result_df.stack().reset_index()
    result = result_df_melt.rename(
        columns={"level_0": "goal_1", "goal": "goal_2", 0: "prb"}, inplace=False
    )
    result["result_goal"] = (
        result["goal_1"].astype("str") + "-" + result["goal_2"].astype("str")
    )

    return result


def results_distribution_by_skellam(avg_1, avg_2, total):
    df = goals_matrix_melt(avg_1=avg_1, avg_2=avg_2)
    df["exp_counts"] = df["prb"] * total
    df["exp_counts"] = df["exp_counts"].round(0)

    return df
