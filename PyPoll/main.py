# -*- coding: UTF-8 -*-

import os
import csv
from collections import Counter

Total_vote =0
Candidate_list = []
Winner = ""
Winner_votes = 0

filepath = os.path.join("raw_data", "election_data_2.csv")

with open(filepath) as csvfile:
	reader = csv.DictReader(csvfile)
	
	for row in reader:
		Candidate = row['Candidate']
		Candidate_list.append(Candidate)
Election_results = Counter(Candidate_list)			

for total_votes_results in Election_results.items():
	Total_vote += total_votes_results[1]
	
	
Results_string_start = f'''Election Results
-------------------------
Total Votes: {Total_vote}
-------------------------'''
print(Results_string_start)
for names_results in Election_results.items():
	Percent_of_vote = names_results[1] / Total_vote
	print(str(names_results[0]) + " " +str(round(Percent_of_vote*100.00,1))+ "% " +str(names_results[1]))
	if Winner_votes < names_results[1]:
		Winner = names_results[0]


Results_string_end = f'''-------------------------
Winner: {Winner}
-------------------------
'''
print(Results_string_end)

