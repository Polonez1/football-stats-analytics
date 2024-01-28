import SQL.ssh_sql_connector as SQL
import pandas as pd
import data_processing.add_columns as add_columns


class MainData:
    def __init__(self, seasons):
        self.seasons: list = seasons

    def standings_data(self) -> pd.DataFrame:
        dff = []
        for season in self.seasons:
            df = SQL.get_standings_data(season)
            df = add_columns.add_average_goals(df=df)
            dff.append(df)

        return pd.concat(dff)

    def fixtures_data(self) -> pd.DataFrame:
        df: pd.DataFrame = SQL.get_fixtures_data()
        dff = df.loc[df["league_season"].isin(self.seasons)]

        return dff


if "__main__" == __name__:
    maindata = MainData(seasons=[2020, 2021, 2022])
    df = maindata.fixtures_data()
    print(df.head(20))
