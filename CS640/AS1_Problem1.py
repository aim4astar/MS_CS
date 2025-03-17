from collections import deque

def is_valid(state):
    M_left, C_left, B = state
    M_right, C_right = 3 - M_left, 3 - C_left

    if(M_left > 0 and M_left < C_left) or (M_right > 0 and M_right < C_right):
        return False
    
    return True

def get_next_states(state):

    M, C, B = state
    moves = [(1, 0), (2, 0), (1, 1), (0, 1), (0, 2)]

    next_states = []

    for m, c in moves:
        if(B == 'L'):
            next_state = (M - m, C - c, 'R')
        else:
            next_state = (M + m, C + c, 'L')

        if(0 <= next_state[0] <= 3 and 0 <= next_state[1] <= 3 and is_valid(next_state)):
            next_states.append(next_state)
    
    print("State: ", state, "Generated states: ", next_states)
    return next_states
        

def bfs():
    start = (3, 3, 'L')
    goal = (0, 0, 'R')
    queue = deque([(start, [])])
    visited = set()


    while(queue):
        state, path = queue.popleft()
        if state in visited:
            continue

        visited.add(state)
        new_path = path + [state]

        if state == goal:
            return new_path
        
        for next_state in get_next_states(state):
            queue.append((next_state, new_path))
    
    return None

solution = bfs()
if solution:
    for step in solution:
        print("Missionaries: ", step[0], "Cannibals: ", step[1], "Boat: ", step[2])

else:
    print("No solution found")
    

