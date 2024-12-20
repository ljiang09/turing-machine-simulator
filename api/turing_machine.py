# Takes in strings over the alphabet {a, b}.
# Determines if there are an equal number of a's and b's, where all a's come before any b's.
TM_ANBN = {
    "states": [1, 2, 4, 6, 7, 777, 666],
    "alphabet": ['a','b'],
    "tape_alphabet": ['a','b','X','Y','_'],
    "start": 1,
    "accept": 777,
    "reject": 666,
    "delta": [
        (1, 'a', 2, 'X', 1),
        (1, '_', 777, '_', 1),
        (2, 'a', 2, 'a', 1),
        (2, 'Y', 2, 'Y', 1),
        (2, 'b', 4, 'Y', -1),
        (4, 'Y', 4, 'Y', -1),
        (4, 'a', 7, 'a', -1),
        (4, 'X', 6, 'X', 1),
        (6, 'Y', 6, 'Y', 1),
        (6, '_', 777, '_', 1),
        (7, 'a', 7, 'a', -1),
        (7, 'X', 1, 'X', 1)
    ]
}


TM_ANBNCN = {
    "states": [1, 2, 3, 4, 5, 6, 7, 8, 666, 777],
    "alphabet": ['a','b','c'],
    "tape_alphabet": ['a','b','c','X','Y','Z','_'],
    "start": 1,
    "accept": 777,
    "reject": 666,
    "delta": [
        (1, 'a', 2, 'X', 1),
        (1, '_', 777, '_', 1),
        (2, 'a', 2, 'a', 1),
        (2, 'Y', 2, 'Y', 1),
        (2, 'b', 3, 'Y', 1),
        (3, 'b', 3, 'b', 1),
        (3, 'Z', 3, 'Z', 1),
        (3, 'c', 4, 'Z', -1),
        (4, 'Z', 4, 'Z', -1),
        (4, 'Y', 5, 'Y', -1),
        (4, 'b', 7, 'b', -1),
        (5, 'Y', 5, 'Y', -1),
        (5, 'X', 6, 'X', 1),
        (6, 'Y', 6, 'Y', 1),
        (6, 'Z', 6, 'Z', 1),
        (6, '_', 777, '_', 1),
        (7, 'b', 7, 'b', -1),
        (7, 'Y', 7, 'Y', -1),
        (7, 'a', 8, 'a', -1),
        (8, 'a', 8, 'a', -1),
        (8, 'X', 1, 'X', 1)
    ]
}


# Print a configuration from a Turing machine.

def print_config(m, c):
    (state, tape, pos) = c
    width = max(len(str(q)) for q in m['states'])
    padding = max(0, pos - len(tape))
    tape = tape + (' ' * padding)
    content = "".join(f"[{x}]" if i + 1 == pos else f" {x} " for (i, x) in enumerate(tape))
    # print(f"{(str(state) + ' ' * width)[:width]} {content}")
    print(content)


# Finds the starting configuration for a Turing Machine
# 
# m: Turing machine
# w: an input string
# 
# Returns: the starting configuration for executing the machine
def start_tm(m, w):
    start = m["start"]
    
    if len(w) == 0:
        return (start, "_", 1)

    return (start, w, 1)


# m: Turing machine m
# c: configuration of the form (state, tape, pos)
# 
# Returns a list of all configurations that can be reached by following an enabled transition from the given configuration: that is, it should return a list of all configurations that you can obtain by following a transition from state state with symbol tape[pos - 1].
def step_tm(m, c):
    (state, tape, pos) = c
    if pos-1 == len(tape):
        tape += "_"
    tape_val = tape[pos-1]

    configs = []

    for transition in m["delta"]:
        if state == transition[0] and tape_val == transition[1]:
            new_tape = tape[:pos-1] + transition[3] + tape[pos:]
            new_tape_pos = pos + transition[4]
            if new_tape_pos == len(tape):
                new_tape += "_"
            if new_tape_pos < 1:
                new_tape_pos = 1
            configs.append((transition[2], new_tape, new_tape_pos))

    # if in any given state and symbol there is no enabled transition,
    # then pretend there was an enabled transition that went to the reject state
    if len(configs) == 0:
        configs.append((666, tape, pos + 1))

    return configs


# Finds if the configuration is an accepting configuration
# 
# m: Turing machine
# c: a configuration
# 
# returns True exactly when the configuration has an accepting state
def is_accept_tm(m, c):
    if c[0] == m["accept"]:
        return True
    return False


# determines if a configuration is a stopping config
# 
# m: Turing machine
# c: a configuration
# 
# returns True exactly when the configuration is a configuration that stops the machine
def is_done_tm(m, c):
    if c[0] == m["accept"] or c[0] == m["reject"]:
        return True
    return False

