def parse_rooms_data(roomsFile):
    parsed_rooms = []

    # Formatar as salas disponíveis
    for data in roomsFile:
        parsed_rooms.append(int(data.split('\t')[1].replace('\n', '')))

    return parsed_rooms
