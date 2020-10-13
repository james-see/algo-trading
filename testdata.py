import pandas as pd

pd.core.common.is_list_like = pd.api.types.is_list_like

from pandas_datareader import data

df = data.get_data_yahoo('MSFT', '2018-01-01', '2019-01-01')

print(df.head())