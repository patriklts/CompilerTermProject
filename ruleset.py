# ruleset.py

# Dictionary for derivations 
derivations = {
    0 : "CODE -> CODE' CODE",  
    1 : "CODE -> ''",
    2 : "CODE' -> VDECL",
    3 : "CODE' -> FDECL",
    4 : "VDECL -> id VDECL'",
    5 : "VDECL' -> semi",
    6 : "VDECL' -> ASSIGN semi",
    7 : "ASSIGN -> assign RHS",
    8 : "RHS -> EXPR",
    9 : "RHS -> literal ",
    10 : "RHS -> character", 
    11 : "RHS -> boolstr",
    12 : "EXPR -> TERM EXPR'",
    13 : "EXPR' -> addsub TERM EXPR'",
    14 : "EXPR' -> ''",
    15 : "TERM -> FACTOR TERM'",
    16 : "TERM' -> multdiv FACTOR TERM'",
    17 : "TERM' -> ''",
    18 : "FACTOR -> lparen EXPR rparen",
    19 : "FACTOR -> num",
    20 : "FACTOR -> id",
    21 : "FDECL -> id lparen ARG rparen lbrace BLOCK RETURN rbrace",
    22 : "ARG -> vtype id MOREARGS",
    23 : "ARG -> ''",
    24 : "MOREARGS -> comma vtype id MOREARGS",
    25 : "MOREARGS -> ''",
    26 : "BLOCK -> STMT BLOCK", 
    27 : "BLOCK -> ''",
    28 : "STMT -> VDECL",
    29 : "STMT -> ASSIGN semi",
    30 : "STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE",
    31 : "STMT -> while lparen COND rparen lbrace BLOCK rbrace",
    32 : "COND -> boolstr COND'",
    33 : "COND' -> comp COND",
    34 : "COND' -> ''",
    35 : "ELSE -> else lbrace BLOCK rbrace", 
    36 : "ELSE -> ''",
    37 : "RETURN -> return RHS semi"
}

# Dictionary for action mapping of SLR table
action_map = {
    0: {'vtype': 's2', 'id': 's5'},
    1: {'vtype': 's2', "id": "s5", '$': 'r1'},
    2: {'id': 'r2', "vtype": "r2", "$": 'r2'},
    3: {'$': 'r3', "vtype": "r3", "id": 'r3'},    
    4: {'id': 's7'},
    5: {'lparen': 's8'},
    6: {'$': 'acc'},
    7: {'semi': 's10', 'assign': 's12'},
    8: {'vtype': 's14', "rparen": "r23"},
    9: {'vtype': 'r4', 'id': 'r4', "assign": "r4", "rbrace": "r4", "$": 'r4', 'if': 'r4', 'while': 'r4', 'return': 'r4'},
    10: {'vtype': 'r5', 'id': 'r5', "assign": "r5", "rbrace": "r5", "$": 'r5', 'if': 'r5', 'while': 'r5', 'return': 'r5'},
    11: {'semi': 's15'},
    12: {'id' : 's25', 'literal': 's18', 'character': 's19', 'boolstr': 's20', 'lparen': 's23', 'num': 's24'},
    13: {'rparen': 's26'},
    14: {'id': 's27'},
    15: {'vtype': 'r6', 'id': 'r6', 'assign': 'r6', 'rbrace': 'r6', 'if': 'r6', 'while': 'r6', 'return': 'r6', '$': 'r6'},
    16: {'semi': 'r7'},
    17: {'semi': 'r8'},
    18: {'semi': 'r9'},
    19: {'semi': 'r10'},
    20: {'semi': 'r11'},
    21: {'semi': 'r14', 'addsub': 's29', 'rparen': 'r14'},
    22: {'semi': 'r17', 'addsub': 'r17', 'multdiv': 's31', 'rparen': 'r17'},
    23: {'id': 's25', 'lparen': 's23', 'num': 's24'},
    24: {'semi': 'r19', 'addsub': 'r19', 'multdiv': 'r19', 'rparen': 'r19'},
    25: {'semi': 'r20', 'addsub': 'r20', 'multdiv': 'r20', 'rparen': 'r20'},
    26: {'lbrace': 's33'},
    27: {'rparen': 'r25', 'comma': 's35'},
    28: {'semi': 'r12', 'rparen': 'r12'},
    29: {'id': 's25', 'lparen': 's23', 'num': 's24'},
    30: {'semi': 'r15', 'addsub': 'r15', 'rparen': 'r15'},
    31: {'id': 's25', 'lparen': 's23', 'num': 's24'},
    32: {'rparen': 's38'},
    33: {"vtype": "s4", 'assign': 's12', 'rbrace': 'r27', 'if': 's43', 'while': 's44', "return": 'r27'},
    34: {'rparen': 'r22'},
    35: {'vtype': 's45'},
    36: {'semi': 'r14', 'addsub': 's29', 'rparen': 'r14'},
    37: {'semi': 'r17', 'addsub': 'r17', 'multdiv': 's31', 'rparen': 'r17'},
    38: {'semi': 'r18', 'addsub': 'r18', 'multdiv': 'r18', 'rparen': 'r18'},
    39: {'return': 's49'},
    40: {"vtype": "s4", 'assign': 's12', 'rbrace': 'r27', 'if': 's43', 'while': 's44', "return": 'r27'},
    41: {'vtype': 'r28', 'assign': 'r28', 'rbrace': 'r28', 'if': 'r28', 'while': 'r28', "return": 'r28'},
    42: {'semi': 's51'},
    43: {'lparen': 's52'},
    44: {'lparen': 's53'},
    45: {"id": "s54"},
    46: {'semi': 'r13', "rparen": "r13"},
    47: {'semi': 'r16', "addsub": "r16", 'rparen': 'r16'},
    48: {'rbrace': 's55'},
    49: {'id': 's25', 'literal': 's18', 'character': 's19', 'boolstr': 's20', 'lparen': 's23', 'num': 's24'},
    50: {'rbrace': 'r26', 'return': 'r26'},
    51: {'vtype': 'r29', 'assign': 'r29', 'rbrace': 'r29', 'if': 'r29', 'while': 'r29', 'return': 'r29'},
    52: {'boolstr': 's58'},
    53: {'boolstr': 's58'},
    54: {'rparen': 'r25', 'comma': 's35'},
    55: {'id': 'r21', 'vtype': 'r21', "$": "r21"},
    56: {'semi': 's61'},
    57: {'rparen': 's62'},
    58: {'rparen': 'r34', 'comp': 's64'},
    59: {'rparen': 's65'},
    60: {'rparen': 'r24'},
    61: {'rbrace': 'r37'},
    62: {'lbrace': 's66'},
    63: {'rparen': 'r32'},
    64: {'boolstr': 's58'},
    65: {'lbrace': 's68'},
    66: {'vtype': 's4', 'assign': 's12', 'rbrace': 'r27', 'if': 's43', 'while': 's44', 'return': 'r27'},
    67: {'rparen': 'r33'},
    68: {'vtype': 's4', 'assign': 's12', 'rbrace': 'r27', 'if': 's43', 'while': 's44', 'return': 'r27'},
    69: {'rbrace': 's71'},
    70: {'rbrace': 's72'},
    71: {'vtype': 'r36', 'assign': 'r36', 'rbrace': 'r36', 'if': 'r36', 'while': 'r36', 'else': 's74', 'return': 'r36'},
    72: {'vtype': 'r31', 'assign': 'r31', 'rbrace': 'r31', 'if': 'r31', 'while': 'r31', 'return': 'r31'},
    73: {'vtype': 'r30', 'assign': 'r30', 'rbrace': 'r30', 'if': 'r30', 'while': 'r30', 'return': 'r30'},
    74: {'lbrace': 's75'},
    75: {'vtype': 's4', 'assign': 's12', 'rbrace': 'r27', 'if': 's43', 'while': 's44', 'return': 'r27'},
    76: {'rbrace': 's77'},
    77: {'vtype': 'r35', 'assign': 'r35', 'rbrace': 'r35', 'if': 'r35', 'while': 'r35', 'return': 'r35'},
}

