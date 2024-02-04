import data
import calculate.calc as calc
import vizualizations.vizuals as vs

import pandas as pd

maindata = data.MainData(seasons=[2020, 2021, 2022])


def result_distribution():
    df = maindata.fixtures_data()
    graph = calc.SkellamDistribution(df=df)
    full_data = graph.create_full_data()
    vs.distribution_by_goals(full_data)


def stats_distribution():
    pass


if "__main__" == __name__:
    result_distribution()
