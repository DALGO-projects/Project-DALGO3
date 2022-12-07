

def saltoDivisor(m:int,k:int):
      #Inicializar listas
      lista = [0 for _ in range(m+1)]
      totals = [0 for _ in range(m+1)]
      modulo = 998244353

      for i in range(m//k):
            lista[(i+1)*k] = lista[(i+1)*k] + 1
            totals[(i+1)*k] = totals[(i+1)*k] + 1
      
      sum = 2*k + 1

      while sum <= m:
            actual = [0 for _ in range(m+1)]
            k = k+1
            for i in range(k,m+1):
                  actual[i] = (actual[i-k]+totals[i-k])%modulo
                  lista[i] = (actual[i]+lista[i])%modulo
            totals = actual
            sum = sum + k
      
      longitud = len(lista)

      return lista


lista = saltoDivisor(25252,11)
print(lista)


            
