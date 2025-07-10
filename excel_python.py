# 1. The column Id has to be
# transformed = The first letter
# of the name and the last
# concatenated with its numerical value
# example: JZ1

# 2. The first name column must have
# the first and last name starting
# with a capital letter
# example: Juan Perez

# 3. The profession column must be
# capitalized

# 4. Create a new column ‘Total’ after # salary.
# salary, which will be equal to
# salary - tax (20% of the salary)
# example: 200 - 40 = 160

# 5. Create a new column called # Index, it will be a new column called
# Index, it will be an auto-generated column.
# numerical and sequential.
# It should be placed as the first column
# 1 - Juan Perez, 5 - Domingo Masias

import pandas as pd
data_people=pd.read_excel('datos.xlsx')

# print(data_people.info())
print(data_people.head())
#1
data_people['Id']=data_people['Nombre'].astype(str).str.upper().str[0] +\
                    data_people['Nombre'].astype(str).str.upper().str[-1] +\
                    data_people['Id'].astype(str)

#2
data_people['Nombre']= data_people['Nombre'].astype(str).str.title()

#3
data_people['Profesion']=data_people['Profesion'].astype(str).str.upper()

#4
data_people['Total']= data_people['Sueldo']-data_people['Sueldo']*0.2

#5
data_people['Indice']=range(1,len(data_people)+1)

#5.1
data_people= data_people[['Indice','Id','Nombre','Profesion', 'Sueldo', 'Total']]

#Center
# data_people['Indice']=data_people['Indice'].astype(str).str.center(20)
# data_people['Id']=data_people['Id'].astype(str).str.center(20)
# data_people['Nombre']=data_people['Nombre'].astype(str).str.center(20)
# data_people['Profesion']=data_people['Profesion'].astype(str).str.center(20)
# data_people['Sueldo']=data_people['Sueldo'].astype(str).str.center(20)
# data_people['Total']=data_people['Total'].astype(str).str.center(20)

columns_to_format = ['Indice', 'Id', 'Nombre', 'Profesion', 'Sueldo', 'Total']

for col in columns_to_format:
    data_people[col] = data_people[col].astype(str).str.center(20)
    
##Create Excel
data_people.to_excel('processed_excel.xlsx', index= False)