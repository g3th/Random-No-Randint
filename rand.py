import time

print("\x1bc")

end = int(input('Random range: (1-5 Numbers)'))
start = 10

while True:
	a = str(time.time_ns())[start:start+end]
	#print(len(a), end)
	if '0' in a[0]:
		pass
	else:
		break
		
print('Random Number:', int(a))
