import SQL.ssh_sql_connector as SQL
import pandas as pd


class MainData:
    def __init__(self, season):
        self.season = season

    def standings_data(self) -> pd.DataFrame:
        df = SQL.get_standings_data(self.season)

        return df


if "__main__" == __name__:
    maindata = MainData(season=2023)
    df = maindata.standings_data()
    print(df.dtypes)
