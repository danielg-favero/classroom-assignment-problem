def parse_classrooms_data(roomsFile):
    parsed_rooms = []

    # Formatar as salas disponíveis
    for data in roomsFile:
        room = data.split(' ')

        for roomData in room:
            roomData.replace('\n', '')

        parsed_rooms.append([
            room[0],
            int(room[1]),
            int(room[2]),
            room[3]
        ])

    parsed_rooms.sort(key=lambda i: i[1], reverse=True)

    return parsed_rooms