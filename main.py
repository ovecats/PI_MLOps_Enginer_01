from fastapi import FastAPI
import pandas as pd
import numpy as np
from typing import List
from typing import Dict

app = FastAPI()


#http://127.0.0.1:8000

df = pd.read_csv('MD_DATA.csv')
df['release_date'] = pd.to_datetime(df['release_date'], format='%Y-%m-%d')



@app.get('/')
def index():
    return 'BIENVENIDOS API_DATA'



@app.get('/peliculas_mes/{mes}')
def peliculas_mes(mes:str):
    df = pd.read_csv('MD_DATA.csv')
    mes = mes.capitalize()
    '''Se ingresa el mes y la funcion retorna la cantidad de peliculas que se estrenaron ese mes historicamente'''
    cantidad = len(df.loc[df['month'] == mes, 'title'])
    return {'mes':mes.lower(), 'cantidad':cantidad}
    


@app.get('/peliculas_dis/{dis}')
def peliculas_dia(dia:str):
    dia = dia.capitalize()
    cantidad = len(df.loc[df['weekday'] == dia, 'title'])
    return {'dia':dia, 'cantidad':cantidad}


@app.get('/franquicia/{franquicia}')
def franquicia(franquicia:str):
    cantidad_peliculas = (df[df['belongs_to_collection'] == franquicia]).shape[0]
    df_presupuesto = (df[df['belongs_to_collection'] == franquicia])['budget']
    df_ingresos = (df[df['belongs_to_collection'] == franquicia])['revenue']
    ganancia_total = df_ingresos.sum() - df_presupuesto.sum()
    ganancia_promedio = ganancia_total/cantidad_peliculas
    return{'franquicia':franquicia , 'cantidad':cantidad_peliculas, 'ganancia_total':ganancia_total, 'ganancia_promedio':ganancia_promedio}


@app.get('/peliculas_pais/{pais}')
def peliculas_pais(pais): 
    pais = pais.title()
    cantidad = 0
    lista = df["production_countries"]
    for i in range(len(lista)):
        if lista[i] is None:
            continue
        if type(lista[i]) is not list and lista[i] == pais:
            cantidad += 1
        if pais in lista[i]:
            cantidad += 1
    return {'pais':pais, 'cantidad':cantidad}


@app.get('/productoras/{productora}')
def productoras(productora:str):
    prod = df[['production_companies', 'budget', 'revenue']].dropna()
    prod ['production_companies'] = prod['production_companies'].map(str.lower)
    cantidad = prod.shape[0]
    gtotal= (prod['revenue'] - prod['budget']).sum()
    return {'productora':productora, 'ganancia_total': gtotal, 'cantidad': cantidad }


@app.get('/retorno/{pelicula}')
def retorno(pelicula:str) -> dict:
    '''Ingresas la pelicula, retornando la inversion, la ganancia, el retorno y el año en el que se lanzo'''
    pelicula_df = df.loc[df['title'] == pelicula]
    inversion = pelicula_df['budget'].sum()
    ganancia = pelicula_df['revenue'].sum()-pelicula_df['budget'].sum()
    retorno = pelicula_df['return'].sum()
    anio = pelicula_df['release_year'].values[0]
    return {'pelicula':pelicula, 'inversion':inversion, 'ganacia':ganancia,'retorno':retorno, 'anio':anio}


@app.get('/recomendacion/{titulo}')
def recomendacion(titulo:str):
    '''Ingresas un nombre de pelicula y te recomienda las similares en una lista'''
    return {'lista recomendada': respuesta}