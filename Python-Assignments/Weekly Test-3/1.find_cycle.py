from base_program import generate_dictionary

def findCycle(dic):
    print(dic)
    final_list = []
    for i,j in dic.items():
        l1 = [i]
        if i!=j:
            for k in range(len(dic)-1):
                try:
                    l1.append(j)
                    j = dic.get(j)
                    if j == i:
                        l1 = sorted(l1)
                        if l1 not in final_list:
                            final_list.append(l1)
                        break
                except:
                    pass
        else:
            final_list.append(l1)
    print(final_list,end='\n')
        

inputs = [(0,11), (12, 38), (0,6), (20,11), (50,15), (34,56)]

for i in inputs:
    dic = generate_dictionary(i[0],i[1])
    findCycle(dic)

print("")
findCycle({1: 5, 2: 6, 3: 5, 4: 5, 5: 6, 6: 7, 7: 1, 9: 6})
print("")
findCycle({2:7, 3:11, 4:10, 5:10, 7:2, 9:5, 10:10, 11:5})
            

