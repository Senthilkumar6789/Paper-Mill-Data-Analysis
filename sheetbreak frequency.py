import pandas as pd

file_path = r"E:\Datasets\PD_May_22_2022-06-01.csv"
data = pd.read_csv(file_path)

data['datetime'] = pd.to_datetime(data['datetime'])

data.set_index('datetime', inplace=True)

data_15min = data.resample('15T').mean()

data_15min.reset_index(inplace=True)

output_file_path = r"E:\Datasets\may.csv"
data_15min.to_csv(output_file_path, index=False)
