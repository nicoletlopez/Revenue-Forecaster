from PythonScripts.ExcelWriter import ExcelWriter

revpar ='Revenue Per       Average Rate'
arr = 'Avarage Room Rate'
occupancy = 'Occupancy (%)'
revenue = "Revenue (000's)"
rack = 'Rack'

#constructor(project_name, month, year
writer = ExcelWriter.ExcelWriter("Urmum's Project", 'December', '2016')
#insert_individual_forecast_values(value, subsegment, metric)
writer.insert_individual_forecast_values(30, 'Corporate Others', occupancy)
writer.insert_individual_forecast_values(40, 'Rack', occupancy)
#title format: project_name + ' - Forecast Report,' + month_year + '.xlsx'
writer.save_file()