import pandas as pd

nameDataFilePath = "../../data/raw/1name_data.tsv"
#print(nameDataFilePath)
nameData = pd.read_csv(nameDataFilePath, sep='\t')                                         
nameData.head(2)