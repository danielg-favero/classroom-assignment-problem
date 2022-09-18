import sys

from file_reader import file_reader
from parse_rooms_data import parse_rooms_data
from parse_schedules_data import parse_schedules_data
from write_results import write_results

roomsFile = file_reader("data/rooms.txt")
schedulesFile = file_reader("data/schedules.txt")


def classroom_assign(classes, rooms, total_hours):
    total_classrooms = len(rooms)
    agenda = [[0] * total_classrooms for i in range(total_hours)]

    total_assigned_classes = 0

    # ordernar as turmas C em ordem crescente de tempo de início (Si)
    classes.sort(key=lambda i: i[1])

    for i in range(0, len(classes)):
        d = 0
        j = i
        while (j < len(classes)) and (d < total_classrooms):
            start = classes[j][1]
            finish = classes[j][1] + classes[j][2]

            # se: ci é compatível com uma das d salas abertas, adicione ci a essa sala
            if (agenda[start][d] == 0) and (agenda[finish][d] == 0):
                total_assigned_classes += 1
                for k in range(start, finish + 1):
                    agenda[k][d] = classes[j][0]

                j += 1
            # senão: abra a sala d + 1 e adicione ci a essa nova sala
            else:
                # a sala d + 1 está disponível?
                if (d + 1) < total_classrooms:
                    d += 1
                # voltar a verificar na primeira sala
                else:
                    d = 0
                    j += 1

    return [agenda, total_assigned_classes]


# Escolher as turmas disponíveis baseado nos dias da semana
# 1 - Segunda-feira
# 2 - Terça-feira
# 3 - Quarta-feira
# 4 - Quinta-feira
# 5 - Sexta-feira
# 6 - Sábado
write_results(classroom_assign,
              [parse_schedules_data(schedulesFile, int(
                  sys.argv[1])), parse_rooms_data(roomsFile), 14],
              "greedy_method_results")
