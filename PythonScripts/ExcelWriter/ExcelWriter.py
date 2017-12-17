from openpyxl import load_workbook


class ExcelWriter(object):
    def __init__(self, file_path, project_name='ProjectName', month='January', year='2017'):
        self.template = load_workbook('ForecastOutput.xlsx')
        self.sheet = self.template['Forecast']
        self.default_value = 'No Forecast Yet'
        month_year = month + ", " + year
        self.sheet['C1'] = project_name
        self.sheet['C2'] = month_year
        self.sub_segment_list = ['Rack', 'Corporate', 'Corporate Others', 'Packages/Promo', 'Wholesale Online'
            , 'Wholesale Offline', 'Individual Others', 'Industry Rate']

#Insert one value to any cell in the Individual/Group Forecast/Actual table.

    def insert_individual_forecast_values(self, forecast_value, sub_segment, metric):
        sub_segment_index = self.__check_individual_forecast_subsegment(sub_segment)
        metric_index = self.__check_individual_forecast_metric(metric)
        forecast_cell = self.sheet.cell(row=metric_index, column=sub_segment_index)
        forecast_cell.value = forecast_value

    def insert_group_forecast_values(self, forecast_value, sub_segment, metric):
        sub_segment_index = self.__check_group_forecast_subsegment(sub_segment)
        metric_index = self.__check_group_forecast_metric(metric)
        forecast_cell = self.sheet.cell(row=metric_index, column=sub_segment_index)
        forecast_cell.value = forecast_value

# Check for Individual/Group Forecast Subsegment/Metric Index

    def __check_individual_forecast_subsegment(self, sub_segment):
        for sub_segment_range in self.sheet.iter_rows(min_row=5, max_row=5, min_col=3, max_col=19):
            for index, cell in enumerate(sub_segment_range):
                if cell.value == sub_segment:
                    return index

    def __check_group_forecast_subsegment(self, sub_segment):
        for sub_segment_range in self.sheet.iter_rows(min_row=16, max_row=16, min_col=3, max_col=18):
            for index, cell in enumerate(sub_segment_range):
                if cell.value == sub_segment:
                    return index

    def __check_individual_forecast_metric(self, metric):
        for metric_range in self.sheet.iter_rows(min_row=6, max_row=12, min_col=2, max_col=2):
            for index, cell in enumerate(metric_range):
                if cell.value == metric:
                    return index

    def __check_group_forecast_metric(self, metric):
        for metric_range in self.sheet.iter_rows(min_row=17, max_row=23, min_col=2, max_col=2):
            for index, cell in enumerate(metric_range):
                if cell.value == metric:
                    return index

#Check for Individual/Group Actual Subsegment/Metric Index

    def __check_individual_actual_subsegment(self, sub_segment):
        for sub_segment_range in self.sheet.iter_rows(min_row=5, max_row=5, min_col=23, max_col=39):
            for index, cell in enumerate(sub_segment_range):
                if cell.value == sub_segment:
                    return index

    def __check_group_actual_subsegment(self, sub_segment):
        for sub_segment_range in self.sheet.iter_rows(min_row=16, max_row=16, min_col=23, max_col=38):
            for index, cell in enumerate(sub_segment_range):
                if cell.value == sub_segment:
                    return index

    def __check_individual_actual_metric(self, metric):
        for metric_range in self.sheet.iter_rows(min_row=6, max_row=12, min_col=22, max_col=22):
            for index, cell in enumerate(metric_range):
                if cell.value == metric:
                    return index

    def __check_group_actual_metric(self, metric):
        for metric_range in self.sheet.iter_rows(min_row=17, max_row=23, min_col=22, max_col=22):
            for index, cell in enumerate(metric_range):
                if cell.value == metric:
                    return index
