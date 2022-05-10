import pandas as pd 

covid_url = ("https://www.data.gouv.fr/fr/datasets/r/63352e38-d353-4b54-bfd1-f1b3ee1cabd7")
df = pd.read_csv(covid_url, sep = ";", parse_dates = True, index_col = 2)
df = df.query("sexe == 0")
df.sort_index(inplace = True)
sdf = df.groupby(['jour']).sum()




def get_hospis():
	return pd.Series(sdf.tail(1)["hosp"], dtype = "string")[0]


def get_reas():
	return pd.Series(sdf.tail(1)["rea"], dtype = "string")[0]
	
	

if __name__ == "__main__":
	stats.run()

