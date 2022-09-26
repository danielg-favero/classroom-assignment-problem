from audioop import reverse
from time import process_time

from file_reader import file_reader
from parse_classrooms_data import parse_classrooms_data
from parse_subjects_data import parse_subjects_data
from write_results import write_results

classroomFile = file_reader("data/utfpr/rooms.txt")
subjectsFile = file_reader("data/utfpr/subjects.txt")

classes = parse_subjects_data(subjectsFile)
classrooms = parse_classrooms_data(classroomFile)


def overlap(start_time: int, end_time: int, current_classroom: int, Sk: list):
    availability = []

    for i in range(start_time, end_time):
        if Sk[i][current_classroom] != 0:
            availability.append(1)

    # Se pelo menos um horário não é compatível, não é possível alocar a sala
    if 1 in availability:
        return True
    else:
        return False


def available_class(L: list, classrooms: list, Sk: list):
    for i in range(0, len(classrooms) - 1):
        start_time = L[1]
        end_time = L[2] + 1

        # Verificar as retrições:
        if (
            # a) Em uma mesma sala e horário, não poderá haver duas turmas alocadas
            overlap(start_time, end_time, i, Sk) is False and

            # b) Uma sala não pode receber mais alunos que ela comporta
            # c) Utilizar o espaço de forma eficiente, ou seja, evitar alocar aulas de turmas pequenas em salas de maior capacidade
            L[3] <= classrooms[i][1]
        ):
            # Retornar o índice da sala disponível para alocação
            return i

    return None


def assign_class(L: list, D: int, Sk: list):
    start_time = L[1]
    end_time = L[2] + 1
    for i in range(start_time, end_time):
        Sk[i][D] = L[0]


def generate_empty_solution(rows: int, columns: int):
    return [[[0 for x in range(columns)] for y in range(rows)] for z in range(5)]


def greedy_classroom_assign(classes: list, classrooms: list):
    S = generate_empty_solution(16, len(classrooms))  # Solução do problema

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


algorithm_start_time = process_time()
S = greedy_classroom_assign(classes, classrooms)
algorithm_end_time = process_time()

write_results('greedy_results', S, algorithm_end_time - algorithm_start_time)
