from scipy.stats import poisson
import pandas as pd
import numpy as np

import sys

sys.path.append(".\calc\calculate\calculate_data_processing")

# import calculate.
import calculate_data_processing.skellam_dist_proc as skellam_dist_proc

# import calculate.
import calculate_data_processing.group_data as group_data


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


def result_from_skellam_matrix(avg_1, avg_2):
    skellam_matrix = skellam_dist_matrix(avg_1, avg_2)
    goals_range = list(range(0, 11))

    draw = 0
    home_win = 0
    away_win = 0

    for i in goals_range:
        for j in goals_range:
            prb = skellam_matrix.iloc[i, j]
            if i == j:
                draw = draw + prb
            if i > j:
                home_win = home_win + prb
            if i < j:
                away_win = away_win + prb

    return pd.DataFrame(
        {"result": ["home_win", "draw", "away_win"], "prb": [home_win, draw, away_win]}
    )


class SkellamDistribution:
    def __init__(self, df: pd.DataFrame, season: int = None, league: str = None):
        self.data = df
        self.league = league
        self.season = season

        if season is not None:
            self.__filter_by_season()
        if league is not None:
            self.__filter_by_league()

    def __filter_by_season(self):
        if self.season is not None:
            self.data = self.data[self.data["league_season"] == self.season]

    def __filter_by_league(self):
        if self.league is not None:
            self.data = self.data[self.data["league_name"] == self.league]

    def __get_averages(self):
        df_agg = self.data.agg(
            {
                "fixture_id": "count",
                "goals_home": "mean",
                "goals_away": "mean",
            }
        )
        return df_agg

    def __skellam_distribution_data(self):
        averages = self.__get_averages()
        skellam_dist = results_distribution_by_skellam(
            avg_1=averages["goals_home"],
            avg_2=averages["goals_away"],
            total=averages["fixture_id"],
        )
        skellam_dist = skellam_dist_proc.skellam_dist_processing(skellam_dist)
        return skellam_dist

    def __fact_distribution_data(self):
        df = group_data.group_fixture_by_goals(self.data, by=["goals_result"])
        df["source"] = "fact"

        return df

    def create_full_data(self):
        fact = self.__fact_distribution_data()
        skellam_dist = self.__skellam_distribution_data()

        dff = pd.concat([fact, skellam_dist])

        return dff

    def skellam_params(self):
        averages = self.__get_averages()
        season = self.season
        league = self.league
        avg_1 = averages["goals_home"]
        avg_2 = averages["goals_away"]
        total = averages["fixture_id"]

        return {
            "avg1": round(avg_1, 2),
            "avg2": round(avg_2, 2),
            "total": int(total),
            "season": season,
            "league": league,
        }

    def __create_fact_result_data(self):
        df = self.data.groupby("result").size().reset_index(name="count")
        return df

    def __create_skellam_result_data(self):
        averages = self.__get_averages()

        # result_from_skellam_matrix()


if "__main__" == __name__:
    p = result_from_skellam_matrix(1.4, 1.2)
    print(p)
