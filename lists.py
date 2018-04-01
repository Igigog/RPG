import openpyxl
database = openpyxl.load_workbook('database.xlsx')

enemies_list = database['enemies']
guns_list = database['guns']
armor_list = database['armor']
location_list = database['locations']

locations = []
opponents = []
weapons = []
armors = []

lists = {enemies_list: opponents, guns_list: weapons,
         armor_list: armors, location_list: locations}

for listik in lists:        # fill all lists
    for row in listik.rows:
        pre_list = []
        for cell in row:
            pre_list.append(cell.value)
        lists[listik].append(pre_list)
    lists[listik].pop(0)
