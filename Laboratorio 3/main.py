import sys
import requests as req
import pandas as pd
import random

def ver_menu():
    print()
    print("Bienvenido a los chistes de Chuck Norris")
    print("Seleccione una de las siguientes opciones:")
    print("1=Chiste aleatorio de Chuck Norris")
    print("2=Ver las categorias disponibles de chistes")
    print("3=Salir")
    print()

menu= ["1","2","3"]

def user_input():
        choice= input("Ingrese su seleccion: ")

        if choice in menu:
            return choice
        else:
                print()
                print("Seleccion no disponible")
                print()


def chiste_aleatorio():
       URL="https://api.chucknorris.io/jokes/random"
       response= req.get(URL)
       json_dictionary= response.json()
       print()
       print("El chiste:\n")
       print(json_dictionary["value"])
       print()

def seleccion_categoria():
        print()
        query=str(input(print("Escriba la categoria deseada\n")))
        requestURL=f"https://api.chucknorris.io/jokes/search?query={query}"
        response_cat=req.get(requestURL)
        
        if response_cat == 400:
               print("La categoria no existe o no fue escrita correctamente")
        else:
            json_dictionary= response_cat.json()
            json_list=json_dictionary["result"]
            l_chistes=[d.get('value') for d in json_list]
            #cat_random=[randint(0,len(l_chistes))]              
            print()
            print("El chiste:\n")
            print(l_chistes[random.randint(0,len(l_chistes))])
            print()

def menu_categorias():
        seleccion_categoria()
        print("1=Ingresar otra categoria")
        print("2=Volver al menu principal")
        user_choice=user_input()
        
        if user_choice=="1":
                seleccion_categoria()       
        elif user_choice=="2":
                ver_menu()


def ver_categorias():
    URL_Cat="https://api.chucknorris.io/jokes/categories"
    response= req.get(URL_Cat)
    json_response= response.json()
    categoria_list= pd.DataFrame(json_response, columns=["Categorias"])
    print(categoria_list)

    seleccion_categoria()
    menu_categorias()


    


while True:
        ver_menu()
        user_choice=user_input()
        if user_choice=="1":
                chiste_aleatorio()
                
        elif user_choice=="2":
                ver_categorias()
        
        elif user_choice=="3":
                print("Adios")
                sys.exit()