def partition(vetor, leftInd, rightInd):
   i = leftInd+1
   j = rightInd
   max = vetor[leftInd]

   while i<=j:
       if max < vetor[i]:
           max = vetor[i]
       if max < vetor[j]:
           max = vetor[j]
       i += 1
       j -= 1

   return max

def largest_number(vetor, i, j):
   mid = (i+j)//2
   max1 = partition(vetor, i, mid)
   max2 = partition(vetor, mid+1, j)
   return max1 if max1 > max2 else max2

n = int(input())
vetor = []
for i in range(n):
   num = int(input())
   vetor.append(num)
print('Maior numero: ', largest_number(vetor, 0, n-1))
