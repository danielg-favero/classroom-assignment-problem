from greedy_method_utils import overlap, available_class, assign_class, generate_empty_solution, generate_previous_assigned_classes, random_available_class
import random
from math import *  

def random_solution(classes: list, classrooms: list):
    # Solução do problema vazia
    S = generate_empty_solution(16, len(classrooms), 5)  

     # Resolver o problema para cada dia da semana
    for i in range(0, 5):
        # Solução do problema para um dia da semana
        Sk = S[i]

        # Disciplinas ordenadas por quantidade de alunos
        C = classes[i]
        C.sort(key=lambda j: j[3], reverse=True)

        while len(C) > 0:
            # Seleciona uma turma aleatoriamente
            k = floor(random.random() * len(C))

            L = C[k]

            # Verificar se há salas disponíveis para turma L
            D = random_available_class(L, classrooms, Sk)

            if D is not None:
                # Atribuir sala para turma L e atualizar solução
                assign_class(L, D, Sk)

            # Remover o primeiro elemento da lista, pois o mesmo já foi validado
            C.pop(k)
        
    return S