# Getting all he valid rooms in the unit, to maybe transfer here?
valid_rooms = {
    "CVICU": {
        "K0263", "K0264", "K0265", "K0266", "K0267", "K0268", "K0269","K0270", 
        "K0272", "K0273", 
        "K0274", "K0275", "K0276", "K0277",
    },

    "CVU": {
        "K0210", "K0211", "K0212",
        "K0214", "K0215", "K0216", "K0217",
        "K0220", "K0221", "K0222", "K0223", "K0224", "K0225", "K0226",
        "K0230", "K0231", "K0232", "K0233", "K0234", "K0235", "K0236",
        "K0240", "K0241", "K0242", "K0243", "K0244", "K0245", "K0246",
        "K0250", "K0251", "K0252", "K0253", "K0254", "K0255", "K0256", "K0257",
        "K0271"
    }
}


CVU_ROOM_PODS = {
    "B": { "K0210", "K0211", "K0212", "K0214", "K0215", "K0216", "K0217", 
          "K0220", "K0221", "K0222", "K0223", "K0224", "K0225", "K0226", "K0230",
          "K0255", "K0256", "K0257"},
    "C": {"K0231", "K0232", "K0233", "K0234", "K0235", "K0236",
          "K0240", "K0241", "K0242", "K0243", "K0244", "K0245", "K0246",
          "K0250", "K0251", "K0252", "K0253", "K0254",
          "K0271"}
}

CVU_ROOM_NEIGHBOURS = {

    # ---- 10-17 side ----
    "K0210": {"K0211"},
    "K0211": {"K0210", "K0212"},
    "K0212": {"K0211", "K0214"},
    "K0214": {"K0212", "K0215"},
    "K0215": {"K0214", "K0216"},
    "K0216": {"K0215", "K0217"},
    "K0217": {"K0216"},

    # ---- 20-30 / 31-36 middle corridor ----
    "K0220": {"K0221"},
    "K0221": {"K0220", "K0222"},
    "K0222": {"K0221", "K0223"},
    "K0223": {"K0222", "K0224"},
    "K0224": {"K0223", "K0225"},
    "K0225": {"K0224", "K0226"},
    "K0226": {"K0225", "K0230"},
    "K0230": {"K0226", "K0231"},   # B/C divider
    "K0231": {"K0230", "K0232"},   # B/C divider
    "K0232": {"K0231", "K0233"},
    "K0233": {"K0232", "K0234"},
    "K0234": {"K0233", "K0235"},
    "K0235": {"K0234", "K0236"},
    "K0236": {"K0235"},

    # ---- 40-46 side ----
    "K0240": {"K0241"},
    "K0241": {"K0240", "K0242"},
    "K0242": {"K0241", "K0243"},
    "K0243": {"K0242", "K0244"},
    "K0244": {"K0243", "K0245"},
    "K0245": {"K0244", "K0246"},
    "K0246": {"K0245", "K0250"},   # bridge toward 50-side

    # ---- 50-57 side ----
    "K0250": {"K0246", "K0251", "K0271"},
    "K0251": {"K0250", "K0252"},
    "K0252": {"K0251", "K0253"},
    "K0253": {"K0252", "K0254"},
    "K0254": {"K0253", "K0255"},   # C/B divider
    "K0255": {"K0254", "K0256"},   # C/B divider
    "K0256": {"K0255", "K0257"},
    "K0257": {"K0256"},

    # ---- edge room ----
    "K0271": {"K0250"},
}

#Across
ACROSS_PAIRS = [
    ("K0210", "K0220"),
    ("K0225", "K0257"),
    ("K0226", "K0256"),
    ("K0230", "K0255"),
    ("K0231", "K0254"),
    ("K0236", "K0240"),
    ("K0245", "K0250"),
]

CVU_ACROSS_ROOMS = {}

for room1, room2 in ACROSS_PAIRS:
    CVU_ACROSS_ROOMS.setdefault(room1, set()).add(room2)
    CVU_ACROSS_ROOMS.setdefault(room2, set()).add(room1)

def validate_neighbours(neighbours):
    for room, adjacent_rooms in neighbours.items():
        for adj in adjacent_rooms:
            if room not in neighbours.get(adj, set()):
                print(f"Warning: {room} lists {adj}, but {adj} does not list {room}")


from collections import deque

def room_distance(room1, room2, neighbours):
    if room1 not in neighbours or room2 not in neighbours:
        return None

    if room1 == room2:
        return 0

    visited = set()
    queue = deque([(room1, 0)])

    while queue:
        current_room, dist = queue.popleft()

        if current_room == room2:
            return dist

        if current_room in visited:
            continue

        visited.add(current_room)

        for next_room in neighbours[current_room]:
            if next_room not in visited:
                queue.append((next_room, dist + 1))

    return None

print(room_distance("K0220", "K0236", CVU_ROOM_NEIGHBOURS))