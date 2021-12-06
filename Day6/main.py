from pathlib import Path
import os
import sys
from collections import defaultdict, Counter

def part1(filename):
	infile = sys.argv[1] if len(sys.argv) > 1 else filename
	L = []
	for line in open(infile):
		Str = line.replace('\n','')
		tempL = Str.split(',')
		for _ in tempL:
			L.append(int(_))	
	print(L)
	day = 1
	while day <= 80:
		for k,v in enumerate(L):
			L[k] = v - 1
			if v == 0:
				L[k] = 6
				L.append(9)
		day += 1
	print("part1: ",len(L))

def part2(filename):


	infile = sys.argv[1] if len(sys.argv) > 1 else filename
	X = Counter([int(x) for x in open(infile).read().strip().split(',')])

	def solve(S, n):
		X = S
		for day in range(n):
			Y = defaultdict(int)
			for x, cnt in X.items():
				if x == 0:
					Y[6] += cnt
					Y[8] += cnt
				else:
					Y[x - 1] += cnt
			X = Y
		return sum(X.values())

	print(solve(X, 80))
	print(solve(X, 256))

if __name__ == '__main__':
	script_dir = os.path.dirname(os.path.abspath(__file__))
	input_file = Path(script_dir, '.', 'puzzleInput.in')
	test_input_file = Path(script_dir, '.', 'testInput.in')
	# part1(input_file)
	part2(input_file)
