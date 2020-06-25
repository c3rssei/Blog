---
title: Descubrir tu data (Conceptos)
categories: librerias,preprocesado,estadistica
published: true
---

# [](#header-1) Descripcion
Los datos estan construidos por data objects. un data object representa una entidad, en una base de datos medica, los objetos pueden ser pacientes, tambien se conocen como muestras, ejemplos, instancias o objetos. Por ende una fila de una base de datos corresponde a un data object.

Referencias:

[Visualizaciones de datos con Python](https://relopezbriega.github.io/blog/2016/09/18/visualizaciones-de-datos-con-python/).
https://www.ingeniovirtual.com/tipos-de-graficos-y-diagramas-para-la-visualizacion-de-datos/
https://infogram.com/es/pagina/elige-el-grafico-correcto-visualizacion-datos
https://bookdown.org/aquintela/EBE/variables-continuas.html
https://blog.adrianistan.eu/estadistica-python-pandas-numpy-scipy-parte-i


## [](#header-2) Atributos




Un atributo es un campo de dato, que representa una caracteristica de una muestra, por ejemplo teniendo como muestra un cliente un posible atributo seria el nombre, telefono y asi...



### [](#header-3) Atributos Nominales

Nominal significa **relativo a nombres**, los valores de un atributo nominal son simbolos o nombres de cosas, cada valor representa algun tipo de categoria, por ejemplo el color de pelo, estado civil..

Los atributos nominales tambien pueden ser representados con numeros, por ejemplo el id de un respectivo cliente


### [](#header-3) Atributos Ordinales

Un atributo ordinal corresponde a un atributo con un posible sentido de orden o ranking, por ejemplo la talla de ropa que va de xs,s,m,l,xl ....

### [](#header-3) Atributos Continuos

Aquellos atributos que son continuos son aquellos que se pueden medir, como por ejemplo la temperatura, la humedad...

La distribucion que siguen los atributos continuos pueden ser uniforme, normal, exponencial

### [](#header-3) Atributos Discretos

Los atributos discretos son aquellos que se pueden contar teniendo en cuenta un numero finito de cantidades, por ejemplo los años, cantidad de hijos...


## [](#header-2) Medición de la tendencia central




### [](#header-3) Promedio

la medida mas comun y efectiva para el centro de un conjunto de datos es el promedio.



Lo cual corresponde a la sumatoria de los elementos dividos en la cantidad de elementos.

El promedio si bien es bastante util, es muy sensible a valores extremos, incluso una pequeña cantidad de datos extremos pueden corromper el promedio. Las cifras de un conjunto de datos que son extremadamente altas o extremadamente bajas en comparación con el resto de las cifras se llaman valores atípicos. Debido a la forma de hacer los cálculos, los valores atípicos altos tienden a subir o bajar la media

Para esto se puede calcular **La media Truncada** lo cual se refiere a remover los valores extremos, por ejemplo podemos quitar del el 2% del top y del bottom de la data.

```python
import numpy as np
np.mean(data)
```


### [](#header-3) Mediana

Para valores asimetricos la mejor medida del centro de los datos es la **Mediana** 
La mediana corresponde a el valor medio de una lista de valores ordenados, dejando la misma cantidad de valores a un lado que al otro, la mediana entonces corresponde al valor que separa la parte mas alta de un grafico de la parte mas baja.

Lo mas importante para el calculo de la mediana es que los datos este ordenados de manera ascendente o descendente. 

Si el conjunto de datos contiene un número impar de cifras, elige la que esté exactamente en el centro. Ésa es la mediana.

Si el conjunto de datos contiene un número par de cifras, coge las dos del centro y calcula la media para obtener la mediana.

```python
import numpy as np
np.median(data)
```



### [](#header-3) Moda

La moda es el valor que mas se repite dentro del conjunto de datos. a diferencia de la media no se ve afectada por valores atipicos al igual que la mediana.
```python
import numpy as np
import scipy.stats as stats

stats.mode(data)
```


## [](#header-2) Desviacion

La desviacion es una medicion que indica que tan dispersos son los datos, o que tan alejados estan de la media,

"La desviación estándar puede ser difícil de interpretar como número aislado. Básicamente, una desviación estándar pequeña significa que la mayoría de los valores del conjunto de datos están próximos a la media de ese conjunto, y una desviación estándar grande significa que la mayoría de los valores del conjunto de datos están más alejados de la media". (Estadisticas para dummies)

```python
import numpy as np
import scipy.stats as stats

np.std(data)
```


### [](#header-3) Representacion grafica 

La representacion grafica de las variables variara segun lo que se quiera observar:
1. Comparacion: el objetivo es comparar atributos, puede ser un grafico de barras o puntos.
2. Relaciones: Comprender la relacion entre dos o mas atributos. Para determinar si existe un patron entre dos variables numericas.
3. Composicion : Comprender como se compone una variable, diagrama de torta o e barras
4. Distribucion: Esta categoria permite observar como se distribuyen los datos. Suele utilizarse en la exploracion de los datos, el tipo de grafico dependera a que tipo de variable corresponda el atributo, ya sea cuantitativo o cualitativo.


Los atributos categoricos pueden ser representados por un grafico de sectores o Torta, los cuales son para observar la composicion del atributo, lo ideal es que sean pocas categoricas para que sea mas claro.

Tambien se debe considerar el tipo de variable al escoger el grafico.


#### [](#header-4) Relaciones

Segun la ayuda de eleccion de graficos, las relaciones son mediante graficos de dispersion o de burbujas.

entre las dos variables continuas del conjunto

Ejemplo :
Precio vs Puntos.


#### [](#header-4) Distribucion

Los gráficos de distribución/histogramas se usan para conocer la frecuencia de los como valores de una variable y responden a preguntas del estilo:

**¿Número de clientes qué tengo por grupo de edad? ¿Cuántos días tardan nuestros pagos?**

Si la representación es de una única variable y son pocos los datos que hay se utiliza gráficos de barras (Bar histogram). Por ejemplo: Número de habitantes por Comunidad Autónoma.

Si la representación es de una única variable y hay muchos datos se utilizan gráfico lineales (Line histogram).

Si se quiere representar dos variables hay varias opciones como utilizar gráfico de Scatter plot o de barras con distinto color o varios gráficos.
Extraido de --> [analitica-de-datos-con-python-y-sofia2-14-graficos-de-distribucion](https://about.sofia2.com/2017/09/04/analitica-de-datos-con-python-y-sofia2-14-graficos-de-distribucion/).

1
#### [](#header-4) Comparacion

A traves del tiempo o entre categorias.

En este tipo de graficos se utiliza principalmente el grafico de barras, **es necesario que al menos uno de los ejes sea numerico**


#### [](#header-4) Histogramas

si la variable es numerica entonces es llamado histograma, la variable x esta dento de rangos, lo usual es que los rangos sean iguales, dentro de cada rango se despliega la barra con la cantidad de observaciones en ese rango.

```python
plt.figure(figsize = (12,8)) # Tamaño de la figura
data[data["Precio"]<200]["Precio"].plot.hist()
```
idem sns.distplot()


#### [](#header-4) Boxplot

los graficos de tipo boxplot permiten **Visualizar una variable numerica**, utila valores **Cuartiles**,**Extremos**,**valores raros o outiers**


#### [](#header-4) Pivot Table

Similar a las tablas temporales de sql, permite seleccionar ciertos atributos del conjunto de datos, agrupa en base a un indice mediante el parametro **index**, a su vez pueden mostrar estimadores estadisticos ya sea promedio o un conjunto de estos.

1. pd.pivot_table(index=["Atributo","Atributo2","Atributo n"])
2. pd.pivot_table(index,values="Atributo",aggfunc=["mean",np.median])

a su vez la tabla generada permite hacerle un query

tab.query("Variedad ==['Agiorgitiko']")


#### [](#header-4) Catplot

Catplot es un tipo de grafico de dispersion categorica.

