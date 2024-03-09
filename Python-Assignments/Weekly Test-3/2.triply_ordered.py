from base_program import generate_dictionary

def step_1_2(l1,l2):
    dic1={}
    for i in enumerate(l2):
        if i[1] not in dic1:
            dic1[i[1]] = [l1[i[0]]] #step 2
        else:
            dic1[i[1]].append(l1[i[0]])
    
    print("step1:",dic1)
    return dic1

def step_3(dic):
    dic2 = {}
    for i,j in dic.items():
        dic2[len(j)] = {}
    dic2 = dict(sorted(dic2.items()))

    for i,j in dic.items():
        dic2[len(j)][i]=j
    
    print("step2:",dic2)
    return dic2

def triply(dic):
    print("\n================================")
    print("input:",dic)
    l1 = list(dic.keys())
    l2 = list(dic.values())
    res1 = step_1_2(l1,l2)
    res2 = step_3(res1)
    print('step3:',res2)


# # Driver Code
inputs = [(0,11), (12, 38), (0,6), (20,11), (50,15), (34,56)]

for i in inputs:
    dic = generate_dictionary(i[0],i[1])
    triply(dic)

print("")
triply({1: 5, 2: 6, 3: 5, 4: 5, 5: 6, 6: 7, 7: 1, 9: 6})
print("")
triply({2:7, 3:11, 4:10, 5:10, 7:2, 9:5, 10:10, 11:5})