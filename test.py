# def a(x, *c, **b):
#     print(f' x is {x}\n b is {b}\n c is {c}')
#     print(b.get('b', 'csv'))


# a('amar', ' omk', 'aro')

import pandas as pd
SUPPORTED_DATA_TYPES = ['csv', 'txt']

# current_directory = os.getcwd()


# def a(tableName: str, *column, **fileType) -> None:
#     # File Type, Default File Type Csv
#    # pfileType = (fileType in SUPPORTED_DATA_TYPES &
#     #            fileType.get('fileType', 'csv')) or 'csv'
#     sfileType = fileType.get('fileType', 'csv') if fileType.get(
#         'fileType', 'csv') in SUPPORTED_DATA_TYPES else 'csv'
#     print(sfileType)


# a('ss')
# print(
#     f'You Are Redirected To Default Format\nFormat Named "JDHD" Doesnot exist here, You may again Check \nDoes {format} spelling is correct.')


# Create a DataFrame
# data = [{'name': ['Alice', 'Bob', 'Charlie'],
#         'age': [25, 30, 35]}, {'name': ['Alice', 'Bob', 'Charlie'],
#         'age': [25, 30, 35]}]
# df = pd.DataFrame(data)

# # Write the DataFrame to a JSON file
l = "C:\\Users\\Lipu\\OneDrive\\Desktop\\GulistanDB\\Data\\AMARDBT.json"


# # Load the existing JSON file into a Pandas DataFrame
# df = pd.read_json('/path/to/json/file.json')

# # Append new data to the DataFrame
# new_data = {'name': 'David', 'age': 40}
# df = df.append(data, ignore_index=True)

# # Write the updated DataFrame to a new JSON file
# df.to_json('/path/to/new/json/file.json', orient='records')

# with open(l, 'r') as file:
#     data = file.read()
#     print(data)


thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(len("222"))


print(f'ABCD\bEFGH')


def a(**f):
    print(f)


a(fileName="jsjs", OP="sss")
