#!/usr/bin/env python
# encoding: utf-8
import tweepy
import sys,os
import json

from datetime import datetime
from archivocsv import leer_archivo
from credencialesTwitter import *

#Carga cuentas desde donde descargar Tweets ------------------------------------
dafile="cuentas.csv"
datafileCuentas = os.path.join(dafile)
Listaconsulta=leer_archivo(datafileCuentas) #Lista de las cuentas o hastags de twitter que deseamos descargar


#Llaves del API de Twitter -----------------------------------------------------
consumer_key,consumer_secret,access_token_key,access_token_secret=credenciales()

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #Autenticar
auth.set_access_token(access_token_key, access_token_secret) #Autenticar

api = tweepy.API(auth) #Autenticandonos en la api, para poder hacer uso de ella

# Descarga de Tweets cuenta a cuenta
today=str(datetime.now())


for searchQuery in Listaconsulta:
    maxTweets = 100 # Número de tweets que deseamos descargar
    tweetsPerQry = 100
    # Si los resultados de un ID específico en adelante son reqd, defina since_id a ese ID
    # Si no se pone, por defecto será el limite inferior al que puede llegar la API
    sinceId = None
    # Si solo hay resultado para un ID específico definir max_id con ese ID.
    # Si no se pone limite superior será el tweet mas reciente que coincida con la búsqueda
    max_id = -1L
    tweetCount = 0


    tweetsJson = []

    print searchQuery
    print "Descarga max " ,maxTweets, " tweets"
    while tweetCount < maxTweets:#Mientras que el número de descargas sea menor al número maximo de descargas
        try:
            if (max_id <= 0): #
                if (not sinceId):#si no ponemos límite inferior
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry)#la consulta se realiza sin el parámetro sinceID
                else: #si  ponemos límite inferior
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                                since_id=sinceId)#la consulta se realiza con el parámetro sinceID
            else: # Si el Max_id es mayor que 0
                if (not sinceId): #la consulta se realiza con el parámetro max_id
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                                max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId)
            if not new_tweets:
                print(" No se han encontrado mas tweets")
                break

            #######################################################################################


            for tweet in new_tweets:

                if (not tweet.retweeted) and ('RT @' not in tweet.text):
                    #Crear Objeto
                    tweetdb={
                        "idt":str(tweet.id),
                        "consulta":searchQuery,
                        "tweet":tweet.text.encode('utf-8'),
                        "fecha_creacion":str(tweet.created_at),
                        "idioma":tweet.lang,
                        "dispositivo":tweet.source,
                        "userid":tweet.user.id,
                        "username":tweet.user.screen_name,
                        "userSeguidores":tweet.user.followers_count,
                        "fechaTweet":today
                        };
                    tweetsJson.append(tweetdb)


                        #############################################################333

            tweetCount += len(new_tweets)
            #print ("no repetido", count)

            max_id = new_tweets[-1].id
        except tweepy.TweepError:
            time.sleep(60*15)
            continue
        except IOError:
            time.sleep(60*5)
            continue
        except StopIteration:
            break

    print "Descargado",len(tweetsJson), "tweets"
with open('dataTweets.json', 'w') as outfile:
    json.dump(tweetsJson, outfile)
