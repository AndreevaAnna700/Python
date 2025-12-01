volume = 1.44
pages = 100
lines = 50
symbols = 25
code = 4

Normal = (pages * lines * symbols * code) / (1024 * 1024)

Real = volume // Normal
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", int(Real))
