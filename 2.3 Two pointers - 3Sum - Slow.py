test1 = [-1,0,1,2,-1,-4]
test2 = [0,1,1]

def three_sum(my_list):
    result = []
    for i in range(len(my_list)):
        for j in range(i + 1,len(my_list)):
            for k in range(j + 1,len(my_list)):
                if my_list[i] + my_list[j] + my_list[k] == 0 and (my_list[i] != my_list[j] != my_list[k]):
                    result.append([my_list[i], my_list[j], my_list[k]])
    return result


print(three_sum(test1))
