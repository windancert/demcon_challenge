import heapq

def assign_stages(shows):
    # Sort shows by start time
    shows.sort(key=lambda x: x[1])  # x = (name, start, end)

    # Heap: stores (end_time, stage_id)
    heap = []

    # Stage counter
    next_stage_id = 1

    # Available stage IDs (reusable)
    available_stages = []

    # Result: list of (show_name, start, end, stage_id)
    planning = []

    for name, start, end in shows:
        # Free up stages where the show ended strictly before this one starts
        while heap and heap[0][0] < start:
            ended_time, freed_stage = heapq.heappop(heap)
            heapq.heappush(available_stages, freed_stage)

        # Assign a stage
        if available_stages:
            stage_id = heapq.heappop(available_stages)
        else:
            stage_id = next_stage_id
            next_stage_id += 1

        # Add current show to the heap (end time inclusive)
        heapq.heappush(heap, (end, stage_id))

        # Save the assignment
        planning.append((name, start, end, stage_id))

    # Output
    print(f"Total stages needed: {next_stage_id - 1}\n")
    print("Planning:")
    for name, start, end, stage_id in planning:
        print(f"{name}: Stage {stage_id} (Start: {start}, End: {end})")

    return planning

# # Sample input (you can replace or extend this)
# shows = [
#     ("show_1", 36, 39),
#     ("show_2", 30, 33),
#     ("show_3", 29, 36),
#     ("show_4", 33, 35),
#     ("show_5", 40, 42),
#     ("show_6", 36, 40),
# ]

# assign_stages(shows)
