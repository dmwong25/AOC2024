with open("day1/day1_input.txt", "r") as file:
  input_data = file.readlines()
  
# columns to lists
a = []
b = []
for line in input_data:
  a.append(int(line.split()[0].strip()))
  b.append(int(line.split()[1].strip()))
  
a.sort()
b.sort()
sum = 0
k = 0
for i in range(len(a)):
    count  = 0
    while a[i] >= b[k]:
        if a[i] == b[k]:
            count += 1
        k += 1
        if k >= len(b):
            break
    sum += a[i] * count
    if k >= len(b):
            break
    

print(sum)