# determines if a Turing Machine accepts an input string
# 
# m: Turing machine
# input: string
def accept_tm(m, input):
    current_config = start_tm(m, input)

    while not is_done_tm(m, current_config):
        print_config(m, current_config)
        # if current_config[2] >= len(current_config[1]):
        #     print("***")
        #     current_config = (777, current_config[1], current_config[2] + 1)
        # else:
        next_steps = step_tm(m, current_config)
        if len(next_steps) > 1:
            raise Exception("Machine is non-deterministic")
        else:
            current_config = next_steps[0]

    print_config(m, current_config)

    if is_accept_tm(m, current_config):
        return True
    return False



# Takes in strings over the alphabet {a, b}.
# Determines if there are an equal number of a's and b's, but in any order.
TM_EQUAL = {
    "states": [1, 2, 3, 4, 5, 6, 7, 8, 9, 777, 666],
    "alphabet": ['a', 'b'],
    "tape_alphabet": ['a', 'b', 'X', 'Y', '_'],
    "start": 1,
    "accept": 777,
    "reject": 666,
    "delta": [
        # huge block of transitions if we start with an a
        (1, 'a', 2, 'X', 1),
        (2, 'a', 2, 'a', 1),
        (2, 'Y', 2, 'Y', 1),
        (2, '_', 666, '_', 1),  # reject if we don't find a matching b
        (2, 'b', 3, 'Y', -1),

        # move back to front of the tape
        (3, 'a', 3, 'a', -1),
        (3, 'b', 3, 'b', -1),
        (3, 'Y', 3, 'Y', -1),

        (3, 'X', 4, 'X', 1),

        (4, 'b', 4, 'b', 1),
        (4, 'Y', 4, 'Y', 1),
        (4, '_', 777, '_', 1),  # accept if we're done with the string
        (4, 'a', 5, 'Y', -1),

        # move back to front of the tape
        (5, 'a', 5, 'a', -1),
        (5, 'b', 5, 'b', -1),
        (5, 'Y', 5, 'Y', -1),

        (5, 'X', 2, 'X', 1),


        # huge block of transitions if we start with a b
        (1, 'b', 6, 'X', 1),
        (6, 'b', 6, 'b', 1),
        (6, 'Y', 6, 'Y', 1),
        (6, '_', 666, '_', 1),  # reject if we don't find a matching b
        (6, 'a', 7, 'Y', -1),

        # move back to front of the tape
        (7, 'a', 7, 'a', -1),
        (7, 'b', 7, 'b', -1),
        (7, 'Y', 7, 'Y', -1),

        (7, 'X', 8, 'X', 1),

        (8, 'a', 8, 'a', 1),
        (8, 'Y', 8, 'Y', 1),
        (8, '_', 777, '_', 1),  # accept if we're done with the string
        (8, 'b', 9, 'Y', -1),

        # move back to front of the tape
        (9, 'a', 9, 'a', -1),
        (9, 'b', 9, 'b', -1),
        (9, 'Y', 9, 'Y', -1),

        (9, 'X', 6, 'X', 1),
    ]
}


# Takes in strings over the alphabet {0, 1, #} of the form #u#v#w, where u, v, and w are binary strings.
# Determines if w is equal to the pointwise AND of u and v.
TM_AND = {
    "states": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 777, 666],
    "alphabet": ['0', '1', '#'],
    "tape_alphabet": ['0', '1', '#', "S", "X", '_'],
    "start": 1,
    "accept": 777,
    "reject": 666,
    "delta": [
        # mark the first hashtag as the start
        (1, '#', 1, 'S', 1),
        (1, '_', 777, '_', 1),
        
        # skip numbers we've already seen
        (1, 'X', 1, 'X', 1),

        # if we find a digit, read it and skip all remaining digits
        (1, '1', 2, 'X', 1),
        (1, '0', 3, 'X', 1),
        # skip all remaining digits
        (2, '1', 2, '1', 1),
        (2, '0', 2, '0', 1),
        (3, '1', 3, '1', 1),
        (3, '0', 3, '0', 1),

        # if we see the next hashtag, let's move to a new state and start the process again
        (2, '#', 4, '#', 1),
        (3, '#', 5, '#', 1),

        # skip the digits we've seen (in the 2nd set of digits)
        (4, 'X', 4, 'X', 1),
        (5, 'X', 5, 'X', 1),

        # if we find a digit, read it and skip all remaining digits
        (4, '1', 6, 'X', 1),
        (4, '0', 7, 'X', 1),
        (5, '1', 8, 'X', 1),
        (5, '0', 9, 'X', 1),
        # skip all remaining digits
        (6, '1', 6, '1', 1),
        (6, '0', 6, '0', 1),
        (7, '1', 7, '1', 1),
        (7, '0', 7, '0', 1),
        (8, '1', 8, '1', 1),
        (8, '0', 8, '0', 1),
        (9, '1', 9, '1', 1),
        (9, '0', 9, '0', 1),

        # if we see the third hashtag, let's move to a new state and start the process again
        (6, '#', 10, '#', 1),
        (7, '#', 11, '#', 1),
        (8, '#', 12, '#', 1),
        (9, '#', 13, '#', 1),

        # skip the digits we've seen (in the 3nd set of digits)
        (10, 'X', 10, 'X', 1),
        (11, 'X', 11, 'X', 1),
        (12, 'X', 12, 'X', 1),
        (13, 'X', 13, 'X', 1),

        # if we find a digit, read it and either reject or move back to the start
        # rejection states
        (10, '0', 666, 'X', 1),
        (11, '1', 666, 'X', 1),
        (12, '1', 666, 'X', 1),
        (13, '1', 666, 'X', 1),

        # start moving back to the start of the tape
        (10, '1', 14, 'X', -1),
        (11, '0', 14, 'X', -1),
        (12, '0', 14, 'X', -1),
        (13, '0', 14, 'X', -1),

        # otherwise, we know the string is done and we can accept
        # (10, '_', 777, '_', -1),
        # (11, '_', 777, '_', -1),
        # (12, '_', 777, '_', -1),
        # (13, '_', 777, '_', -1),

        # keep moving backwards until we're at the start again
        (14, '0', 14, '0', -1),
        (14, '1', 14, '1', -1),
        (14, '#', 14, '#', -1),
        (14, 'X', 14, 'X', -1),

        # if we find the start then go back to state 1
        (14, 'S', 1, 'S', 1),
    ]
}


