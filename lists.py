import openpyxl
database = openpyxl.load_workbook('database.xlsx')
enemies_list = database['enemies']
guns_list = database['guns']
opponents = []
weapons = []
for row in enemies_list.rows:
    pre_list = []
    for cell in row:
        pre_list.append(cell.value)
    opponents.append(pre_list)

for row in guns_list.rows:
    pre_list = []
    for cell in row:
        pre_list.append(cell.value)
    weapons.append(pre_list)

weapons.pop(0)
opponents.pop(0)
