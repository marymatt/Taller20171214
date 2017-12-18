# Instrucciones

## Prerequisitos:

#### Herramientas
**Python 2.7:**
Ingresar en  la carpeta donde se encuentre instalado python  en mi caso es C:\Python27. Descargar  el archivo get-pip  del enlace https://bootstrap.pypa.io/get-pip.py dentro.

  1.  Abrir la consola  y poner

               cd C:\Python27

  2.  Para descargar PIP debe ejecutar

                 python.exe get-pip.py

  3.  Editar las variables de entorno en Path y poner

           C:\Python27 y C:\Python27\Scripts

**Librerias**

 1. Tweepy

           pip install tweepy

 2. Paquete de seguridad

           pip install requests[security]

 3. pattern

            pip install pattern

 4. Nltk

           pip install nltk

 5. Sklearn

           pip install sklearn
 6. Numpy

           pip install numpy

 7. Scipy

            pip install scipy

#### Otros
 1. Cuenta en Twitter
 2. Descargar la carpeta  TallerUPV

## Descripción:
Este taller está dividido en dos partes.
En la primera parte nos centraremos en el proceso de **descarga de tweets** usando la libreria Tweepy y en la segunda parte abordaremos el proceso de **clasificación de los tweets** que hemos descargados, usando  el corpus de entrenamiento generado en el caso de estudio "Analisis de contenido de comunicación ciudadana".

## Parte 1: DescargaTweet
Pasos para obtener las credenciales en Twitter

1.	Ingresar al link https://apps.twitter.com/
2.	Click en **Create New App**
3.	Llenar los datos y dar click en **Create your Twitter application**
4.	En la ventana que aparece dar clik en la pestaña **Keys and Access Tokens**
5.	Una vez allí, dar click en  **Create my Access token**
6.	Finalmente tiene todo lo necesario para poder comenzar a trabajar. Los datos a tener en cuenta son:  **Consumer Key (API Key)**,
**Consumer Secret (API Secret)**,
**Access Token** y **Access Token Secret** .


Pasos para poner en funcionamiento el código descargado.

1. Editar el archivo **credencialesTwitter.py** y agregarle las credenciales que generamos en el punto anterior.
2. Ejecutar el archivo **DescargaTwitt.py**
3. El producto final del punto anterior es un archivo llamado **dataTweets.json**.
4. Se pueden cambiar las cuentas de las que queremos descargar la información, agregandolas en el archivo **cuentas.csv**, luego se ejecuta el archivo **DescargaTwitt.py**

## Parte 2: Clasificación

Pasos para poner en funcionamiento el código descargado.

1. Asegurarse que en la carpeta **DescargaTweet** se encuentre el archivo **dataTweets.json** generardo en la parte 1 del taller
2. Dentro de la carpeta **Clasificacion** se encuentra el archivo **ClasificacionTaller.py** que debemos ejecutar.
3. El producto final del punto anterior es un archivo llamado **TweetsClasificados.json**.

**Nota:** El taller se realizó con python 2.7 y con las librerias mencionadas en el apartado herramientas. Si durante el proceso de ejecución del código fuente le indica error en las stopwords debe descomentariar la linea de código.

    #nltk.download('stopwords')
    #nltk.download('punkt')

Que se encuentra en el código **normalizacion.py** dentro de la carpeta **clasificacion**.

Si muestra un Warnig sobre la librería sklearning se debe a que el clasificador (archivo.pickle) se generó en una versión anterior.
