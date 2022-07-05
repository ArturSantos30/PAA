from itertools import permutations

def valido(vetor, coluna):
   for i in range(coluna):
       if (vetor[i] == vetor[coluna]) or (abs(vetor[i]-vetor[coluna]) == abs(i-coluna)):
           return False
   return True

n = int(input())
vetor = [i for i in range(n)]
perm = permutations(vetor)

for j in list(perm):
   v = list(j)
   if any(valido(v, i) for i in v):
       print(v)
