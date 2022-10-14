from local_search_utils import cost, swap_classes

def local_search(S: list, classrooms: list):
    C = S
    final_cost = 0

    # Custo inicial gerado pelo metodo guloso
    initial_cost = cost(C, classrooms)
    while final_cost <= initial_cost:
        # Realizar troca das posicoes das turmas
        Ck = swap_classes(C, classrooms)

        # Custo final após a troca das turmas
        final_cost = cost(Ck, classrooms)

        # Atribuir a nova solução a solução corrente
        C = Ck
         
    return C