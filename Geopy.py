import folium
def CadenaNueva(cadena):
    nuevaCadena=[]
    for i in cadena:
        i=i.split()
        i=[float(x) for x in i]
        i.reverse()
        nuevaCadena.append(tuple(i))
    return nuevaCadena
def coordenadas(path,G):
    contador1=0
    contador2=0
    Coordenadas=[]
    for i in range(len(path)):
        if i==len(path)-1:
            break
        elif path[i]!=path[i+1]:
            contador1+=G[path[i]][path[i+1]]['dist']
            contador2 += G[path[i]][path[i + 1]]['acoso']
            Coordenadas.extend(CadenaNueva(G[path[i]][path[i+1]]['Linestring']))
    print(contador1,' Distancia en metros')
    print(contador2/len(path), ' Riesgo de acoso')
    return Coordenadas
def crearMapa(camino,G,my_map,colour):
    Coordenadas1 = coordenadas(camino,G)
    folium.PolyLine(locations = [Coordenadas1],color=colour,
                    line_opacity = 0.5).add_to(my_map)
    return my_map
