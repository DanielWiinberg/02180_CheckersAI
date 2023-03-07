
s_3 = [4, 1]
s_4 = [8, 5]

s_5 = [1, 2]
s_6 = [7, 6]


s_1 = [s_3, s_4]
s_2 = [s_5, s_6]

s_init = [s_1, s_2]


def recursive_loop(nodes, depth, depth_limit):
    max_or_min_values = []
    for node in nodes:
        if  depth < depth_limit:
            depth +=1
            max_or_min = recursive_loop(node, depth, depth_limit)
            max_or_min_values.append(max_or_min)
            depth -= 1
        else:
            max_or_min_values.append(node)
    
    if (depth % 2) == 0:
        return max(max_or_min_values)

    else:
        return min(max_or_min_values)
    

#print(recursive_loop(s_init, 0, 2))
    
