#!/usr/bin/python3
import scipy.optimize
from math import ceil

def compute(V, init = 10):
	if V == [1]*len(V):
		return len(V)
	if len(V) <= 1:
		return
	def h(x):
		return sum([x**(-v) for v in V])-1
	X = scipy.optimize.brenth(h,1, init)
	return X

def Ceil(x):
	return ceil(x*1000)/1000

def print_bv(V):
	V = sorted(V)
	R = [f"{i}x{V.count(i)}" for i in range(1, max(V)+1)]
	return ','.join(R)

def check(L, S):
	for X in L:
		if X.issubset(S):
			return True
	return False

def combine_two(F1, F2):
	A = [[] for x in range(20)]
	for x0 in F1:
		for y0 in F2:
			x = set(x0)
			y = set(y0)
			z = x.union(y)
			A[len(z)].append(z)
	L = []
	V = []
	for k in range(len(A)):
		for S in A[k]:
			if check(L, S):
				continue
			L.append(set(S))
			V.append(k)
	return L, V

max_BN = 0

def combine(X):
	global max_BN
	L = X[0]
	for F in X[1:]:
		L,V = combine_two(L, F)
	BN = Ceil(compute(V))
	Lp = ['{'+','.join([Names[x] for x in sorted(S)])+'}' for S in L]
	out = ','.join(Lp)
	if len(out) > 70:
		out = out[:70-3]+"..."
	print(f"{out:70} {BN:.3f} {print_bv(V)}")
	max_BN = max(max_BN, BN)

def Map(S, f):
	return [[f[x] for x in L] for L in S]

def case(L, f0, label2 = ""):
	f = f0[:]

	label = []
	for x,y in L:
		f[f.index(x)] = y
		label.append(f"{Names[x]}={Names[y]}")
	if label2 != "":
		print(f"{label2}",end=" ")
	else:
		label = ','.join(label)
		if label != "":
			print(f"{label:20}",end=" ")
	return f

# The sets F_i represent the sets F_i(a,b_1,b_2,b_3) from Lemma 7,
# where i is the number of the case.
# The vertices a,b_1,b_2,b_3 are represented by 0,1,2,3, respectively.
# The vertices of N(b_i)\{a} are represented by 2i+2 and 2i+3 (if |N(b_i)\{a}| > 1)

F_2 = [[0], [1], [6], [8], [2,3], [4,5]]
F_3 = [[0], [1], [2], [8], [4,5], [6,7]]
F_6 = [[0], [1], [2], [8], [4,5]]
F_4 = [[0], [1], [2], [3], [4,5], [6,7], [8,9]]
F_8 = [[0], [1], [2], [3], [4,5], [6,7]]
F_9 = [[0], [1], [2], [3], [4,5]]

Names = ["a", "b1", "b2", "b3", "c1", "c2", "c3", "c4", "c5", "c6", 
		 "a'", "b'1", "b'2", "b'3", "c'1", "c'2", "c'3", "c'4", "c'5", "c'6",
		 "a''", "b''1", "b''2", "b''3", "c''1", "c''2", "c''3", "c''4", "c''5", "c''6",
		 "a'''", "b'''1", "b'''2", "b'''3", "c'''1", "c'''2", "c'''3", "c'''4", "c'''5", "c'''6"
]
f0 = [1,0,4,5,2,3,16,17,18,19]
f2 = [2,0,6,7,1,3,26,27,28,29]
f3 = [3,0,8,9,1,2,36,37,38,39]

######################################################################
print("Rule 6")
print("i,j = 1,1")
F1 = F_2

f = case([(16,6)], f0)
F2 = Map(F_2, f)
C1 = [[0],[1],[4],[6],[2]]
combine([F1,F2,C1])

f = case([(16,6),(18,8)], f0)
F2 = Map(F_2, f)
C2 = [[0],[1],[5],[8],[3]]
combine([F1,F2,C1,C2])

######################################################################

print()
print("i,j = 1,2")
F1 = F_2

