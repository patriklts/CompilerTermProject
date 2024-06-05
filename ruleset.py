# ruleset.py

# Dictionary for derivations 
derivations = {
    0 : "CODE -> TYPE CODE",  
    1 : "CODE -> ''",
    2 : "TYPE -> vtype CODE'",
    3 : "CODE' -> VDECL",
    4 : "CODE' -> FDECL",
    5 : "VDECL -> id VDECL'",
    6 : "VDECL' -> semi",
    7 : "VDECL' -> ASSIGN semi",
    8 : "ASSIGN -> assign RHS",
    9 : "RHS -> EXPR",
    10 : "RHS -> literal ",
    11 : "RHS -> character", 
    12 : "RHS -> boolstr",
    13 : "EXPR -> TERM EXPR'",
    14 : "EXPR' -> addsub TERM EXPR'",
    15 : "EXPR' -> ''",
    16 : "TERM -> FACTOR TERM'",
    17 : "TERM' -> multdiv FACTOR TERM'",
    18 : "TERM' -> ''",
    29 : "FACTOR -> lparen EXPR rparen",
    20 : "FACTOR -> num",
    21 : "FACTOR -> id",
    22 : "FDECL -> id lparen ARG rparen lbrace BLOCK RETURN rbrace",
    23 : "ARG -> vtype id MOREARGS ",
    24 : "ARG -> ''",
    25 : "MOREARGS -> comma vtype id MOREARGS ",
    26 : "MOREARGS -> ''",
    27 : "BLOCK -> STMT BLOCK", 
    28 : "BLOCK -> ''",
    29 : "STMT -> VDECL",
    30 : "STMT -> ASSIGN semi",
    31 : "STMT -> if lparen COND rparen lbrace BLOCK rbrace ELSE",
    32 : "STMT -> while lparen COND rparen lbrace BLOCK rbrace",
    33 : "COND -> boolstr COND'",
    34 : "COND' -> comp COND",
    35 : "COND' -> ''",
    36 : "ELSE -> else lbrace BLOCK rbrace", 
    37 : "ELSE -> ''",
    38 : "RETURN -> return RHS semi"
}

