for i in range(10, 0, -1):
    print(i)
print('-------------------------------------------------------------------')

list_0 = list(range(10))
print('List_0: ', list_0, type(list_0))
print('-------------------------------------------------------------------')

print('1: ', list_0[5:7])
print('-----------')

print('2: ', list_0[5:])
print('-----------')

print('3: ', list_0[:-1])
print('-----------')

print('4: ', list_0[5:-1])
print('-----------')

print('5: ', list_0[5:-3])
print('-----------')

print('6: ', list_0[:8:2])
print('-----------')

print('7: ', list_0[-1:0:-1])  # -1 beginning of list; 0 ending of list; -1 step upon list
print('-----------')

print('8: ', list_0[-1::-1])  # -1 beginning of list; :: ending of list; -1 step upon list
print('-------------------------------------------------------------------')

list_1 = list(range(10))
print('List_1: ', list_1, type(list_1), id(list_1))

list_2 = list_1[:]  # The same function what list_1.copy()
print('List_2: ', list_2, type(list_2), id(list_2))
print('-------------------------------------------------------------------')

# Lab

