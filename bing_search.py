from py_ms_cognitive import PyMsCognitiveNewsSearch
import pandas as pd 
import numpy as np
import csv

with open('/Users/kunalsingh/Documents/ML@Berkeley/Investarget/bing_data.csv', 'a') as data:
	writer = csv.writer(data)
	df = pd.read_csv('/Users/kunalsingh/Documents/ML@Berkeley/Investarget/CrunchbaseMattermarkMerge.csv',  usecols=[1])
	names = df['Name'].values.tolist()

	for name in names:
		search_service = PyMsCognitiveNewsSearch('7831cba4b4104e7b9d45ab6666ad3514', name)
		first_fifty_result = search_service.search(limit=10, format='json')

		descriptions = []
		for item in first_fifty_result:
			descriptions.append(item.description)
    	writer.writerow(descriptions)
