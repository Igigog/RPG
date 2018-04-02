import openpyxl
database = openpyxl.load_workbook('database.xlsx')

enemies_list = database['enemies'];     opponents = []
guns_list = database['guns'];           weapons = []
armor_list = database['armor'];         armors = []
location_list = database['locations'];  locations = []
treasure_list = database['loot'];       loot = []

lists = {enemies_list: opponents, guns_list: weapons,
         armor_list: armors, location_list: locations,
         treasure_list: loot}

for listik in lists:        # fill all lists
    for row in listik.rows:
        pre_list = []
        for cell in row:
            pre_list.append(cell.value)
        lists[listik].append(pre_list)
    lists[listik].pop(0)
