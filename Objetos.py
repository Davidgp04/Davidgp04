import math
import networkx as nx
import pandas as pd
import sys
from geopy.geocoders import Nominatim
def modificarCadena(cadena):
    cadena = cadena[1:-1]
    cadena = cadena.split(',')
    cadena.reverse()
    cadena = [float(x) for x in cadena]
    return cadena
loc = Nominatim(user_agent="GetLoc")
final=input('Adónde quieres ir\n')
inicio=input('Ingrese el punto de salida\n')
getLoc = loc.geocode(inicio)
getLoc2=loc.geocode(final)
Cinicio=[getLoc.latitude,getLoc.longitude]
Cfinal=[getLoc2.latitude,getLoc2.longitude]
print('Estamos tratando de calcular su ruta .',end='')
df=pd.read_csv('calles_de_medellin_con_acoso.csv', sep=';')
df['harassmentRisk'].fillna(df['harassmentRisk'].mean(),inplace=True)
G=nx.DiGraph()
G2=nx.Graph()
G.add_nodes_from(list(df['origin']))
G2.add_nodes_from(list(df['origin']))
distanciaMinima=sys.maxsize
distanciaMinima2=sys.maxsize
Origen=[]
Destino=[]
for j in range(df['length'].size):
    Inicio=modificarCadena(df['origin'][j])
    Final=modificarCadena(df['destination'][j])
    if math.sqrt(math.pow((Cinicio[0]-Inicio[0]),2)+math.pow((Cinicio[1]-Inicio[1]),2))<distanciaMinima:
        distanciaMinima=math.sqrt(math.pow((Cinicio[0]-Inicio[0]),2)+math.pow((Cinicio[1]-Inicio[1]),2))
        Origen=f'({Inicio[1]}, {Inicio[0]})'
    if math.sqrt(math.pow((Cfinal[0]-Final[0]),2)+math.pow((Cfinal[1]-Final[1]),2))<distanciaMinima2:
        distanciaMinima2=math.sqrt(math.pow((Cfinal[0]-Final[0]),2)+math.pow((Cfinal[1]-Final[1]),2))
        Destino = f'({Final[1]}, {Final[0]})'
    G.add_edge(df['origin'][j],df['destination'][j])
    G2.add_edge(df['origin'][j],df['destination'][j])
    weight = math.sqrt((math.pow(df['length'][j], 2) + math.pow(df['harassmentRisk'][j] * 100, 2)))
    weight = round(weight, 2)
    G.edges[df['origin'][j],df['destination'][j]]['weight']=weight
    G.edges[df['origin'][j], df['destination'][j]]['dist'] = df['length'][j]
    G.edges[df['origin'][j], df['destination'][j]]['acoso'] = df['harassmentRisk'][j]
    Linestring=df['geometry'][j]
    Linestring = Linestring[12:-1]
    Linestring = Linestring.split(',')
    G.edges[df['origin'][j],df['destination'][j]]['Linestring']=Linestring
    G2.edges[df['origin'][j], df['destination'][j]]['weight'] = weight
print('.',end='')
