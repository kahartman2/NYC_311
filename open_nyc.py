import requests
import pandas as pd
import json

open_nyc = requests.get('https://data.cityofnewyork.us/resource/fhrw-4uyv.json?$limit=300000').json
# print(open_nyc())

open_nyc_df = pd.DataFrame(open_nyc)
