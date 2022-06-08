import unittest

def merge_sort(a):
	if len(a) < 2:
		return a[:]
	else:
		median = int(len(a) / 2)
		left = merge_sort(a[:median])
		right = merge_sort(a[median:])
		return merge(left, right)

def merge(left, right):
	res = []
	i, j = 0, 0
	while i < len(left) and j < len(right):
		if left[i] < right[j]:
			res.append(left[i])
			i += 1
		else:
			res.append(right[j])
			j += 1
	while i < len(left):
		res.append(left[i])
		i += 1
	while j < len(right):
		res.append(right[j])
		j += 1
	return res

# def insertion_sort(m):
# 	for i in range(1, len(m)):
# 		temp = m[i]
# 		j = i - 1
# 		while (j >= 0 and temp < m[j]):
# 			m[j + 1] = m[j]
# 			j = j - 1
# 		m[j + 1] = temp
# 	return m 


class TestMergeSort(unittest.TestCase):

	def test1(self):
		a = [1, 23, 45, 11, 15, 16, 8, 6, 65, 24]
		# self.assertEqual(merge_sort(a),insertion_sort(a))
		b = sorted(a)
		self.assertEqual(merge_sort(a), b)

	def test2(self):
		a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
		b = sorted(a)
		self.assertEqual(merge_sort(a), b)

	def test3(self):
		a = [1, 1000, 10, 10000, 100, 1000000, 999, 700]
		b = sorted(a)
		self.assertEqual(merge_sort(a), b)

if __name__ == '__main__':
    unittest.main()
