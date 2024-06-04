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

def get_lhs(derivation_rule):
  """Extracts the left-hand side (LHS) of a derivation rule.

  Args:
      derivation_rule: The string representing the derivation rule.

  Returns:
      The left-hand side (non-terminal) of the rule, or None if no "->" is found.
  """
  parts = derivation_rule.split(" -> ")
  return parts[0] if len(parts) > 0 else None

def error_handling():
    # TODO proper error handling
    exit()

def reduce(action: str, index: int):
    print(action)
    stack.pop() # TODO pop so oft wie rechtse seite elemente hat
    derivation_rule = int(action[1:])
    nonTerminal_of_derivation_rule = get_lhs(derivations[derivation_rule])
    if (nonTerminal_of_derivation_rule is None):
        print("The derivation rule: ", derivation_rule, " does not exist" )
        error_handling()
    # TODO parse tree hier erstellen! mithilfe der derivation rule
    current_state = stack.peek()
    stack.push(goto_map[current_state][nonTerminal_of_derivation_rule])
    
def shift(action: str, index: int):
    print(action)
    stack.push(int(action[1:])) # push state on stack
    return index + 1 # move the splitter to the right

def check_tokens(tokens: List[str]):          
    index = 0
    
    while(True):
        # check if for the given state and the token there is something in the action map
        current_state = stack.peek()
        next_input_symbol = tokens[index]

        if not tokens[index] in action_map[current_state]:            
            print("error handling bitte")
            break

        action = action_map[current_state][next_input_symbol] 

        if action[0] == 'r':    # if action starts with r -> reduce
           reduce(action, index)

        elif action[0] == 's':  # if action starts with s -> shift
            index = shift(action, index)
                
        elif action == "acc":     # if action is acc -> accept
            print("accept")     # TODO: implement accept logic
            break

        print(index, stack.peek())
        
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python syntax_analyzer.py <input file>")
        exit()
    
    input_file = sys.argv[1]
    stack = Stack()
    stack.push(0)   # push start state to stack
    tokens = read_file_to_word_array(input_file) #array with our non terminals and terminals
    check_tokens(tokens)