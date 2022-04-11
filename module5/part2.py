import json
class Model:
	title = '1'
	text = '2'
	author = '3'

	def save(self):
		attr_names = list(filter(lambda x: not x.startswith('_'), dir(self)))
		d = {}
		attr_names.remove('save')
		for i in attr_names:
			d[i] = eval('self.' + i)
		with open('file.json', 'w') as f:
			json.dump(d, f)
		return print(d)

m = Model()
m.save()