import pandas as pd
import argparse
countries  = pd.read_csv('owid-covid-data.csv',encoding = 'ISO-8859-1', index_col = 'Country')