# Dictionary for action mapping of SLR table
action_map = {
    0: {'vtype': 's2'},
    1: {'vtype': 's2', '$': 'r1'},
    2: {'id': 's7'},
    3: {'$': 'acc'},    # TODO eigentlich muss hier CODE -> TYPE CODE reduziert werden und dann noch GOTO map prüfen, ob endlos Schleife. Dann halt auch die Logik anpassen, ab wann es akzeptiert wird
    4: {'vtype': 'r2', '$': 'r2'},
    5: {'vtype': 'r3', '$': 'r3'},
    6: {'vtype': 'r4', '$': 'r4'},
    7: {'semi': 's10', 'assign': 's12', 'lparen': 's9'},
    8: {'vtype': 'r5', 'id': 'r5', 'assign': 'r5', 'rbrace': 'r5', 'if': 'r5', 'while': 'r5', 'return': 'r5', '$': 'r5'},
    9: {'vtype': 's14', 'rparen': 'r24'},
    10: {'vtype': 'r6', 'id': 'r6', 'assign': 'r6', 'rbrace': 'r6', '$': 'r6', 'if': 'r6', 'while': 'r6', 'return': 'r6'},
    11: {'semi': 's15'},
    12: {'id' : 's25', 'literal': 's18', 'character': 's19', 'boolstr': 's20', 'lparen': 's23', 'num': 's24'},
    13: {'rparen': 's26'},
    14: {'id': 's27'},
    15: {'vtype': 'r7', 'id': 'r7', 'assign': 'r7', 'rbrace': 'r7', 'if': 'r7', 'while': 'r7', 'return': 'r7', '$': 'r7'},
    16: {'semi': 'r8'},
    17: {'semi': 'r9'},
    18: {'semi': 'r10'},
    19: {'semi': 'r11'},
    20: {'semi': 'r12'},
    21: {'semi': 'r15', 'addsub': 's29', 'rparen': 'r15'},
    22: {'semi': 'r18', 'addsub': 'r18', 'multdiv': 's31', 'rparen': 'r18'},
    23: {'id': 's25', 'lparen': 's23', 'num': 's24'},
    24: {'semi': 'r20', 'addsub': 'r20', 'multdiv': 'r20', 'rparen': 'r20'},
    25: {'semi': 'r21', 'addsub': 'r21', 'multdiv': 'r21', 'rparen': 'r21'},
    26: {'lbrace': 's33'},
    27: {'rparen': 'r26', 'comma': 's35'},
    28: {'semi': 'r13', 'rparen': 'r13'},
    29: {'id': 's25', 'lparen': 's23', 'num': 's24'},
    30: {'semi': 'r16', 'addsub': 'r16', 'rparen': 'r16'},
    31: {'id': 's25', 'lparen': 's23', 'num': 's24'},
    32: {'rparen': 's38'},
    33: {'id': 's45', 'assign': 's12', 'rbrace': 'r28', 'if': 's43', 'while': 's44', "return": 'r28'},
    34: {'rbrace': 'r23'},
    35: {'vtype': 's46'},
    36: {'semi': 'r15', 'addsub': 's29', 'rparen': 'r15'},
    37: {'addsub': 'r18', 'addsub': 'r18', 'multdiv': 's31', 'rparen': 'r18'},
    38: {'addsub': 'r19', 'addsub': 'r19', 'multdiv': 'r19', 'rparen': 'r19'},
    39: {'return': 's50'},
    40: {'id': 's45', 'assign': 's12', 'rbrace': 'r28', 'if': 's43', 'while': 's44', "return": 'r28'},
    41: {'id': 'r29', 'assign': 'r29', 'rbrace': 'r29', 'if': 'r29', 'while': 'r29', "return": 'r29'},
    42: {'semi': 's52'},
    43: {'lparen': 's53'},
    44: {'lparen': 's54'},
    45: {'semi': 's10', 'assign': 's12'},
    46: {'id': 's55'},
    47: {'semi': 'r14', 'rparen': 'r14'},
    48: {'semi': 'r17', 'addsub': 'r17', 'rparen': 'r17'},
    49: {'rbrace': 's56'},
    50: {'id': 's25', 'literal': 's18', 'character': 's19', 'boolstr': 's20', 'lparen': 's23', 'num': 's24'},
    51: {'rbrace': 'r27', 'return': 'r27'},
    52: {'id': 'r30', 'assign': 'r30', 'rbrace': 'r30', 'if': 'r30', 'while': 'r30', 'return': 'r30'},
    53: {'boolstr': 's59'},
    54: {'boolstr': 's59'},
    55: {'rparen': 'r26', 'comma': 's35'},
    56: {'$': 'r22', 'vtype': 'r22'},
    57: {'semi': 's62'},
    58: {'rparen': 's63'},
    59: {'rparen': 'r35', 'comp': 's65'},
    60: {'rparen': 's66'},
    61: {'rparen': 'r25'},
    62: {'rbrace': 'r38'},
    63: {'lbrace': 's67'},
    64: {'rparen': 'r33'},
    65: {'boolstr': 's59'},
    66: {'lbrace': 's69'},
    67: {'id': 's45', 'assign': 's12', 'rbrace': 'r28', 'if': 's43', 'while': 's44', 'return': 'r28'},
    68: {'rparen': 'r34'},
    69: {'id': 's45', 'assign': 's12', 'rbrace': 'r28', 'if': 's43', 'while': 's44', 'return': 'r28'},
    70: {'rbrace': 's72'},
    71: {'rbrace': 's73'},
    72: {'id': 'r37', 'assign': 'r37', 'rbrace': 'r37', 'if': 'r37', 'while': 'r37', 'else': 's75', 'return': 'r37'},
    73: {'id': 'r32', 'assign': 'r32', 'rbrace': 'r32', 'if': 'r32', 'while': 'r32', 'return': 'r32'},
    74: {'id': 'r31', 'assign': 'r31', 'rbrace': 'r31', 'if': 'r31', 'while': 'r31', 'return': 'r31'},
    75: {'lbrace': 's76'},
    76: {'id': 's45', 'assign': 's12', 'rbrace': 'r28', 'if': 's43', 'while': 's44', 'return': 'r28'},
    77: {'rbrace': 's78'},
    78: {'id': 'r36', 'assign': 'r36', 'rbrace': 'r36', 'if': 'r36', 'while': 'r36', 'return': 'r36'},
}

# Dictionary for goto mapping of SLR table
goto_map = { 
    0: {"TYPE": 1},
    1: {"CODE": 3, "TYPE": 1},
    2: {"CODE'": 4, "VDECL": 5, "FDECL": 6},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {"VDECL'": 8, "ASSIGN": 11},
    8: {},
    9: {"ARG": 13},
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
    29: {"FACTOR": 22},
    30: {},
    31: {"FACTOR": 37},
    32: {},
    33: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 39, "STMT": 40},
    34: {},
    35: {},
    36: {"EXPR'": 47},
    37: {"TERM'": 48},
    38: {},
    39: {"RETURN": 49},
    40: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 51, "STMT": 40},
    41: {},
    42: {},
    43: {},
    44: {},
    45: {"VDECL'": 8, "ASSIGN": 11},
    46: {},
    47: {},
    48: {},
    49: {},
    50: {"RHS": 57, "EXPR": 17, "TERM": 21, "FACTOR": 22},
    51: {},
    52: {},
    53: {"COND": 58},
    54: {"COND": 60},
    55: {"MOREARGS": 61},
    56: {},
    57: {},
    58: {},
    59: {"COND'": 64},
    60: {},
    61: {},
    62: {},
    63: {},
    64: {},
    65: {"COND": 68},
    66: {},
    67: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 70, "STMT": 40},
    68: {},
    69: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 71, "STMT": 40},
    70: {},
    71: {},
    72: {"ELSE": 74},
    73: {},
    74: {},
    75: {},
    76: {"VDECL": 41, "ASSIGN": 42, "BLOCK": 77, "STMT": 40},
    77: {},
    78: {}
}