import SQL.ssh_sql_connector as SQL
import pandas as pd
import data_processing.add_columns as add_columns

# import data_processing.group_data as group_data


class MainData:
    def __init__(self, seasons):
        self.seasons: list = seasons

    def standings_data(self) -> pd.DataFrame:
        dff = []
        for season in self.seasons:
            df = SQL.get_standings_data(season)
            df = add_columns.add_average_goals(df=df)
            dff.append(df)

        # dft = pd.concat(dff)
        # dfg = dft.agg(
        #    {
        #        "goal_avg_GF": "mean",
        #        "goal_avg_GA": "mean",
        #    }
        # )
        # return dfg

    def fixtures_data(self) -> pd.DataFrame:
        df: pd.DataFrame = SQL.get_fixtures_data()
        dff = df.loc[df["league_season"].isin(self.seasons)]
        dff = add_columns.add_goals_string_result(dff)
        # dff = group_data.group_fixture_by_goals(dff)

        return dff


if "__main__" == __name__:
    maindata = MainData(seasons=[2020, 2021, 2022])
    df = maindata.standings_data()
    print(df.head(20))
    # df.to_csv("./data/fixtures.csv")
    # print(df.head(20))
