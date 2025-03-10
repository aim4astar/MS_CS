from collections import deque

def isValid(state):
    M, C, B = state
    M_right, C_right = 3 - M, 3 - C

    if(M > 0 and M < C) or (M_right > 0 and M_right < C_right):
        return False
    
    return True

def get_next_state(state):
    M, C, B = state

    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

    next_states = []

    for m, c in moves:
        if(B == 'L'):
            next_state = (M - m, C - c, 'R')
        else:
            next_state = (M + m, C + c, 'L')

        if(0 <= next_state[0] <= 3 and 0 <= next_state[1] <= 3 and isValid(next_state)):
            next_states.append(next_state)
        

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

        if(state == goal):
            return new_path
        
        for next_state in get_next_state(state):
            queue.append((next_state, new_path))

    return None

solution = bfs()
if solution:
    for step in solution:
        print(f"Missionaries(Left): {step[0]} Cannibals(Left): {step[1]} Boat: {step[2]}")

else:
    print("Solution not found! :/")
        

