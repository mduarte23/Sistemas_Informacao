import heapq

lista = []
#insere elemento
heapq.heappush(lista, (1/5, "Gerson"))
heapq.heappush(lista, (1/7, "Clodoaldo"))
heapq.heappush(lista, (1/1, "Cleonilson"))
heapq.heappush(lista, (1/3, "Tiburcio"))

print ("Atendimento")
for i in range (4):
    elemento = heapq.heappop(lista)
    print (elemento)
    input ('proximo')
