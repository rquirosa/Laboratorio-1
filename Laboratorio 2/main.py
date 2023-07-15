from api import *
from ids import *
import time
import asyncio


users_list=ids
def normal_process():
    for user in users_list:
        
        print(getOneUser(user))
#cree esta funcion para obtener la referencia de lo que tarda la funcion original sin optimizar

async def async_process():
               
        async for user in users_list:
            getOneUser(user)

#utilizo un for con async para recorrer la lista de ids y meterlo en el getoneuser

async1=async_process()

if __name__ == "__main__":
    start_time = time.time()

    #async_process()

    asyncio.run(async1)

    print()
    duration = time.time() - start_time
    print(f"Processed {len(users_list)} users in {duration} seconds")

#Al parecer el sistema me pide esperar algun objeto pero no pude solucionarlo, cuando corri con la linea de "asyncio.run(async1)" me dice que requiere un objeto con metodo aiter, lo cual trate de implementar pero no logre que funcionara