import random

def overlap(start_time: int, end_time: int, current_classroom: int, Sk: list):
    availability = []

    for i in range(start_time, end_time):
        if Sk[i][current_classroom] != 0 and Sk[i][current_classroom] != 'RESERVADO':
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

        # Verificar as retrições essenciais:
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
        Sk[i][D] = L


def generate_empty_solution(rows: int, columns: int):
    return [[[0 for x in range(columns)] for y in range(rows)] for z in range(5)]

def generate_previous_assigned_classes(S: list):
    i = 0

    while i < 5:
        random.seed()
        column = round(random.random() * len(S[0]))
        row = round(random.random() * 15)
        total_hours = round(random.random() * 3)

        for j in range (0, total_hours):
            if row + j <= 15:
                S[i][row + j][column] = 'RESERVADO'

        i += 1

        # 50% de chance de alocar outra sala reservada
        assign_again = random.random()

        if assign_again <= 0.5:
            i -= 1

    return S