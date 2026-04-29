import heapq


valid_rooms = {
    "CVICU": {
        "K0263", "K0264", "K0265", "K0266", "K0267", "K0268", "K0269", "K0270",
        "K0272", "K0273", "K0274", "K0275", "K0276", "K0277",
    },

    "CVU": {
        "K0210", "K0211", "K0212", "K0214", "K0215", "K0216", "K0217",
        "K0220", "K0221", "K0222", "K0223", "K0224", "K0225", "K0226",
        "K0230", "K0231", "K0232", "K0233", "K0234", "K0235", "K0236",
        "K0240", "K0241", "K0242", "K0243", "K0244", "K0245", "K0246",
        "K0250", "K0251", "K0252", "K0253", "K0254", "K0255", "K0256",
        "K0257", "K0271"
    }
}


CVU_ROOM_PODS = {
    "B": {
        "K0210", "K0211", "K0212", "K0214", "K0215", "K0216", "K0217",
        "K0220", "K0221", "K0222", "K0223", "K0224", "K0225", "K0226",
        "K0230", "K0255", "K0256", "K0257"
    },

    "C": {
        "K0231", "K0232", "K0233", "K0234", "K0235", "K0236",
        "K0240", "K0241", "K0242", "K0243", "K0244", "K0245", "K0246",
        "K0250", "K0251", "K0252", "K0253", "K0254", "K0271"
    }
}


POD_CROSSING_PENALTY = 30


CVU_ROOM_CONNECTIONS = {
    # ---- 10-17 side ----
    "K0210": {"K0211": 5, "K0220": 24},
    "K0211": {"K0210": 5, "K0212": 8},
    "K0212": {"K0211": 8, "K0214": 4},
    "K0214": {"K0212": 4, "K0215": 8},
    "K0215": {"K0214": 8, "K0216": 4},
    "K0216": {"K0215": 4, "K0217": 6},
    "K0217": {"K0216": 6, "K0224": 20, "K0225": 16, "K0257": 18},

    # ---- 20-30 / 31-36 middle corridor ----
    "K0220": {"K0221": 8, "K0210": 24},
    "K0221": {"K0220": 8, "K0222": 4},
    "K0222": {"K0221": 4, "K0223": 8},
    "K0223": {"K0222": 8, "K0224": 4},
    "K0224": {"K0223": 4, "K0225": 22, "K0217": 20},

    "K0225": {"K0217": 16, "K0224": 22, "K0226": 8, "K0257": 2},
    "K0226": {"K0225": 8, "K0230": 4, "K0256": 2},
    "K0230": {"K0226": 4, "K0231": 8, "K0255": 2},

    "K0231": {"K0230": 8, "K0232": 22, "K0254": 2},
    "K0232": {"K0231": 22, "K0233": 4, "K0251": 18, "K0252": 16},
    "K0233": {"K0232": 4, "K0234": 8},
    "K0234": {"K0233": 8, "K0235": 4},
    "K0235": {"K0234": 4, "K0236": 8},
    "K0236": {"K0235": 8, "K0240": 10},

    # ---- 40-46 side ----
    "K0240": {"K0236": 10, "K0241": 8},
    "K0241": {"K0240": 8, "K0242": 4},
    "K0242": {"K0241": 4, "K0243": 8},
    "K0243": {"K0242": 8, "K0244": 4},
    "K0244": {"K0243": 4, "K0245": 22, "K0251": 16, "K0252": 18},
    "K0245": {"K0244": 22, "K0246": 8, "K0250": 4},
    "K0246": {"K0245": 8, "K0271": 4},

    # ---- 50-57 side ----
    "K0250": {"K0251": 8, "K0245": 4, "K0271": 18},
    "K0251": {"K0250": 8, "K0252": 4, "K0232": 18, "K0244": 16},
    "K0252": {"K0251": 4, "K0253": 8, "K0232": 16, "K0244": 18},
    "K0253": {"K0252": 8, "K0254": 4},
    "K0254": {"K0253": 4, "K0255": 8, "K0231": 2},

    "K0255": {"K0254": 8, "K0256": 4, "K0230": 2},
    "K0256": {"K0255": 4, "K0257": 8, "K0226": 2},
    "K0257": {"K0217": 18, "K0256": 8, "K0225": 2},

    # ---- 71 edge room ----
    "K0271": {"K0246": 4, "K0250": 18},
}


def get_room_pod(room):
    for pod, rooms in CVU_ROOM_PODS.items():
        if room in rooms:
            return pod
    return None


def rooms_cross_pods(room1, room2):
    pod1 = get_room_pod(room1)
    pod2 = get_room_pod(room2)

    if pod1 is None or pod2 is None:
        return False

    return pod1 != pod2


def room_distance(room1, room2, connections=CVU_ROOM_CONNECTIONS):
    """
    Returns real walking distance in steps.
    Uses Dijkstra because step distances are weighted.
    """
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


def adjusted_room_distance(room1, room2):
    """
    Returns walking distance + pod crossing penalty.
    Use this in assignment_engine.py.
    """
    distance = room_distance(room1, room2)

    if distance is None:
        return None

    if rooms_cross_pods(room1, room2):
        distance += POD_CROSSING_PENALTY

    return distance


def validate_connections(connections=CVU_ROOM_CONNECTIONS):
    for room, connected_rooms in connections.items():
        for connected_room, weight in connected_rooms.items():
            if connected_room not in connections:
                print(f"Warning: {connected_room} not found in connections.")
                continue

            reverse_weight = connections[connected_room].get(room)

            if reverse_weight is None:
                print(f"Warning: {room} connects to {connected_room}, but reverse link is missing.")
            elif reverse_weight != weight:
                print(
                    f"Warning: weight mismatch: {room} -> {connected_room} ({weight}) "
                    f"but {connected_room} -> {room} ({reverse_weight})"
                )


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


def run_unit_map_tests():
    print("\n--- VALIDATING CONNECTIONS ---")
    validate_connections()

    print("\n--- VALIDATING CVU ROOM MAP ---")
    validate_all_cvu_rooms_mapped()

    print("\n--- VALIDATING PODS ---")
    validate_pods()

    print("\n--- POD TESTS ---")
    print("K0256 pod:", get_room_pod("K0256"))  # B
    print("K0254 pod:", get_room_pod("K0254"))  # C
    print("K0230 pod:", get_room_pod("K0230"))  # B
    print("K0231 pod:", get_room_pod("K0231"))  # C

    print("\n--- DISTANCE TESTS ---")
    print("Raw K0230 to K0231:", room_distance("K0230", "K0231"))
    print("Adjusted K0230 to K0231:", adjusted_room_distance("K0230", "K0231"))

    print("Raw K0254 to K0255:", room_distance("K0254", "K0255"))
    print("Adjusted K0254 to K0255:", adjusted_room_distance("K0254", "K0255"))

    print("Raw K0225 to K0257:", room_distance("K0225", "K0257"))
    print("Adjusted K0225 to K0257:", adjusted_room_distance("K0225", "K0257"))


# Uncomment to test this file directly:
run_unit_map_tests()