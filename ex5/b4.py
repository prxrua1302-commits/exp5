import matplotlib.pyplot as plt

cities = ['LA', 'San Diego', 'San Jose', 'SF', 'Fresno',
          'Sacramento', 'Long Beach', 'Oakland', 'Bakersfield', 'Anaheim']

areas = [1302, 964, 469, 121, 298, 259, 132, 202, 388, 131]


cities, areas = zip(*sorted(zip(cities, areas), key=lambda x: x[1], reverse=True))


plt.barh(cities, areas)

plt.title("Top 10 thành phố lớn nhất California (diện tích)")
plt.xlabel("Diện tích (km²)")
plt.ylabel("Thành phố")

plt.show()