# Dictionary for goto mapping of SLR table
goto_map = { 
    0: {"CODE'": 1, "VDECL": 2, "FDECL": 3},
    1: {"CODE": 6, "CODE'": 1, "VDECL": 2, "FDECL": 3},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {"VDECL'": 9, "ASSIGN": 11},
    8: {"ARG": 13},
    9: {},
    10: {},
    11: {},
    12: {"RHS": 16, "EXPR": 17, "TERM": 21, "FACTOR": 22},
    13: {},
    14: {},
    15: {},
    16: {},
    17: {},
    18: {},
    19: {},
    20: {},
    21: {"EXPR'": 28},
    22: {"TERM'": 30},
    23: {"EXPR": 32, "TERM": 21, "FACTOR": 22},
    24: {},
    25: {},
    26: {},
    27: {"MOREARGS": 34},
    28: {},
    29: {"FACTOR": 22, "TERM": 36},
    30: {},
    31: {"FACTOR": 37},
    32: {},
    33: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 39, "STMT": 40},
    34: {},
    35: {},
    36: {"EXPR'": 46},
    37: {"TERM'": 47},
    38: {},
    39: {"RETURN": 48},
    40: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 50, "STMT": 40},
    41: {},
    42: {},
    43: {},
    44: {},
    45: {},
    46: {},
    47: {},
    48: {},
    49: {"RHS": 56, "EXPR": 17, "TERM": 21, "FACTOR": 22},
    50: {},
    51: {},
    52: {"COND": 57},
    53: {"COND": 59},
    54: {"MOREARGS": 60},
    55: {},
    56: {},
    57: {},
    58: {"COND'": 63},
    59: {},
    60: {},
    61: {},
    62: {},
    63: {},
    64: {"COND": 67},
    65: {},
    66: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 69, "STMT": 40},
    67: {},
    68: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 70, "STMT": 40},
    69: {},
    70: {},
    71: {"ELSE": 73},
    72: {},
    73: {},
    74: {},
    75: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 76, "STMT": 40},
    76: {},
    77: {}
}