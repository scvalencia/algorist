anagrams = [('heart', 'earth'), ('python', 'typhon')]

def anagram1(s1, s2):
	alist = list(s2)

	pos1 = 0
	still_ok = True

	while pos1 < len(s1) and still_ok:
		pos2 = 0
		found = False

		while pos2 < len(s2) and not found:
			if s1[pos1] == s2[pos2]:
				found = True
			else:
				pos2 = pos2 + 1

		if found:
			alist[pos2] = None
		else:
			still_ok = False

		pos1 = pos1 + 1

	return still_ok

def anagram2(s1, s2):
	list1 = list(s1)
	list2 = list(s2)

	list1.sort()
	list2.sort()

	pos = 0
	matches = True

	while pos < len(s1) and matches:
		if list1[pos] == list2[pos]:
			pos = pos + 1

		else:
			matches = False

	return matches

def anagram3(s1, s2):
	c1 = [0 for _ in range(26)]
	c2 = [0 for _ in range(26)]

	for i in range(len(s1)):
		pos = ord(s1[i]) - ord('a')
		c1[pos] += c1[pos] + 1
		pos = ord(s2[i]) - ord('a')
		c2[pos] += c2[pos] + 1

	j = 0
	still_ok = True

	while j < len(c1) and still_ok:
		if c1[j] == c2[j]:
			j += 1
		else:
			still_ok = False

	return still_ok


def main():
	for a, b in anagrams:
		print anagram1(a, b)
		print anagram2(a, b)
		print anagram3(a, b)


if __name__ == '__main__':
	main()