import data
import data_processing.group_data as group_data
import data_processing.create_dist_tables as dist
import calculate.calc as calc
import vizualizations.vizuals as vs

import pandas as pd

maindata = data.MainData(seasons=[2020, 2021, 2022])


def result_distribution():
    df = maindata.fixtures_data()
    averages = maindata.get_standings_averages()
    skellam_dist = calc.results_distribution_by_skellam(
        avg_1=averages["goals_home"],
        avg_2=averages["goals_away"],
        total=averages["fixture_id"],
    )

    skellam_dist = dist.skellam_dist_processing(skellam_dist)
    df = group_data.group_fixture_by_goals(df, by=["goals_result"]).sort_values(
        "count", ascending=False
    )
    df["source"] = "fact"
    dff = pd.concat([skellam_dist, df])
    vs.distribution_by_goals(df=dff)


def stats_distribution():
    pass


if "__main__" == __name__:
    result_distribution()
