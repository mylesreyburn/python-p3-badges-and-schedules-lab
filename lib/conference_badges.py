def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    badge_list = [f"Hello, my name is {name}." for name in names]
    return badge_list

def assign_rooms(names):
    i = 0
    room_list = []
    for name in names:
        i += 1
        room_list.append(f"Hello, {name}! You'll be assigned to room {i}!")
    return room_list

def printer(names):
    badge_names = batch_badge_creator(names)
    room_phrases = assign_rooms(names)
    for string in badge_names:
        print(string)
    for string in room_phrases:
        print(string)
