import time

print("\x1bc")

end = int(input('Random range: (1-5 Numbers)'))
start = 13

while True:
	a = str(time.time())[start:start+end]
	#print(len(a), end)
	if len(a) < end:
		pass
	else:
		break

print('Random Number:', int(a))
