from greedy_method_utils import overlap, available_class, assign_class, generate_empty_solution, generate_previous_assigned_classes

def greedy_classroom_assign(classes: list, classrooms: list):
    # Solução do problema vazia
    S = generate_empty_solution(16, len(classrooms), 5)  

    # Gerar conjunto aleatório de salas reservadas
    S = generate_previous_assigned_classes(S)

    # Resolver o problema para cada dia da semana
    for i in range(0, 5):
        # Solução do problema para um dia da semana
        Sk = S[i]

        # Disciplinas ordenadas por quantidade de alunos
        C = classes[i]
        C.sort(key=lambda j: j[3], reverse=True)

        while len(C) > 0:
            # Seleciona a primeira turma, ou seja, a que possui o maior número de alunos
            L = C[0]

            # Verificar se há salas disponíveis para turma L
            D = available_class(L, classrooms, Sk)

            if D is not None:
                # Atribuir sala para turma L e atualizar solução
                assign_class(L, D, Sk)

            # Remover o primeiro elemento da lista, pois o mesmo já foi validado
            C.pop(0)

    return S