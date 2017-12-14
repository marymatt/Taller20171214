#!/usr/bin/env python
# encoding: utf-8

import sys, os, io
import json
import cPickle as pickle
from normalizacion import *
from tweetsToText import convNumToNom


#  DAO Entrada
def leer():
    idt=[]
    tweet=[]
    with open('../DescargaTweet/dataTweets.json') as file:
        data = json.load(file)
    for texto in data:
        idt.append(str(texto['idt']))
        tweet.append(str(texto['tweet'].encode('utf-8')))
    if len(idt)>0:
        return idt,tweet
    else:
        return -1, -1
# Fin DAO Entrada

# Vectorizador
def transformar(textos, nombre):
    textosNormalizados = normalizar_corpus(textos)
    vectorizador = leer_Pickle('vectorizer_'+ nombre +'.pickle')
    data = vectorizador.transform(textosNormalizados)
    data = data.toarray()

    return data
#  fin Vectorizador

# procesopickle
def leer_Pickle(parametro):
    datafile = os.path.abspath(parametro)
    fichero = file(datafile)
    variable = pickle.load(fichero)
    return variable
#fin procesopickle


#DAO Salida
def escribirClasificados(corpus,puntaje,clases,idt):
    tweetsJson = []
    for i in range(len(corpus)):
        lista= sorted(zip(puntaje[i],  clases), reverse=True)
        categoria=convNumToNom(lista[0][1])
        #y_pred.append(lista[0][1])#lista de las categorias predicas, acertadas y erradas
        tweetdb={
            "categoria":categoria.decode('utf-8'),
            #"puntaje":lista[0][0],
            #"idt":idt[i], #1
            "texto":corpus[i].decode('utf-8')
            };
        try:
            tweetsJson.append(tweetdb)
        except:
                print "No se pudo guardar"
    print 'Han sido clasificados ',len(corpus),'tweets'

    with open('TweetsClasificados.json', 'w') as outfile:
        json.dump(tweetsJson, outfile)
#Fin DAO Escritura
# BLL
def generar_clasificacion():
    print "Comienza el proceso de clasificación...".decode('utf-8')

    #1--------------------cargar el corpus-------------------
    idt,corpus=leer()

    if idt!=-1:#validación del método leer, por si no hay registros
        #CONSULTAR EN BASE DE DATOS EL NOMBRE DEL CLASIFICADOR (DAO)
        nombre="MaryPr"
        if nombre!=-1:#validación de vacio
            tfidf=transformar(corpus,nombre)
            SGDtfidf=leer_Pickle(nombre +'.pickle')

            print 'Se ha usado el vectorizador....'
            clases=SGDtfidf.classes_ #generando las clases

            puntaje=SGDtfidf.decision_function(tfidf) #generando puntajes
            print 'Se ha usado el clasificador....'
            #4--------------------Guardar  en db Clasificador-------------------

            escribirClasificados(corpus,puntaje,clases,idt)
#Fin BLL
generar_clasificacion()
