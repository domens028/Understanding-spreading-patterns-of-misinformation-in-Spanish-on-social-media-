import networkx as nx
import pandas as pd
import random
import csv
import json
import matplotlib.pyplot as plt

#leemos el dataframe 



def GraphCreation():
    fila_anterior = None 
    contador = 0
    conexion = {}
    edges = {}
    valor_anterior = 0
    df = pd.read_csv('data_clean.csv')
    pivot_table = df.pivot_table(index = ["url","date"], columns =["channel"], values = "id", aggfunc = "count")
    
    
    #Creamos el Graph
    G = nx.Graph()
    for row_label, row in pivot_table.iterrows():
        # Obtenemos una lista de todas las claves del diccionario
        claves = list(conexion.keys())
        # Recorremos la lista de claves con un bucle for anidado
        for i in range(len(claves)):
            for j in range(i+1, len(claves)):
                valor_enlace = conexion[claves[i]] + conexion[claves[j]]
                edges[(claves[i],claves[j])] = valor_enlace
                G.add_edges_from([(claves[i],claves[j], {'weight': valor_enlace})])       
        conexion = {}
                
        for col_label in pivot_table.columns:
            G.add_node(col_label)
            valor = pivot_table.loc[row_label, col_label]
            if fila_anterior == row_label:
                if(valor > 3):
                    
                    conexion[col_label] = valor

            else:
                fila_anterior = row_label
                
    nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
    # Escribir el diccionario en un archivo JSON
    node_dict = {node: i for i, node in enumerate(G.nodes)}
    with open('GraphNodes.csv', 'w') as f:
        for key in node_dict.keys():
            f.write("%s,%s\n"%(key,node_dict[key]))
    
    return G

def printAdjacencyMatrix(G):
    # print the adjacency list
    for line in nx.generate_adjlist(G):
        print(line)
    # write edgelist to grid.edgelist
    nx.write_edgelist(G, path="grid.edgelist", delimiter=":")
    
def printGraph():  
    
    G = GraphCreation()  
    # Obtener el layout inicial utilizando el algoritmo de Fruchterman-Reingold
    pos = nx.circular_layout(G, scale=10)
    
    # Crear un diccionario que asocie nombres de nodos con números enteros
    node_dict = {node: i for i, node in enumerate(G.nodes)}

    # Obtener los nodos que no tienen conexiones
    isolated_nodes = [node for node in G.nodes if len(list(G.neighbors(node))) == 0]

    # Dibujar nodos con conexiones en verde y nodos aislados en amarillo
    node_color = ["#9acd32" if node not in isolated_nodes else "yellow" for node in G.nodes]
    nx.draw_networkx_nodes(G, pos=pos, node_size=350, node_color=node_color, alpha=0.8)

    # Obtener los pesos de las aristas
    edge_weights = nx.get_edge_attributes(G, "weight")

    # Dibujar las aristas con el ancho de línea ajustado al peso
    nx.draw_networkx_edges(G, pos=pos, width=[w * 0.1 for w in edge_weights.values()], alpha=0.5, edge_color="gray")

    # Agregar etiquetas de nodos
    nx.draw_networkx_labels(G, pos=pos, labels=node_dict, font_size=8, font_weight="bold")


    # Ajustar límites y guardar figura
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("grafo_optimizado.png", dpi=300)
    plt.show()
    
    
printGraph()