
def saltoDivisor(m:int,k:int):
      modulo = 998244353
      DP1 = [0 for _ in range(m+1)]
      DP1[0] = 1
      DP2 = [0 for _ in range(m+1)]
      R = [0 for _ in range(m)]
      conteo = 0
      while conteo < m:
            for i in range(conteo,m+1-k):
                  DP2[i+k] = DP2[i+k] + (DP1[i]+DP2[i])%modulo
                  DP2[i+k] = DP2[i+k]%modulo
            DP1 = DP2
            DP2 = [0 for _ in range(m+1)]
            for i in range(conteo,m+1):
                  R[i-1] = R[i-1]+DP1[i]
                  R[i-1] = R[i-1]%modulo
            conteo = conteo+k
            k = k+1
      return R[m-1]


#Casos de prueba

"""
rta1 = saltoDivisor(8,1)
rta2 = saltoDivisor(10,2)
rta3 = saltoDivisor(10000,3)
rta4 = saltoDivisor(10000,7)
rta5 = saltoDivisor(200000,1) #El que mas se demora

print(rta)
"""
            
