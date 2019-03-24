from multiprocessing.connection import Client
import random

c = Client(('localhost', 6163))


for _ in range(50):
	c.send({
		'type': 'MESH',
		'verts': [
			(random.random(), random.random(), random.random()) for _ in range(3)
		],
		'faces': [
			(0, 1, 2)
		]
	})
