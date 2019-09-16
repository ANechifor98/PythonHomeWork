import sys
N = int(sys.argv[1])

connect = sys.stdin.readlines()
file = [x.strip() for x in connect]


#row results
row = 0
for line in file:
   count = 0
   for char in line:
      if char == "x":
         count += 1
      else:
         count = 0
      if count == N:
         row += 1
         count = 0

#column results
column = 0
for i in range(len(file[0])):
   count = 0
   for j in range(len(file)):
      char = file[j][i]
      if char == "x":
         count += 1
      else:
         count = 0
      if count == N:
         column += 1
         count = 0

#diagonal results
diagonal = 0			
for i in range(-len(file), len(file[0])):
   count = 0
   for j in range(len(file)):
      if i < 0:
         i += 1
         continue
      char = file[j][i]
      if char == "x":
         count += 1
      else:
         count = 0
      if count == N:
         diagonal += 1
         count = 0
      if i < len(file[0])-1:
         i += 1
      else:
         break			

#reverse diagonal results         
reverse_diagonal = 0			
for j in range(len(file)+len(file[0])):
   count = 0
   for i in range(len(file[0])):
      if j >= len(file):
         j -= 1
         continue
      char = file[j][i]
      if char == "x":
         count += 1
      else:
         count = 0
      if count == N:
         reverse_diagonal += 1
         count = 0
      if j > 0:
         j -= 1
      else:
         break			
						
total = row + column + diagonal + reverse_diagonal
print(total)