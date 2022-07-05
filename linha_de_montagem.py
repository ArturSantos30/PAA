def print_path(T1, T2, n):
   for i in range(n):
       if T1[i] < T2[i]:
           print(f"Linha 1, estacao {i+1}, custo {T1[i]}")
       else:
           print(f"Linha 2, estacao {i+1}, custo {T2[i]}")
 
def linha_de_montagem (a, t, e, x):
   NUM_STATION = len(a[0])
   T1 = [0 for i in range(NUM_STATION)]
   T2 = [0 for i in range(NUM_STATION)]
  
   T1[0] = e[0] + a[0][0]
   T2[0] = e[1] + a[1][0]
 
   for i in range(1, NUM_STATION):
       T1[i] = min(T1[i-1] + a[0][i],
                   T2[i-1] + t[1][i] + a[0][i])
       T2[i] = min(T2[i-1] + a[1][i],
                   T1[i-1] + t[0][i] + a[1][i] )
 
   T1.append(T1[NUM_STATION - 1] + x[0])
   T2.append(T2[NUM_STATION - 1] + x[1])
 
   print_path(T1, T2, NUM_STATION+1)
 
a = [[4, 5, 3, 2],
   [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
   [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]
 
linha_de_montagem(a, t, e, x)