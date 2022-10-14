from local_search_utils import cost, swap_classes

def local_search(S: list, classrooms: list):
    C = S

    initial_cost = 0
    final_cost = 0

    initial_cost = cost(C, classrooms)
    while final_cost <= initial_cost:
        Ck = swap_classes(C, classrooms)
        final_cost = cost(Ck, classrooms)

        if final_cost < initial_cost:
            C = Ck
         
    return C