import pandas as pd
import numpy as np
np.random.seed(10)


data = {
    'tra': pd.read_csv('Data/air_visit_data.csv'),
    'as': pd.read_csv('Data/air_store_info.csv'),
    'hs': pd.read_csv('Data/hpg_store_info.csv'),
    'ar': pd.read_csv('Data/air_reserve.csv'),
    'hr': pd.read_csv('Data/hpg_reserve.csv'),
    'id': pd.read_csv('Data/store_id_relation.csv'),
    'tes': pd.read_csv('Data/sample_submission.csv'),
    'hol': pd.read_csv('Data/date_info.csv').rename(columns={'calendar_date':'visit_date'})
    }

data['hr'] = pd.merge(data['hr'], data['id'], how='inner', on=['hpg_store_id'])

data
