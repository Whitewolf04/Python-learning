def fact(num):
    ending = num+1
    factorlist = []
    for factor in range(1, ending):
        if num%factor == 0:
            factorlist.append(factor)
        else:
            pass
    return factorlist

def generator():
    triangle_list = []
    item = 0
    for num in range(1, 1000000):
        item += num
        triangle_list.append(item)
    return triangle_list

for so in generator():
    if len(fact(so)) > 200:
        print(so)
        break
    else:
        continue
