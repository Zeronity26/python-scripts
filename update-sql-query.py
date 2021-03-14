import pandas as pd

sample_data = pd.read_csv('./sample-data/sample-data-for-update-sql-query.csv')

table_name = input("Enter Table Name: ") 
columns = list(sample_data.columns)

sql_file = open("./output/update_query.sql", "w")

for row_index, row in sample_data.iterrows():
    update_data = []
    where_condition = ''
    for column_index, column in enumerate(columns):
        if column_index == 0:
            where_condition = f'WHERE {column}={row[column_index]}'
        else:
            #for handling NaN case
            if row[column_index] and row[column_index]==row[column_index]:
                update_data.append(f'{column}={row[column_index]}')
    if update_data:
        update_data_string = ','.join(map(str,update_data))
        update_statement = f'UPDATE {table_name} SET {update_data_string} {where_condition};\n'
        print(f'writing sql record ... {row_index+1}')
        sql_file.write(update_statement)    

sql_file.close()
