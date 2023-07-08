from trig import *
import datetime
import sys


def ver_menu():
    print()
    print("Bienvenido a trigonometria de Pi")
    print("Seleccione una de las siguientes operaciones:")
    print("1=Seno")
    print("2=Coseno")
    print("3=Tangente")
    print("4=Salir")
    print()

menu= ["1","2","3","4"]  

def user_input():
        choice= input("Ingrese una opcion: ")

        if choice in menu:
            return choice
        else:
                print()
                print("Opcion no disponible")
                print()


instance1= trig()
file1=trig()
current_time=datetime.datetime.now()

def sen():
        print("----------------------------------")
        informacion=f"El seno de Pi es igual a= {instance1.seno()}"
        file1.guardar(current_time,informacion)
        print(informacion)

def cos():
        print("----------------------------------")
        informacion=f"El coseno de Pi es igual a= {instance1.coseno()}"
        file1.guardar(current_time,informacion)
        print(informacion)

def tan():
        print("----------------------------------")
        informacion=f"La tangente de Pi es igual a= {instance1.tangente()}"
        file1.guardar(current_time,informacion)
        print(informacion)



while True:
        ver_menu()
        user_choice=user_input()
        if user_choice=="1":
                sen()
                
        elif user_choice=="2":
                cos()
                
        
        elif user_choice=="3":
                tan()
                
        elif user_choice=="4":
                print("Adios")
                sys.exit()
