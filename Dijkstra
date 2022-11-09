from Objetos import G
from Objetos import G2
from Geopy import crearMapa
import random
import folium
import sys
from Objetos import Destino
from Objetos import Origen
from Objetos import getLoc
from Objetos import getLoc2
import time
def filtrarLista(visited):
    numero= random.randint(1,len(visited)-1)
    nuevaLista=[]
    for i in range(len(visited)):
        if i%numero==0:
            nuevaLista.append(visited[i])
    return nuevaLista
def modificarCadena(cadena):
    cadena = cadena[1:-1]
    cadena = cadena.split(',')
    cadena.reverse()
    cadena = [float(x) for x in cadena]
    return cadena
def eliminarAristas(visited):
    visited=visited[1:-1]
    nuevosVisitados=[]
    for termino in visited:
        if G.degree(termino)>1:
            nuevosVisitados.append(termino)
    return nuevosVisitados
def Dikstra(actual,final,restringidos):
    visitados=dict()
    temporales=dict()
    if actual not in G.nodes() or final not in G.nodes():
        print('Los nodos no se encuentran en el archivo')
        return None
    temporales[actual] = 0
    distancia=0
    inicio=actual
    while actual!=final:
        visitados[actual]=distancia
        for i in list(G.neighbors(actual)):
            if i not in visitados and i not in restringidos:
                if i not in temporales or temporales[i]> distancia+G[actual][i]['weight']:
                    temporales[i]=distancia+G[actual][i]['weight']
        try:
            temporales.pop(actual)
        except:
            temporales[actual]=sys.maxsize
        distancia=sys.maxsize
        for termino,valor in temporales.items():
            if valor<distancia:
                distancia=valor
                actual=termino
        if distancia == sys.maxsize:
            return distancia
    del temporales
    return hallarRuta(visitados,final,[],inicio,distancia)
def hallarRuta(visitados,actual,ruta,inicio,distancia):
    ruta.append(actual)
    if actual==inicio:
        ruta.reverse()
        return ruta
    for i in list(G2.neighbors(actual)):
        try:
            if actual in G.neighbors(i) and round(abs(distancia-G[i][actual]['weight']),2)==round(visitados[i],2):
                ruta.append(i)
                return hallarRuta(visitados,i,ruta,inicio,distancia-G[i][actual]['weight'])
        except:
            continue
    return "El algoritmo no funcionó"
visitados=dict()
temporales=dict()
inicio=Origen
final=Destino
my_map3 = folium.Map(location=modificarCadena(inicio),
                         zoom_start=15)
folium.Marker(modificarCadena(inicio),
popup = f'Origen: {getLoc.address}').add_to(my_map3)
folium.Marker(modificarCadena(final),
              popup=f'Destino: {getLoc2.address}').add_to(my_map3)
print('.')
camino1=Dikstra(inicio,final,[])
if type(camino1) is not list:
    print('No pudimos hallar un camino para los puntos indicados')
    sys.exit()
my_map3=crearMapa(camino1,G,my_map3,'blue')
camino2=Dikstra(inicio,final,eliminarAristas(camino1[len(camino1)//2:]))
limite1=0
limite2=0
if camino2==sys.maxsize or camino2==camino1:
    while camino2==sys.maxsize or camino2==camino1:
        if limite2==1000:
            camino2=camino1
            break
        camino2=Dikstra(inicio,final,eliminarAristas(filtrarLista(camino1)))
        limite2+=1
my_map3=crearMapa(camino2,G,my_map3,'gray')
camino3 = Dikstra(inicio, final, eliminarAristas(camino1))
if camino3==sys.maxsize or camino3==camino1 or camino3==camino2 or type(camino3):
    while camino3==sys.maxsize or camino3==camino1 or camino3==camino2:
        if limite1==1000:
            camino3=camino2
            break
        camino3 = Dikstra(inicio, final, eliminarAristas(filtrarLista(camino1)))
        limite1+=1
my_map3=crearMapa(camino3,G,my_map3,'purple')
print('Ya puedes revisar el mapa :)')
my_map3.save(r"C:\Users\PC\OneDrive - Universidad EAFIT\Algoritmos\Proyecto\Código\map1.html")
