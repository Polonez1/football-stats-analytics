import data
import calculate.calc as calc
import vizualizations.vizuals as vs

import pandas as pd

maindata = data.MainData(seasons=[2020, 2021, 2022])


def result_distribution():
    df = maindata.fixtures_data()
    dist = calc.SkellamDistribution(df=df)
    full_data = dist.create_full_data()
    dist_params = dist.skellam_params()

    result = dist.create_fact_result_data()
    print(result.head(20))
    # vs.test(full_data)
    # vs.distribution_graph()


def stats_distribution():
    pass


if "__main__" == __name__:
    result_distribution()
