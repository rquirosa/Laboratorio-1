from apicall import *
import sys


API_URL="http://conavi.cloudapi.junar.com/api/v2/datastreams/PEAJE-POR-TURNO/data.json/?auth_key="


df=APIcall.get_data(API_URL)



def ver_menu():
    print()
    print("Conexion a la base de datos de Peajes del CONAVI\n")
    print("Seleccione una de las siguientes opciones:\n")
    print("1=Ver informacion general de los datos")
    print("2=Ver grafico de barras del monto recaudado por peaje")
    print("3=Ver grafico de barras del monto recaudado por peaje")
    print("4=Ver grafico de barras del monto recaudado por peaje")
    print("5=Salir")
    print()

menu= ["1","2","3","4","5"]  

def user_input():
            choice= input("Ingrese una opcion: ")

            if choice in menu:
                return choice
            else:
                    print()
                    print("Opcion no disponible")
                    print()
while True:
        ver_menu()
        user_choice=user_input()
        if user_choice=="1":
                print()

                print(APIcall.informacion_general(df))
                print("--------------------------------------------------------------------------------------------------")
                
        elif user_choice=="2":
                print("Grafico de barras:\n")
                APIcall.grafico_barra(df)
                print("--------------------------------------------------------------------------------------------------")
       
        elif user_choice=="3":
                print("Grafico de linea:\n")
                APIcall.grafico_line(df)
                print("--------------------------------------------------------------------------------------------------")        
        
        elif user_choice=="4":
                print("Grafico de pie:\n")
                APIcall.grafico_pie(df)
                print("--------------------------------------------------------------------------------------------------")
        
        elif user_choice=="5":
                print("Adios")
                sys.exit()