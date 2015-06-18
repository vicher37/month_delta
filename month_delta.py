__author__ = 'vzhang'

def month_delta(from_year, from_month, to_year, to_month):
    date_list = []
    for year in range(from_year, to_year + 1):
        if year == from_year:
            for month in range(from_month, 12 + 1):
                date_list.append(str(year) + '/' + str(month))
        elif year > from_year and year < to_year:
            for month in range(1, 12 + 1):
                date_list.append(str(year) + '/' + str(month))
        elif year == to_year:
            for month in range(1, to_month + 1):
                date_list.append(str(year) + '/' + str(month))
    return date_list
