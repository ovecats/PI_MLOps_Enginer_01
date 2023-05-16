***PROYECTO INDIVIDUAL  MLOps***

Modelo de recomendacion de peliculas

1. Resumen
2. Desarrollo
3. Fuente de Datos

#### Resumen

---

Asumiendo el rol de MLOps Enginer se creara un modelo de recomendacion para una start-up que provee servicios de agrgacion de plataformas de streamig.

Se iniciara con un ETL al csv brindado, luego se hara el desarrollo de la API con el framework fastaAPI , donde se creara 6 funciones para consumo de la API y luego se realizara un deployment con render.

El analisis de la data se llevara a cabo creando un EDA , apoyandose con librerias como PANDAS y MATPLOTLIB, luego se desarrollara la funcion para el sistema de recomendacion.

## DESARROLLO

**ETL:**

+ Algunos campos, como **`belongs_to_collection`**, **`production_companies`** y otros (ver diccionario de datos) están anidados, esto es o bien tienen un diccionario o una lista como valores en cada fila, ¡deberán desanidarlos para poder  y unirlos al dataset de nuevo hacer alguna de las consultas de la API! O bien buscar la manera de acceder a esos datos sin desanidarlos.
+ Los valores nulos de los campos **`revenue`**, **`budget`** deben ser rellenados por el número **`0`**.
+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**, además deberán crear la columna **`release_year`** donde extraerán el año de la fecha de estreno.
+ Crear la columna con el retorno de inversión, llamada **`return`** con los campos **`revenue`** y **`budget`**, dividiendo estas dos últimas **`revenue / budget`**, cuando no hay datos disponibles para calcularlo, deberá tomar el valor **`0`**.
+ Eliminar las columnas que no serán utilizadas, **`video`**,**`imdb_id`**,**`adult`**,**`original_title`**,**`vote_count`**,**`poster_path`** y **`homepage`**

**API:** usando el framework ***FastAPI***.

crear 6 funciones para los endpoints que se consumirán en la API, recuerden que deben tener un decorador por cada una (@app.get(‘/’)).

+ Cantidad de películas producidas por un determinado país en determinado año. La función debe llamarse get_country(year, country) y debe devolver sólo número de películas producidas por dicho país en dicho año.
+ Recaudacion por productora y por año. La función debe llamarse get_company_revenue(company, year) y debe devolver un int, con el total de dólares recaudados ese año por esa productora.
+ Cantidad de películas que salieron en determinado año. La función debe llamarse get_count_movies(year) y debe devolver un int, con el número total de películas que salieron ese año.
+ Película con mayor retorno en determinado año. La función debe llamarse get_return(title, year) y debe devolver sólo el string con el nombre de la película con mayor retorno de inversión en ese año.
+ Película con el menor presupuesto en determinado año. La función debe llamarse get_min_budget(year) deberia devolver el string con el nombre de la película, el año de estreno y el presupuesto, en un diccionario con las llaves llamadas 'title', 'year', 'budget' y cada una con su valor correspondiente.
+ Lista con las 5 franquicias, colleciones o series de películas que más recaudaron históricamente. La función se llamará get_collection_revenue() y debería devolver una lista de longitud 5 que contenga el nombre en string de las 5 franquicias que más recaudaron históricamente.

<br/>

**Deploy:**

se usara  [Render](https://render.com/docs/free#free-web-services) como servicio para que la API pueda ser consumida desde la web.

**EDA:**

Investigar las  relaciones que hay entre las variables de los datasets,  outliers y ver si hay algún patrón interesante que valga la pena explorar en un análisis posterior. nos apoyaremos en librerías como pandas , matplotlib para obtener algunas conclusiones.

## Sistema de recomendacion:

 consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score de similaridad y devolverá una lista de Python con 5 valores, cada uno siendo el nombre de las películas con mayor puntaje, en orden descendente.

## **Fuente de datos**

+ [Dataset](https://drive.google.com/file/d/1Rp7SNuoRnmdoQMa5LWXuK4i7W1ILblYb/view?usp=sharing): Archivo con los datos que requieren ser procesados, tengan en cuenta que hay datos que estan anidados (un diccionario o una lista como valores en la fila).
+ [Diccionario de datos](https://docs.google.com/spreadsheets/d/1QkHH5er-74Bpk122tJxy_0D49pJMIwKLurByOfmxzho/edit#gid=0): Diccionario con algunas descripciones de las columnas disponibles en el dataset.
  `<br/>`