# Takes in strings over the alphabet {0, 1, #} of the form #u#v, where u and v are binary strings of the same length.
# Determines if u + 1 = v when viewed as binary numbers.
TM_PLUS1 = {
    "states": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15, 16, 17, 18, 19, 20, 777, 666],
    "alphabet": ['0', '1', '#'],
    "tape_alphabet": ['0', '1', '#', "S", "X", '_'],
    "start": 1,
    "accept": 777,
    "reject": 666,
    "delta": [
        # mark the first hashtag as the start
        (1, '#', 1, 'S', 1),
        (1, '_', 777, '_', 1),

        # skip unread digits until we find the read portion
        (1, '1', 1, '1', 1),
        (1, '0', 1, '0', 1),

        # if we find the read portion or the next hashtag, go backwards one to get the last unread digit
        # (1, '#', 2, '#', -1),
        (1, 'X', 2, 'X', -1),

        # move to a new state for this last unread digit
        (2, '1', 3, 'X', 1),
        (2, '0', 4, 'X', 1),

        # skip any already-read digits
        (3, 'X', 3, 'X', 1),
        (4, 'X', 4, 'X', 1),

        # if we hit a hashtag, move to a new state to parse the next set of digits
        (3, '#', 5, '#', 1),
        (4, '#', 6, '#', 1),

        # skip through digits
        (5, '0', 5, '0', 1),
        (5, '1', 5, '1', 1),
        (6, '0', 6, '0', 1),
        (6, '1', 6, '1', 1),

        # if we hit an X or the end, scoot back one
        (5, '_', 7, '_', -1),
        (5, 'X', 7, 'X', -1),
        (6, '_', 8, '_', -1),
        (6, 'X', 8, 'X', -1),

        # check second digit
        (7, '1', 666, 'X', -1),
        (7, '0', 10, 'X', -1),
        (8, '1', 9, 'X', -1),
        (8, '0', 666, 'X', -1),
        
        # (8, '_', 777, '_', 1),

        # if no carried ones, move back to start and repeat
        (9, '1', 9, '1', -1),
        (9, '0', 9, '0', -1),
        (9, '#', 9, '#', -1),
        (9, 'X', 9, 'X', -1),
        (9, 'S', 1, 'S', 1),





        # if there is a carried one, move to a new flow
        (10, '1', 10, '1', -1),
        (10, '0', 10, '0', -1),
        (10, '#', 10, '#', -1),
        (10, 'X', 10, 'X', -1),
        (10, 'S', 12, 'S', 1),

        # skip unread digits until we find the read portion
        (12, 'S', 12, 'S', 1),
        (12, '1', 12, '1', 1),
        (12, '0', 12, '0', 1),

        # if we find the read portion or the next hashtag, go backwards one to get the last unread digit
        (12, '#', 13, '#', -1),
        (12, 'X', 13, 'X', -1),

        # move to a new state for this last unread digit
        (13, '1', 14, 'X', 1),
        (13, '0', 15, 'X', 1),

        # skip any already-read digits
        (14, 'X', 14, 'X', 1),
        (15, 'X', 15, 'X', 1),

        # if we hit a hashtag, move to a new state to parse the next set of digits
        (14, '#', 16, '#', 1),
        (15, '#', 17, '#', 1),

        # skip through digits
        (16, '0', 16, '0', 1),
        (16, '1', 16, '1', 1),
        (17, '0', 17, '0', 1),
        (17, '1', 17, '1', 1),

        # if we hit an X or the end, scoot back one
        (16, '_', 18, '_', -1),
        (16, 'X', 18, 'X', -1),
        (17, '_', 19, '_', -1),
        (17, 'X', 19, 'X', -1),

        # check second digit
        (18, '1', 666, 'X', -1),
        (18, '0', 10, 'X', -1),
        (19, '1', 9, 'X', -1),
        (19, '0', 666, 'X', -1),
    ]
}
