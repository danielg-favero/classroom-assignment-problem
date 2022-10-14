import pandas as pd

from parse_classrooms_data import parse_classrooms_data
from file_reader import file_reader


def write_results(output_name: str, S: str, aditional_info:str, execution_time: float):
    classrooms = file_reader("data/utfpr/rooms.txt")
    columns = []

    for room in parse_classrooms_data(classrooms):
        columns.append(room[0])

    results = ""
    results += aditional_info
    results += "Tempo de execução: {}s\n".format(
        execution_time)
    results += "Salas Alocadas: \n"

    for solutions in S:
        results += "{}".format(pd.DataFrame(data=solutions,
                                            columns=columns).to_string())

        results += "\n\n"

    with open("results/" + output_name + ".txt", 'w') as output_file:
        output_file.write("Resultados:\n" + results)
