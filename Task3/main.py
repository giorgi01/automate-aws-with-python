data = {
    1: [
        {"seat_name": "a1", "isTaken": True},
        {"seat_name": "a2", "isTaken": False},
        {"seat_name": "a3", "isTaken": True},
        {"seat_name": "a4", "isTaken": True},
        {"seat_name": "a5", "isTaken": False},
    ],
    2: [
        {"seat_name": "b1", "isTaken": False},
        {"seat_name": "b2", "isTaken": False},
        {"seat_name": "b3", "isTaken": True},
        {"seat_name": "b4", "isTaken": False},
        {"seat_name": "b5", "isTaken": True},
    ],
    3: [
        {"seat_name": "c1", "isTaken": False},
        {"seat_name": "c2", "isTaken": True},
        {"seat_name": "c3", "isTaken": True},
        {"seat_name": "c4", "isTaken": True},
        {"seat_name": "c5", "isTaken": False},
    ]
}

cabin = int(input("Which cabin?"))
seat_name = input("Which seat?")
for seat in data[cabin]:
    if seat["seat_name"] == seat_name:
        if seat["isTaken"]:
            print("Taken :(")
            for potential_seat in data[cabin]:
                if not potential_seat["isTaken"]:
                    print(f"You can take {potential_seat['seat_name']} seat")
                    break
        else:
            print("Welcome")
            break
