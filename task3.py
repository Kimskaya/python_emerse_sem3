'''Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав
его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака'''

tonnage = 19500
things = {'палатка': 5000, 'спальник': 4500, 'вода': 4000, 'еда': 3500,
          'одежда': 2000,'термос': 1500, 'мангал': 1000}



def loading(Dict_things,max_weight):
    '''Функция возвращает список, содержащий вложенные списки -
    все возможные варианты комплектации рюкзака.
    Последний элемент вложенных списков - общий вес комплектации'''
    
    def load_rec(bp_weight,backpack,remains_things):
        '''функция принимает вес комплектации bp_weight,
        комплектацию - список backpack, список оставшихся вещей - remains_things.
        Если комплектация помещается в рюкзак, то она добавляется в список result'''
        if bp_weight<=max_weight:
            result.append(backpack+[bp_weight])
        for i in range(len(remains_things)):
            bp = backpack + [remains_things[i][0]]
            weight = bp_weight + remains_things[i][1]
            rem_things = remains_things[i+1:]
            load_rec(weight,bp,rem_things)

    result = []
    #В функцию load_rec передаётся отсортированный по значению по убыванию
    #список кортежей "ключ-значение" исходного словаря 
    load_rec(0,[],sorted(Dict_things.items(),key=lambda x:x[1],reverse=True))
    return result

#Сортируем результат работы функции loading по весу (последний элемент) по убыванию 
variants = sorted(loading(things,tonnage),key = lambda x:x[-1],reverse=True)[:-1]
print('Лучший вариант:')    #Первый элемент в отсортированном списке
print(*variants[0][:-1],sep = ', ',end = '. ')
print(f'Всего - {variants[0][-1]}г')    #Остальные варианты в порядке убывания
print('Все варианты:')
for variant in variants:
    print(*variant[:-1],sep = ', ',end = '. ')
    print(f'Всего - {variant[-1]}г')