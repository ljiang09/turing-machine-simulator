
GR_ANBN = {
    "nonterminals": ["S"],
    "alphabet": ["a", "b"],
    "rules": [
        ("S", ""),
        ("S", "aSb")
    ],
    "start": "S"
}

GR_ANBM = {
    "nonterminals": ["S", "T", "U"],
    "alphabet": ["a", "b"],
    "rules": [
        ("S", "TU"),
        ("T", ""),
        ("T", "aTb"),
        ("U", ""),
        ("U", "Ub")
    ],
    "start": "S"
}


# Try to apply rules to a given string.

def replace(str, pos, lhs, rhs):
    # Replace lhs with rhs at pos of string.
    return str[:pos] + rhs + str[pos + len(lhs):]

def apply_rule(str, pos, rs):
    # Try to apply a rule in rs to str at position pos
    result = []
    for (lhs, rhs) in rs:
        if str[pos:].startswith(lhs):
            res = replace(str, pos, lhs, rhs)
            result.append(res)
    return result

def apply_rules(rs, str):
    result = []
    for pos in range(len(str)):
        res = apply_rule(str, pos, rs)
        result.extend(res)
    return result


# Remove null rules to simplify generation.

def nullable(g, nonterm):
    for (lhs, rhs) in g['rules']:
        if lhs == nonterm:
            if not rhs:
                return True
            for sym in rhs:
                if sym in g['alphabet']:
                    continue
                if sym == lhs:
                    # Skip in case of recursion.
                    continue
                if not nullable(g, sym):
                    continue
            return True
    return False

def remove_nullable(g):
    large = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nonterminals = [x for x in g['nonterminals']]
    def get_next():
        for t in large:
            if t not in nonterminals:
                nonterminals.append(t)
                return t
        raise Exception("Ran out of capital letters!")
    new_start = get_next()
    rules = g['rules']
    rules = [r for r in rules if r[1]]
    new_rules = []
    for (lhs, rhs) in rules:
        nullables = [i for (i, s) in enumerate(rhs) if nullable(g, s)]
        update = [rhs]
        for i in nullables:
            new_update = []
            for c in update:
                new_update.append(c)
                new_update.append(replace(c, i, "?", "."))
            update = new_update
        new_rules.extend([(lhs, rhs.replace(".", "")) for rhs in update])
    new_rules.append((new_start, g['start']))
    if nullable(g, g['start']):
        new_rules.append((new_start, ""))
    return {
        "alphabet": g['alphabet'],
        "nonterminals": nonterminals,
        "rules": new_rules,
        "start": new_start
    }
            
# Perform an iteratively deepening depth-first search of the rewrite tree.

def dfs_path(maxdepth, grammar, target):
    lt = len(target)
    q = [([grammar['start']], 0)]
    seen = set()
    while q:
        (path, d) = q[0]
        ###print(path, d)
        q = q[1:]
        if path:
            str = path[-1]
            if len(str) == lt and str == target:
                return path
            if str in seen:
                continue
            if d > maxdepth:
                seen.add(str)
                continue
            new_strs = apply_rules(grammar['rules'], str)
            ##print(new_strs)
            new_strs_d = [(path + [x], d + 1) for x in new_strs]
            ##print(new_strs_d)
            q = new_strs_d + q
            seen.add(str)
        else:
            raise Exception(f"Problem: empty path in dfs_path?")
    return []

def idfs_path(maxdepth, grammar, target, verbose=False):
    for d in range(1, maxdepth):
        if verbose:
            print(f"Searching - depth {d}")
        path = dfs_path(d, grammar, target)
        ##print(path)
        if path:
            return path

# Try to generate a string for a given grammar.

def check_cfg(g):
    # Check if a grammar is context free.
    for r in g['rules']:
        (lhs, rhs) = r
        if len(lhs) != 1:
            raise Exception(f"Rule {r} is not context free")
        for sym in rhs:
            if sym not in g['alphabet'] and sym not in g['nonterminals']:
                raise Exception(f"Symbol {sym} not defined")
    if g['start'] not in g['nonterminals']:
        raise Exception(f"Start symbol not a nonterminal")
    
def generate(grammar, str, maxdepth):
    check_cfg(grammar)
    g = remove_nullable(grammar)
    path = idfs_path(maxdepth, g, str, verbose=True)
    for (i, p) in enumerate(path or []):
        print(f"{'->' if i else ''} {p}")
    return bool(path)

# custom generator to quickly check working/failing strings
def generate_custom(grammar, str, maxdepth):
    check_cfg(grammar)
    g = remove_nullable(grammar)
    path = idfs_path(maxdepth, g, str)
    return bool(path)



#
# QUESTION 1
#

# generates the set of all strings of a's followed by b's followed by c's,
# where there are as many b's as a's and c's combined
GR_A = {
    "nonterminals": ["S", "T", "U"],
    "alphabet": ["a", "b", "c"],
    "rules": [
        ("S", ""),
        ("S", "TU"),
        ("T", ""),
        ("T", "aTb"),
        ("U", ""),
        ("U", "bUc")
    ],
    "start": "S"
}

# the set of all strings made up of as followed by bs followed by cs,
# where there are as many cs as as and bs combined
GR_B = {
    "nonterminals": ["S", "T", "U"],
    "alphabet": ["a", "b", "c"],
    "rules": [
        ("S", ""),
        ("S", "T"),
        ("S", "U"),
        ("T", ""),
        ("T", "aTc"),
        ("T", "aUc"),
        ("U", ""),
        ("U", "bUc")
    ],
    "start": "S"
}

# all strings over {a,b} that have the same number of as and bs
GR_C = {
    "nonterminals": ["S"],
    "alphabet": ["a", "b"],
    "rules": [ 
        ("S", ""),
        ("S", "Sab"),
        ("S", "abS"),
        ("S", "aSb"),
        ("S", "Sba"),
        ("S", "baS"),
        ("S", "bSa")
    ],
    "start": "S"
}

# the language of all strings representing unary addition
GR_D = {
    "nonterminals": ["S", "T"],
    "alphabet": ["1", "+", "="],
    "rules": [
        ("S", "1S1"),
        ("S", "1+T1"),
        ("T", "1=1"),
        ("T", "1T1")
    ],
    "start": "S"
}



# Sample Turing machines.


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
    print(f"{(str(state) + ' ' * width)[:width]} {content}")


#
# QUESTION 2
#
# q is a state of the Turing machine
# tape is a string representing the content of the tape
# pos is a number ≥ 1 representing the position of the tape head. (The leftmost cell of the tape is at position 1)


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



#
# QUESTION 3
#

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


# note: there are only 19 states without the accept/reject but i skipped state 11 bc in my diagram i
# skipped it on accident and it was easier to follow while maintaining the numbers
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

# print(accept_tm(TM_PLUS1, "#0#1"))
# print(accept_tm(TM_PLUS1, "#00#01"))
# print(accept_tm(TM_PLUS1, "#000#001"))
# print(accept_tm(TM_PLUS1, "#010#011"))
# print(accept_tm(TM_PLUS1, "#011#100"))
# print(accept_tm(TM_PLUS1, "#100#101"))
# print(accept_tm(TM_PLUS1, "#101#110"))
# print(accept_tm(TM_PLUS1, "#110#111"))
# print(accept_tm(TM_PLUS1, "#101010#101011"))
# print(accept_tm(TM_PLUS1, "#101111#110000"))


print(accept_tm(TM_PLUS1, "#0"))
print(accept_tm(TM_PLUS1, "#0#1#1"))
print(accept_tm(TM_PLUS1, "#0#11"))
