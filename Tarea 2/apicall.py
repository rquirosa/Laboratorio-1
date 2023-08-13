import requests
import pandas as pd
import matplotlib.pyplot as plt

class APIcall:
     



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
    
    def informacion_general(df):
        print()

        #Encontrando maximos por peaje
        df2=df.groupby('PEAJE')['MONTO RECAUDADO'].max()
        df2=df2.sort_values()

        #Encontrando maximos por vehiculo

        df3=df.groupby('VEHICULO')['MONTO RECAUDADO'].max()
        df3=df3.sort_values()

        #Encontrando maximos por año
        df4=df.groupby('ANO')['MONTO RECAUDADO'].max()
        df4=df4.sort_values()

        df5=df['MONTO RECAUDADO'].mean()

        print("El tipo de vehiculo con mayor monto recaudado es:\n")
        print(df3)
        print("El Peaje con mayor monto recaudado es:\n")
        print(df2)
        print("El año con mayor monto recaudado es:\n")
        print(df4)
        print("El monto promedio recaudado al dia de hoy es de:\n")
        print(df5.round(1))


    def grafico_barra(df):
        
        #Diseño de grafico de barras
        df2=df.groupby('PEAJE')['MONTO RECAUDADO'].max()
        df2=df2.sort_values()
        df2=df2.tolist()

        peajes_list=df['PEAJE'].unique()

        fig, ax = plt.subplots()

        bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

        ax.bar(peajes_list, df2, label=peajes_list, color=bar_colors)

        ax.set_ylabel('Monto')
        ax.set_title('Peajes')
        ax.legend(title='Peajes por monto recaudado')
        def addlabels(peajes_list,df2):
            for i in range(len(peajes_list)):
                plt.text(i,df2[i],df2[i])
        
        addlabels(peajes_list,df2)
        plt.show()

    
    def grafico_line(df):
        #Diseño de grafico de linea

        line_chart=df.groupby('ANO')['MONTO RECAUDADO'].max()
        line_chart.plot.line()
        plt.title("Monto total recaudado por año")
        plt.xlabel("Año")
        plt.ylabel("Monto (colones)")
        
        plt.show()

    def grafico_pie(df):
         #Diseño de Pie chart

        pie_df=df.groupby('MES')['MONTO RECAUDADO'].max()
        pie_df=pie_df.iloc[0:5]
        pie_df.plot(kind='pie', y='',autopct='%1.0f%%')
        plt.title("Monto recaudado entre los 5 meses mas activos")

        plt.show()





