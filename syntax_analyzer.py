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

    terminals.extend("$")
    return terminals

def reduce(action: str, index: int):
    # ToDo implement logic to reduce with derivations
    print("reduce")
    #ToDo goto handling
    return -1
    
def shift(action: str, index: int):
    stack.push(int(action[1:])) # push state on stack
    return index + 1

def check_tokens(tokens: List[str]):          
    index = 0
    
    while(True):
        # check if for the given state and the token there is something in the action map
        state = stack.peek()

        if not tokens[index] in action_map[state]:            
            print("error handling bitte")
            break

        action = action_map[state][tokens[index]] 

        if action[0] == 'r':    # if action starts with r -> reduce
           reduce(action, index)

        elif action[0] == 's':  # if action starts with s -> shift
            index = shift(action, index)
                
        elif action == "acc":     # if action is acc -> accept
            print("accept")     # ToDo: implement accept logic
            break

        print(index, stack.peek())
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python syntax_analyzer.py <input file>")
        exit()
    
    input_file = sys.argv[1]
    stack = Stack()
    stack.push(0)   # push start state to stack
    check_tokens(read_file_to_word_array(input_file))