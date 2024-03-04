#Squares each value in a list. 

def list_updater(lst):
    upd_list = []
    for elem in lst:
        elem **= 2
        upd_list.append(elem)
    return upd_list

stuff = [1, 2, 3, 4, 5]
print(list_updater(stuff))
