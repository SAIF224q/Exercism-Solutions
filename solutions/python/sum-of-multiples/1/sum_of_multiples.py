def sum_of_multiples(limit, multiples):
    set_of_multiples = set()
    for i in multiples:
        for j in range(1,10000):
            if j * i >= limit:
                break
            else:
                set_of_multiples.add(j*i)
    return sum(list(set_of_multiples))
            
