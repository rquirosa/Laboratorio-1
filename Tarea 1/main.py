import requests
import pandas as pd
import sys

def ver_menu():
    print()
    print("Conexion a la base de datos de Peajes del CONAVI\n")
    print("Seleccione una de las siguientes opciones:\n")
    print("1=Explorar los datos disponibles")
    print("2=Ver extracto de los datos")
    print("3=Salir")
    print()

menu= ["1","2","3"]  

def user_input():
        choice= input("Ingrese una opcion: ")

        if choice in menu:
            return choice
        else:
                print()
                print("Opcion no disponible")
                print()


API_URL="http://conavi.cloudapi.junar.com/api/v2/datastreams/PEAJE-POR-TURNO/data.json/?auth_key="
def get_data(API_URL):
    APIKey="trUalyfPNnk23xq7NQI18Wvg9zjrqDjxaKMumbqz"
    response= requests.get(API_URL+APIKey, verify=False)
    json_file=response.json()


    if response.status_code == 200:
        api_response = {
        'result': {
            'fLength': 7245,
            'fType': 'ARRAY',
            'fTimestamp': 1691357604599,
            'fArray': json_file['result']['fArray']  # Extracting 'fArray' from the API response
        }
    }

        # Creating an empty dictionary to store the data
        data_dict = {}

        # Iterate through the 'fArray' values to fill the empty dictionary, sepparating Headers from the actual data
        for item in api_response['result']['fArray']:
            if 'fHeader' in item:
                current_header = item['fStr'] if 'fStr' in item else None
                if current_header:
                    data_dict[current_header] = [] #list of headers
            #only interested in the values pairing to the keys "fStr" and "fNum"
            elif 'fStr' in item:
                if current_header in data_dict:
                    data_dict[current_header].append(item['fStr'])
            elif 'fNum' in item:
                if current_header in data_dict:
                    data_dict[current_header].append(item['fNum'])

        # Check if all arrays have the same length
        array_lengths = {key: len(value) for key, value in data_dict.items()}
        if len(set(array_lengths.values())) > 1:
            # Find the maximum common length for all columns
            max_common_length = max(array_lengths.values())

            # Fix columns to make them of the same length
            for key, value in data_dict.items():
                data_dict[key] = value[:max_common_length] if len(value) > max_common_length else value + [None] * (max_common_length - len(value))

        # Pandas DataFrame from the dictionary
        df = pd.DataFrame(data_dict)

        # Data listed under 'Monto recaudado' and is not being appended under each column, have to work around this issue

        #Preparing to create new dataframe
        actual_values = df['MONTORECAUDADO']

        # Transpose the values into different rows with 6 columns each
        num_columns = 6
        num_rows = len(actual_values) // num_columns
        transposed_list = [actual_values[i*num_columns:(i+1)*num_columns].values for i in range(num_rows)]

        # Create a new DataFrame, listing the column names again
        new_df = pd.DataFrame(transposed_list, columns=['ANO', 'MES', 'PEAJE', 'VEHICULO', 'CANTIDAD', 'MONTO RECAUDADO'])

        return new_df

        # Check new DataFrame
        #print()

    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

df=get_data(API_URL)

def show_data(df):
    print("El archivo contiene las siguientes columnas:")
    for cols in df.columns:
        print(cols)
    print()
    print("Se tienen datos de los siguientes peajes:")
    for peajes in df['PEAJE'].unique():
        print(peajes)
    print()
    print(f"Los datos abarcan desde el: {min(df['ANO'])} hasta el {max(df['ANO'])}")
    print()


while True:
        ver_menu()
        user_choice=user_input()
        if user_choice=="1":
                show_data(df)
                print("--------------------------------------------------------------------------------------------------")
                
        elif user_choice=="2":
                print("A continuacion se muestran las primeras 10 filas de datos disponibles\n")
                print(df.head(11))
                print("--------------------------------------------------------------------------------------------------")
                
        elif user_choice=="3":
                print("Adios")
                sys.exit()
