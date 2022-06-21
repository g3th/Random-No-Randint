import time

print("\x1bc")

end = int(input('Random range: (1-5 Numbers)'))
start = 10

while True:
	n = time.time_ns()
	a = str(time.time_ns())[start:start+end]
	#print(len(a), end)
	if '0' in a[0]:
		pass
	else:
		break

print(n)
print('Random Number:', int(a))
