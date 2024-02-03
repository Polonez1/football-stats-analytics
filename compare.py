import data
import data_processing.group_data as group_data
import vizualizations.vizuals as vs

maindata = data.MainData(seasons=[2020, 2021, 2022])


def goals_distribution():
    df = maindata.fixtures_data()
    df = group_data.group_fixture_by_goals(df, by=["goals_result"]).sort_values(
        "count", ascending=False
    )
    df = vs.distribution_by_goals(df=df)

    print(df)


if "__main__" == __name__:
    goals_distribution()
