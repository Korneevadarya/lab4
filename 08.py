#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
# garden_set =
# meadow_set =
# TODO здесь ваш код
garden_set = set(garden)
meadow_set = set(meadow)
sett = garden_set | meadow_set

# выведите на консоль все виды цветов
# TODO здесь ваш код
print(sett)
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
mett = garden_set & meadow_set
print(mett)
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
dett = garden_set - meadow_set
print(dett)
# выведите на консоль те, которые растут на лугу, но не растут в саду
# TODO здесь ваш код
qett = meadow_set - garden_set
print(qett)