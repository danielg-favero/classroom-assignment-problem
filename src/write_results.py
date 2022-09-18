import pandas as pd
from time import process_time

from parse_rooms_data import parse_rooms_data
from file_reader import file_reader


def write_results(algorithm, input, outputName):
    roomsFile = file_reader("data/rooms.txt")
    rooms = parse_rooms_data(roomsFile)

    start_time = process_time()
    output = algorithm(*input)
    end_time = process_time()

    results = ""
    results += "Total de salas alocadas: {}\n".format(output[1])
    results += "Tempo de execução: {}s\n".format(end_time - start_time)
    results += "Salar Alocadas: \n{}".format(pd.DataFrame(data=output[0],
                                                          columns=rooms).to_string())

    with open("results/" + outputName + ".txt", 'w') as output_file:
        output_file.write("Resultados:\n" + results)
