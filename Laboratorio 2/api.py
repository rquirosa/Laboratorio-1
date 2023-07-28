import requests as req

URL= "https://jsonplaceholder.typicode.com/users/"

def getOneUser(id): 
    response = req.get(URL)
    print(response.json()[id]["name"])
    return response.json()[id]


async def get_user_async(session,id):
    async with session.get(URL) as response:
        jsonRes = await response.json()
        print(jsonRes[id]["name"])