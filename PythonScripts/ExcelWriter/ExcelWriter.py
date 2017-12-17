from openpyxl import load_workbook
from openpyxl.utils import coordinate_from_string, column_index_from_string


class ExcelWriter(object):
    def __init__(self, project_name='ProjectName', month='January', year='2017', file_path='ForecastOutput.xltx'):
        self.workbook = load_workbook(file_path)
        self.workbook.template = False
        self.worksheet = self.workbook['Forecast']
        self.default_value = 'No Forecast Yet'
        self.project_name = project_name
        self.month_year = month + ", " + year
        self.worksheet['C1'] = self.project_name
        self.worksheet['C2'] = self.month_year

#Insert one value to any cell in the Individual/Group Forecast/Actual table.

    def insert_individual_forecast_values(self, forecast_value, sub_segment, metric):
        sub_segment_index = self.__check_individual_forecast_subsegment(sub_segment)
        metric_index = self.__check_individual_forecast_metric(metric)
        forecast_cell = self.worksheet.cell(row=metric_index, column=sub_segment_index)
        forecast_cell.value = forecast_value

    def insert_group_forecast_values(self, forecast_value, sub_segment, metric):
        sub_segment_index = self.__check_group_forecast_subsegment(sub_segment)
        metric_index = self.__check_group_forecast_metric(metric)
        forecast_cell = self.worksheet.cell(row=metric_index, column=sub_segment_index)
        forecast_cell.value = forecast_value

# Save Workbook

    def save_file(self):
        title = self.project_name + ' - Forecast Report, ' + self.month_year + '.xlsx'
        self.workbook.save(title)

# Check for Individual/Group Forecast Subsegment/Metric Index

    def __check_individual_forecast_subsegment(self, sub_segment):
        for sub_segment_range in self.worksheet.iter_rows(min_row=5, max_row=5, min_col=3, max_col=19):
            for cell in sub_segment_range:
                if cell.value == sub_segment:
                    c = cell.column
                    r = cell.row
                    cr = c+str(r)
                    xy = coordinate_from_string(cr)
                    col = column_index_from_string(xy[0])
                    return col
        error = "Error: wrong segment"
        print(error)

    def __check_group_forecast_subsegment(self, sub_segment):
        for sub_segment_range in self.worksheet.iter_rows(min_row=16, max_row=16, min_col=3, max_col=18):
            for index, cell in enumerate(sub_segment_range):
                if cell.value == sub_segment:
                    c = cell.column
                    r = cell.row
                    cr = c + str(r)
                    xy = coordinate_from_string(cr)
                    col = column_index_from_string(xy[0])
                    return col
        error = "Error: wrong segment"
        print(error)

    def __check_individual_forecast_metric(self, metric):
        for metric_range in self.worksheet.iter_rows(min_row=6, max_row=12, min_col=2, max_col=2):
            for cell in metric_range:
                if cell.value == metric:
                    return cell.row

    def __check_group_forecast_metric(self, metric):
        for metric_range in self.worksheet.iter_rows(min_row=17, max_row=23, min_col=2, max_col=2):
            for index, cell in enumerate(metric_range):
                if cell.value == metric:
                    return cell.row

#Check for Individual/Group Actual Subsegment/Metric Index

    def __check_individual_actual_subsegment(self, sub_segment):
        for sub_segment_range in self.worksheet.iter_rows(min_row=5, max_row=5, min_col=23, max_col=39):
            for index, cell in enumerate(sub_segment_range):
                if cell.value == sub_segment:
                    c = cell.column
                    r = cell.row
                    cr = c + str(r)
                    xy = coordinate_from_string(cr)
                    col = column_index_from_string(xy[0])
                    return col
        error = "Error: wrong segment"
        print(error)

    def __check_group_actual_subsegment(self, sub_segment):
        for sub_segment_range in self.worksheet.iter_rows(min_row=16, max_row=16, min_col=23, max_col=38):
            for index, cell in enumerate(sub_segment_range):
                if cell.value == sub_segment:
                    c = cell.column
                    r = cell.row
                    cr = c + str(r)
                    xy = coordinate_from_string(cr)
                    col = column_index_from_string(xy[0])
                    return col
        error = "Error: wrong segment"
        print(error)

    def __check_individual_actual_metric(self, metric):
        for metric_range in self.worksheet.iter_rows(min_row=6, max_row=12, min_col=22, max_col=22):
            for index, cell in enumerate(metric_range):
                if cell.value == metric:
                    return cell.row

    def __check_group_actual_metric(self, metric):
        for metric_range in self.worksheet.iter_rows(min_row=17, max_row=23, min_col=22, max_col=22):
            for index, cell in enumerate(metric_range):
                if cell.value == metric:
                    return cell.row
