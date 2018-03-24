# -*- coding: UTF-8 -*-
import os
import csv

Total_number_of_months = 0
Total_revenue = 0
Average_revenue = 0

Last_month_revenue = 0
current_month_revenue = 0

Greatest_increase = 0
Increase_Month = ""
Greatest_decrease = 0
Decrease_Month = ""

i=0

filepath = os.path.join("raw_data", "budget_data_1.csv")

with open(filepath) as csvfile:
	reader = csv.DictReader(csvfile)

	
	for row in reader:
		i += 1
		Total_number_of_months = i
		Last_month_revenue = current_month_revenue
		date_string = row['Date']
		revenue_int = int(row['Revenue'])
		
		current_month_revenue = revenue_int 
		Total_revenue += revenue_int 
		Difference_monthly = Last_month_revenue - current_month_revenue
        
		if Difference_monthly > Greatest_increase:
			Greatest_increase = Difference_monthly
			Increase_Month = date_string
		if Difference_monthly < Greatest_decrease:
			Greatest_decrease = Difference_monthly
			Decrease_Month = date_string


Average_revenue = int(Total_revenue/Total_number_of_months)
Results_string = f'''
Financial Analysis
----------------------------
Total Months: {Total_number_of_months}
Total Revenue: ${Total_revenue}
Average Revenue Change: ${Average_revenue}
Greatest Increase in Revenue: {Incre ase_Month} (${Greatest_increase})
Greatest Decrease in Revenue: {Decrease_Month} (${Greatest_decrease})
'''
print(Results_string)

