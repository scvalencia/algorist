import operator

def generate(seed):
	seed = str(seed)
	dct = {}
	current_tuple = (0, seed[0])
	dct[current_tuple[0]] = current_tuple[1]

	i = 0
	while i < len(seed):

		if seed[i] != current_tuple[1]:
			current_tuple = (i, seed[i])
			dct[current_tuple[0]] = current_tuple[1]

		i += 1

	ans = ''

	indexes = dct.keys()
	indexes.append(len(seed))

	for i, itm in enumerate(indexes):
		if itm in dct:
			char = dct[itm]
			factor = indexes[i + 1] - itm
			ans += str(factor) + str(char)

	return ans

def perform_sequence(bound):

	i = 0
	ans = 1
	while i < bound:		
		print ans
		print
		ans = generate(ans)
		i += 1

perform_sequence(30)