from random import randint, sample


numbers = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

weights = [randint(1, 711)]
weights.append(randint(1, 712 - weights[0]))
weights.append(randint(1, 713 - weights[0] - weights[1]))

points = sample(range(1, 8), 3)
already = list()

while sum(weights) != 0:
	print(*points, '←for cheating')
	
	check_points = input('Write 3 numbers in range 1-7: ').split()
	
	print("\033[H\033[J", end='')
	
	if [i in '1234567'  for i in check_points] == [True, True, True]:
		for i in range(3):
			check_points[i] = int(check_points[i])
	
	else:
		print('Invalid syntax')
		continue
	
	for i in range(3):
		if check_points[i] == points[i] and weights[i] != 0 :
				weights[i] = 0
				print(f'Now, check {numbers[check_points[i] - 1]} km')
				
	points = sample(range(1, 8), 3)
