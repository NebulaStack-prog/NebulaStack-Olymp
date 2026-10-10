n = int(input())
a = []
count =  0
par = 0
for i in range(n):
	a.append(int(input()))
	
a.sort()

for i in range(n):
	if a[i] % 2 == 0:
		for l in range(i + 1, n):
			if a[l] % 2 == 0:
				par += 1
				k = (a[i] + a[l])/2
				left = 0
				right = n - 1
				bool = True
				while right - left > -1:
					j = a[(left+right)//2]
					if j == k:
						count += 1 
						break
					else:
						if j > k:
							right = (left+right)//2 - 1 
						else:
							left = (left+right)//2 + 1 
							
print("Совпадений " + str(count))
print("Пар четных чисел " + str(par))
