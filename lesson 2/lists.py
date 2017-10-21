lst1 = [x for x in input().split()]
lst2 = [x for x in input().split()]

# используя множество - поддерживаем уникальность элементов
result = set()

for elem in lst1:
	for elem2 in lst2:
		if elem == elem2:
			result.add(elem)
			break

print (*result)
