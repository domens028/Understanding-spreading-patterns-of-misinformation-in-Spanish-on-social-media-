import graph,Bertopic,dataClean,dataAnalisys,dataCreation
import pandas as pd 
#extraemos la información de los json y la tabulamos
#data = dataCreation.CreateData()
data = pd.read_csv('dataset.csv')
#limpiamos los datos
print('comenzamos limpieza')
clean = dataClean.clean(data)
print('Acabamos limpieza')
#llamamos a los analisis 
print('comenzamos analisis')
dataAnalisys.AnalisisDeDireccionabilidad(clean)
dataAnalisys.TwitterAnalisis(clean)
dataAnalisys.printTables(clean)
dataAnalisys.printTablesLan(clean)
print('Acabamos analisis')
print('bertopic')
Bertopic.analisis()
print('Graph')
graph.printGraph()



