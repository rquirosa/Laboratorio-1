Tarea 1:

#Informacion del API utilizado:

Se utiliza el portal de datos abiertos que el Consejo Nacional de Vialidad (CONAVI) pone a disposicion en su pagina "https://conavi.opendata.junar.com/home" para obtener los datos mediante el API disponible.

El request de API luce asi: "http://conavi.cloudapi.junar.com/api/v2/datastreams/ACTIV/data.json/?auth_key=YOUR_API_KEY" 

##Condiciones para el uso del API:

CONAVI tiene varias tablas disponibles, cada una con un identificador GUID diferente, para este ejercicio se selecciono la tabla con titulo "Peajes por tipo de vehículo según mes y año", con el identificador "PEAJE-POR-TURNO".

Para utilizar el API tambien se necesita un key que ya se define en el codigo como "APIKey". En caso de que no funcione, un nuevo Key puede ser  solicitado en el siguiente link: "https://conavi.opendata.junar.com/developers/". Se debera reemplazar la variable "APIKey" con este nuevo Key para correr el request.

#Manipulacio de la respuesta obtenida:

La data venia como una lista de diccionarios, con 'results' el key donde en realidad estaban los datos que se utilizan para la tabla, aunque estos datos vienen en una sola line, en un formato similar a CSV pero que al intentar utilizar la funcion de read_CSV nativa de pandas, la terminal indicaba un error debido a la linea de datos es de tipo serie y no se puede iterar. Se necesito desarrollar una funcion que creara un diccionario a partir de los datos obtenidos del API, con lo que se crea un dataframe inicial. 
Tras obtener el error "ValueError: All arrays must be of the same length", se tuvo que agregar al codigo un paso para que modificar la longitud de los Arrays y que fueran del mismo tamaño que el array mas largo encontrado. 

Al correr el codigo, los datos se fueron agregando solamente a la ultima columna del dataframe, con el resto mostrando datos Null. Por esto se recurrio a crear un segundo dataframe en el que se transpusieran los valores de esta ultima columna ('MONTORECAUDADO') y se separara en 6 columnas diferentes, para finalmente obtener la forma de la tabla que se buscaba. 

| ANO | MES | PEAJE | VEHICULO | CANTIDAD | MONTO RECAUDADO |


#Datos a disposicion del usuario:

Se incluyen 2 funciones para explorar los datos:

1.Explorar los datos disponibles:
    1.1 Las columnas de la tabla
    1.2 Peajes disponibles para analizar
    1.3 Años que abarcan la data

2.Las primeras 10 lineas de datos de la tabla (extracto de los datos)





