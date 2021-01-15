import pandas as pd

df = pd.read_csv('usable_csv.csv') #處理過後的csv檔案

def compute(station, time):
	if time == 'Morning':
		data = df[(df['time'].isin([7,8,9]))]	 #早上時段的csv
	elif time == 'Noon':
		data = df[(df['time'].isin([11,12,13]))] #中午時段的csv
	else:
		data = df[(df['time'].isin([17,18,19]))] #晚上時段的csv

	output_df = data[data['in station'] == station].groupby(by=['date', 'in station', 'time']).sum()	#抓取資料(進站人數)
	output_list = output_df.pivot_table(index = 'date', columns = 'time').values.tolist()	#將dataframe轉換為list

	#print(output_list)
	return output_list



