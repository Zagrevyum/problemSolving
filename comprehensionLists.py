A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i,i**3] for i in A1]
A8 = [00,30]
A7 = [[a+b] for a in range(24) for b in A8]

print(A2, A3, A4, A5, A6)

print(A7)


interval_dict = {(str(a)+":"+str(b)): 0 for a in range(24) for b in range(0,60,30)}

print(interval_dict)