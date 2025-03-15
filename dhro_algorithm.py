import networkx as nx

# Sample exam data: Subject -> List of Students
exam_data = {
    'Math': ['Alice', 'Bob', 'Charlie'],
    'Physics': ['Bob', 'Charlie', 'David'],
    'Chemistry': ['Alice', 'David', 'Eve'],
    'Biology': ['Charlie', 'Eve', 'Frank'],
    'English': ['Alice', 'Frank', 'Grace']
}

# Step 1: Construct Conflict Graph
def build_conflict_graph(exams):
    graph = nx.Graph()
    
    for subject in exams:
        graph.add_node(subject)  # Add each subject as a node

    subjects = list(exams.keys())
    for i in range(len(subjects)):
        for j in range(i + 1, len(subjects)):  # Avoid redundant checks
            subject_a, subject_b = subjects[i], subjects[j]
            common_students = set(exams[subject_a]) & set(exams[subject_b])
            if common_students:
                graph.add_edge(subject_a, subject_b, weight=len(common_students))

    return graph

# Step 2: Graph Coloring for Exam Scheduling
def schedule_exams(graph):
    coloring = {}
    sorted_nodes = sorted(graph, key=lambda x: graph.degree[x], reverse=True)

    for node in sorted_nodes:
        used_colors = {coloring[neighbor] for neighbor in graph[node] if neighbor in coloring}
        for color in range(len(graph)):  # Assign lowest possible time slot
            if color not in used_colors:
                coloring[node] = color
                break
                
    return coloring

# Step 3: Adjust for Fairness (Avoid Back-to-Back Exams)
def adjust_fairness(schedule, exams):
    student_slots = {}

    for subject, slot in schedule.items():
        for student in exams[subject]:
            if student in student_slots and abs(student_slots[student] - slot) == 1:
                schedule[subject] += 1  # Move to the next available slot
            student_slots[student] = schedule[subject]
    
    return schedule

# Step 4: Assign Rooms Efficiently
def assign_rooms(schedule, exams):
    rooms = ['Room A', 'Room B', 'Room C', 'Room D']  # Example rooms
    room_assignment = {}

    sorted_exams = sorted(schedule.keys(), key=lambda x: len(exams[x]), reverse=True)
    
    for subject in sorted_exams:
        slot = schedule[subject]
        assigned_room = rooms[slot % len(rooms)]
        room_assignment[subject] = (slot, assigned_room)

    return room_assignment

# Run the Algorithm
conflict_graph = build_conflict_graph(exam_data)
initial_schedule = schedule_exams(conflict_graph)
fair_schedule = adjust_fairness(initial_schedule, exam_data)
final_schedule = assign_rooms(fair_schedule, exam_data)

# Print Final Schedule
print("📅 Final Exam Schedule:")
for subject, (slot, room) in final_schedule.items():
    print(f"{subject} - Time Slot {slot} - {room}")
