my_dict={'Ivan':19,'Danil':24,'Michael':55}
print(my_dict ['Ivan'])
print(my_dict.get('Andrew', 'Нет такого ключа'))
my_dict.update({'Peter': 33,
                'Mark': 12})
print(my_dict)
a = my_dict.pop('Peter')
print(a)
print(my_dict)

my_set={1,1,34.12,'Roman','Roman', True}
print(my_set)
my_set.add(5)
my_set.add('Jack')
print(my_set)
my_set.discard('Roman')
print(my_set)