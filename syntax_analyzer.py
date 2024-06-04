import sys
from stack import Stack
from typing import List
from ruleset import action_map, goto_map, derivations

def read_file_to_word_array(file_path: str) -> List[str]:
    # Initialize an empty list to store the words
    terminals = []

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words and extend the list
            terminals.extend(line.strip().split())

    return terminals

def reduce(action: str):
    # ToDo implement logic to reduce with derivations
    print("reduce")
    return -1
    
def shift(action: str):
    # ToDo implement logic to do shift operation   
    print("shift")  
    return -1

def check_tokens(tokens: List[str]):          
    stack = Stack()
    stack.push("$") # push acceptance token to stack
    stack.push(0)   # push start state to stack
    
    for index, token in enumerate(tokens):  # go through every token and perform slr parsing
        # check if for the given state and the token there is something in the action map
        if token in action_map[stack.peek()]:            
            action = action_map[stack.peek()][token] 
            print(action)
            if action[0] == 'r':    # if action starts with r -> reduce
                reduce(action)
            elif action[0] == 's':  # if action starts with s -> shift
                shift(action)
            else:
                print("Invalid action") # ToDo error handling einbauen
            
        # check if for the given state and the token there is something in the goto map (?, maybe falsch: nochmal durchsprechen)
        if token in goto_map[stack.peek()]:
            print("jetzt halt schauen welchen state man pushen muss")
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python syntax_analyzer.py <input file>")
        exit()
    
    input_file = sys.argv[1]
    check_tokens(read_file_to_word_array(sys.argv[1]))