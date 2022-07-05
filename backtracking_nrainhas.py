def valido(vetor, coluna):
   for i in range(coluna):
       if (vetor[i] == vetor[coluna]) or (abs(vetor[i]-vetor[coluna]) == abs(i-coluna)):
           return False
   return True

def nrainhas(vetor_solucao, ind_coluna, n):
   print(vetor_solucao)
   sucesso = False
   if ind_coluna > n-1:
       return False
   vetor_solucao[ind_coluna] = -1
   while not sucesso and vetor_solucao[ind_coluna] < n-1:
       vetor_solucao[ind_coluna] = vetor_solucao[ind_coluna]+1
       if valido(vetor_solucao, ind_coluna):
           if ind_coluna != n-1:
               sucesso = nrainhas(vetor_solucao, ind_coluna+1, n)
           else:
               sucesso = True
   return sucesso

n = int(input())
vetor_rainhas = [-1 for i in range(n)]
print(vetor_rainhas)
nrainhas(vetor_rainhas, 0, n)
print(vetor_rainhas)
