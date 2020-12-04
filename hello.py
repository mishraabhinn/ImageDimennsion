a = list(map(chr, range(97, 123)))
A = list(map(chr, range(65, 90)))

for _ in range(int(input()))

	
	n,k=map(int,input().split())
	s=input()
	capital=0;
	lower=0
	for i in s:
		if i in A:
			capital+=1
		else:
			lower+=1
	if(capital<=k && lower<=k):
		print("both")
	elif capital<=k and lower>k:
		print("chef")
	elif capital>k and lower<=k:
		print("brother")
	else:
		print("none")

