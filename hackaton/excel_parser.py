import xlrd

result = dict()
# workbook = xlrd.open_workbook('my_file_name.xls', encoding='cp1252', on_demand=True)
workbook = xlrd.open_workbook("E:/last_download/Tender Hack/20200124_СТЕ_all/table.xlsx", encoding_override="cp1252",
                              on_demand=True)
worksheet = workbook.sheet_by_index(0)

i = 0
for i, data in enumerate(worksheet.get_rows()):
    if i != 0:
        ex_words = ["услуги", "работы"]
        id_, cat, subcat = int(data[0].value), data[4].value, data[5].value
        if any(ex_word in field for field in [cat, subcat] for ex_word in ex_words):
            pass
        else:
            obj = [id_, subcat]
            # result[cat] = result[cat] + [obj] if cat in result.keys() else [obj]
            if cat not in result.keys():
                result[cat] = dict()
            if subcat not in result[cat].keys():
                result[cat][subcat] = list()
            result[cat][subcat].append(id_)
            # result[data[4].value] = [data[0].value, data[5].value]
            # print(id, cat, subcat)

print(result.keys())

print(result)