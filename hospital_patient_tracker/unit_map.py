import heapq


# Getting all the valid rooms in the unit
valid_rooms = {
    "CVICU": {
        "K0263", "K0264", "K0265", "K0266", "K0267", "K0268", "K0269", "K0270",
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
    "B": {
        "K0210", "K0211", "K0212", "K0214", "K0215", "K0216", "K0217",
        "K0220", "K0221", "K0222", "K0223", "K0224", "K0225", "K0226", "K0230",
        "K0255", "K0256", "K0257"
    },
    "C": {
        "K0231", "K0232", "K0233", "K0234", "K0235", "K0236",
        "K0240", "K0241", "K0242", "K0243", "K0244", "K0245", "K0246",
        "K0250", "K0251", "K0252", "K0253", "K0254",
        "K0271"
    }
}
CVU_ROOM_CONNECTIONS = {

    # 1 = Normal/Easy
    # 2 = Slightly awkward / across / offset
    # 3 = POD boundary / undesirable transition

    # ---- 10-17 side ----
    "K0210": {"K0211": 1, "K0220": 2},
    "K0211": {"K0210": 1, "K0212": 1},
    "K0212": {"K0211": 1, "K0214": 1},
    "K0214": {"K0212": 1, "K0215": 1},
    "K0215": {"K0214": 1, "K0216": 1},
    "K0216": {"K0215": 1, "K0217": 2},
    "K0217": {"K0216": 2, "K0224": 2},

    # ---- 20-30 / 31-36 middle corridor ----
    "K0220": {"K0221": 1, "K0210": 2},
    "K0221": {"K0220": 1, "K0222": 1},
    "K0222": {"K0221": 1, "K0223": 1},
    "K0223": {"K0222": 1, "K0224": 1},
    "K0224": {"K0223": 1, "K0225": 2, "K0217": 2},

    "K0225": {"K0224": 2, "K0226": 1, "K0257": 1},
    "K0226": {"K0225": 1, "K0230": 1, "K0256": 1},
    "K0230": {"K0226": 1, "K0231": 3, "K0255": 1},
    "K0231": {"K0230": 3, "K0232": 2, "K0254": 1},
    "K0232": {"K0231": 2, "K0233": 1, "K0251": 2, "K0252": 2},
    "K0233": {"K0232": 1, "K0234": 1},
    "K0234": {"K0233": 1, "K0235": 1},
    "K0235": {"K0234": 1, "K0236": 1},
    "K0236": {"K0235": 1, "K0240": 2},

    # ---- 40-46 side ----
    "K0240": {"K0236": 2, "K0241": 1},
    "K0241": {"K0240": 1, "K0242": 1},
    "K0242": {"K0241": 1, "K0243": 1},
    "K0243": {"K0242": 1, "K0244": 1},
    "K0244": {"K0243": 1, "K0245": 2, "K0251": 2, "K0252": 2},
    "K0245": {"K0244": 2, "K0246": 1, "K0250": 2},
    "K0246": {"K0245": 1, "K0250": 2, "K0271": 3},

    # ---- 50-57 side ----
    "K0250": {"K0246": 2, "K0251": 1, "K0245": 2, "K0271": 2},
    "K0251": {"K0250": 1, "K0252": 1, "K0232": 2, "K0244": 2},
    "K0252": {"K0251": 1, "K0253": 1, "K0232": 2, "K0244": 2},
    "K0253": {"K0252": 1, "K0254": 1},
    "K0254": {"K0253": 1, "K0255": 3, "K0231": 1},
    "K0255": {"K0254": 3, "K0256": 1, "K0230": 1},
    "K0256": {"K0255": 1, "K0257": 1, "K0226": 1},
    "K0257": {"K0256": 1, "K0225": 1},

    # ---- edge room ----
    "K0271": {"K0246": 3, "K0250": 2},
}



def validate_connections(connections):
    for room, connected_rooms in connections.items():
        for connected_room, weight in connected_rooms.items():
            if connected_room not in connections:
                print(f"Warning: {connected_room} not found in connections.")
                continue

            reverse_weight = connections.get(connected_room, {}).get(room)

            if reverse_weight is None:
                print(f"Warning: {room} connects to {connected_room}, but reverse link is missing.")
            elif reverse_weight != weight:
                print(
                    f"Warning: weight mismatch between {room} -> {connected_room} ({weight}) "
                    f"and {connected_room} -> {room} ({reverse_weight})"
                )

def room_distance(room1, room2, connections):
    if room1 not in connections or room2 not in connections:
        return None

    if room1 == room2:
        return 0

    min_heap = [(0, room1)]
    visited = set()

    while min_heap:
        current_cost, current_room = heapq.heappop(min_heap)

        if current_room == room2:
            return current_cost

        if current_room in visited:
            continue

        visited.add(current_room)

        for next_room, edge_cost in connections[current_room].items():
            if next_room not in visited:
                heapq.heappush(min_heap, (current_cost + edge_cost, next_room))

    return None

def validate_all_cvu_rooms_mapped():
    missing = valid_rooms["CVU"] - set(CVU_ROOM_CONNECTIONS.keys())
    extra = set(CVU_ROOM_CONNECTIONS.keys()) - valid_rooms["CVU"]

    if missing:
        print("Missing rooms in CVU_ROOM_CONNECTIONS:", missing)
    if extra:
        print("Extra rooms in CVU_ROOM_CONNECTIONS:", extra)

    if not missing and not extra:
        print("All CVU rooms are correctly mapped in CVU_ROOM_CONNECTIONS.")

def validate_pods():
    all_pod_rooms = set()

    for pod, rooms in CVU_ROOM_PODS.items():
        overlap = all_pod_rooms.intersection(rooms)
        if overlap:
            print(f"Overlap found in pod {pod}: {overlap}")
        all_pod_rooms.update(rooms)

    missing = valid_rooms["CVU"] - all_pod_rooms
    extra = all_pod_rooms - valid_rooms["CVU"]

    if missing:
        print("Rooms missing from CVU_ROOM_PODS:", missing)
    if extra:
        print("Extra rooms in CVU_ROOM_PODS:", extra)

    if not missing and not extra:
        print("All CVU rooms are correctly assigned to pods.")

def get_room_pod(room):
    for pod, rooms in CVU_ROOM_PODS.items():
        if room in rooms:
            return pod
    return None

validate_connections(CVU_ROOM_CONNECTIONS)
validate_all_cvu_rooms_mapped()
validate_pods()

print(get_room_pod("K0256"))              # should be B
print(get_room_pod("K0254"))              # should be C
print(room_distance("K0220", "K0236", CVU_ROOM_CONNECTIONS))
print(room_distance("K0210", "K0217", CVU_ROOM_CONNECTIONS))
print(room_distance("K0210", "K0271", CVU_ROOM_CONNECTIONS))