f = case([(16,6)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[6],[2]]
combine([F1,F2,C1])

f = case([(18,6)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[5],[6],[2]]
combine([F1,F2,C1])

f = case([(16,6),(17,8)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
combine([F1,F2,C1,C2])

f = case([(16,6),(18,8)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[5],[8],[3]]
combine([F1,F2,C1,C2])

######################################################################

print()
print("i,j = 1,3")
F1 = F_2

f = case([(16,6)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
combine([F1,F2,C1])

f = case([(16,6),(17,8)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
combine([F1,F2,C1,C2])

f = case([(16,6),(18,8)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[5],[8],[3]]
combine([F1,F2,C1,C2])

######################################################################

print()
print("i,j = 2,2")
F1 = F_3

f = case([(16,6)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[6],[2]]
combine([F1,F2,C1])

f = case([(16,8)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[8],[3]]
combine([F1,F2,C1])

f = case([(18,6)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[5],[6],[2]]
combine([F1,F2,C1])

f = case([(18,8)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[5],[8],[3]]
combine([F1,F2,C1])

##
f = case([(16,6),(17,8)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
combine([F1,F2,C1,C2])

f = case([(16,6),(18,7)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[5],[7],[2]]
combine([F1,F2,C1,C2])

f = case([(16,6),(18,8)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[5],[8],[3]]
combine([F1,F2,C1,C2])

f = case([(16,8),(18,6)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[8],[3]]
C2 = [[0],[1],[5],[6],[2]]
combine([F1,F2,C1,C2])

##

f = case([(16,6),(17,8),(18,7)], f0)
F2 = Map(F_3, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
C3 = [[0],[1],[5],[7],[2]]
combine([F1,F2,C1,C2,C3])

######################################################################

print()
print("i,j = 2,3")
F1 = F_3

f = case([(16,6)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
combine([F1,F2,C1])

f = case([(16,8)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[8],[3]]
combine([F1,F2,C1])

##

f = case([(16,6),(17,8)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
combine([F1,F2,C1,C2])

f = case([(16,6),(18,7)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[5],[7],[2]]
combine([F1,F2,C1,C2])

f = case([(16,6),(18,8)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[5],[8],[3]]
combine([F1,F2,C1,C2])

##

f = case([(16,6),(17,8),(18,7)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
C3 = [[0],[1],[5],[7],[2]]
combine([F1,F2,C1,C2,C3])

######################################################################

print()
print("i,j = 3,3")
F1 = F_4

f = case([(16,6)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
combine([F1,F2,C1])

##
f = case([(16,6),(17,8)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
combine([F1,F2,C1,C2])

f = case([(16,6),(18,7)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[5],[7],[2]]
combine([F1,F2,C1,C2])

f = case([(16,6),(18,8)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[5],[8],[3]]
combine([F1,F2,C1,C2])

## 

f = case([(16,6),(17,8),(18,7)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
C3 = [[0],[1],[5],[7],[2]]
combine([F1,F2,C1,C2,C3])

##

f = case([(16,6),(17,8),(18,7),(19,9)], f0)
F2 = Map(F_4, f)
C1 = [[0],[1],[4],[6],[2]]
C2 = [[0],[1],[4],[8],[3]]
C3 = [[0],[1],[5],[7],[2]]
C4 = [[0],[1],[5],[9],[3]]
combine([F1,F2,C1,C2,C3,C4])

print(f"Max BN = {max_BN}")
######################################################################

print()
print("Rule 7")
max_BN = 0
F1 = F_2

f = case([], f0, "i,j=1,1")
F2 = Map(F_2, f)
combine([F1,F2])

f = case([], f0, "i,j=1,2")
F2 = Map(F_3, f)
combine([F1,F2])

f = case([], f0, "i,j=1,3")
F2 = Map(F_4, f)
combine([F1,F2])

F1 = F_3

f = case([], f0, "i,j=2,2")
F2 = Map(F_3, f)
combine([F1,F2])

print(f"Max BN = {max_BN}")

######################################################################

print()
print("Rule 8")
	
F1 = F_6
	
f = case([], f0)
F2 = Map(F_4, f)
combine([F1,F2])

######################################################################

print()
print("Rule 9")
	
F1 = F_3
	
f = case([], f0)
F2 = Map(F_4, f)
F3 = Map(F_4, f2)
combine([F1,F2,F3])

######################################################################

print()
print("Rule 10")

F1 = F_9

case([], f0)
F2 = Map(F_8, f0)
combine([F1,F2])

######################################################################

print()
print("Rule 11")

F1 = F_8
case([], f0)
F2 = Map(F_4, f0)
F3 = Map(F_4, f2)
combine([F1,F2,F3])

######################################################################

print()
print("Rule 12")

F1 = F_4
case([], f0)
F2 = Map(F_4, f0)
F3 = Map(F_4, f2)
F4 = Map(F_4, f3)
combine([F1,F2,F3,F4])

######################################################################

F_000 = [[0], [4], [6], [8]]
F_001 = [[0], [4], [6], [3]]
F_010 = [[0], [4], [2], [8]]
F_011 = [[0], [4], [2], [3]]
F_100 = [[0], [1], [6], [8]]
F_101 = [[0], [1], [6], [3]]
F_110 = [[0], [1], [2], [8]]
F_111 = [[0], [1], [2], [3]]

F_list = [F_000, F_001, F_010, F_011, F_100, F_101, F_110, F_111]
case_list = ["000", "001", "010", "011", "100", "101", "110", "111"]

f0 = [4,1,12,13,0,5,16,17,18,19]
C1 = [[0],[1],[4],[12],[6],[2]]

print()
print("Rule 15")
max_BN = 0

L = []
for j in range(8):
	for i in range(j+1):
		if F_list[i][0] == F_list[j][0]:
			L.append((i,j))

# For each vertex x from b_1,b_2,b_3,b'_1,b'_2,b'_3, either deg(x) = 2 or deg(x) >= 3
# (note that b'_1 does not appear in the list above since b'_1 = b_1).
# therefore, there are 2^5 cases to consider.
# The string case1 defines the degrees of b_1,b_2,b_3 (deg(b_i) = 2 iff case1[i-1]=0) and
# The string case2 defines the degrees of b'_1,b'_2,b'_3.
# Due to symmetry, the list L only contains pairs i,j with i <= j
# In fact, we can even take L = [(0,0),(3,0),(4,4),(4+3,4)] for the first case
# and L = [(0,0),(2,0),(3,0),(4,4),(4+2,4),(4+3,4)] for the second case

# First case: there is no path of length 4 between a,a' that passes through b_3 and b'_3.
for i,j in L:
	case1 = case_list[i]
	case2 = case_list[j]
	F1 = F_list[i]
	F2_base = F_list[j]
	f = case([(16,6)], f0, case1+"/"+case2)
	F2 = Map(F2_base, f)
	combine([F1,F2,C1])

print()

# Second case: there is a path of length 4 between a,a' that passes through b_3 and b'_3.
for i,j in L:
	case1 = case_list[i]
	case2 = case_list[j]
	F1 = F_list[i]
	F2_base = F_list[j]
	f = case([(16,6),(18,8)], f0, case1+"/"+case2)
	F2 = Map(F2_base, f)
	combine([F1,F2,C1])

print(f"Max BN = {max_BN}")
