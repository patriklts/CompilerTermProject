import sys
from stack import Stack
from typing import List
from ruleset import action_map, goto_map, derivations
from tree import TreeNode

def read_file_to_word_array(file_path: str) -> List[str]:   # Read the file and return the tokens as a list
    # Initialize an empty list to store the tokens
    tokens = []

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words and extend the list
            tokens.extend(line.strip().split())

    tokens.extend("$") # add the end of file symbol
    return tokens

def get_lhs(derivation_rule):                   # Get the left hand side of the given derivation rule
  parts = derivation_rule.split(" -> ")         # split the derivation rule by ' -> '
  return parts[0] if len(parts) > 0 else None   # return only left hand side, if it exists

def get_number_of_rhs_elements(derivation_rule): # Get the number of elements on the right hand side of the given derivation rule
  parts = derivation_rule.split(" -> ")          # split the derivation rule by ' -> '
  rhs_elements = [element for element in parts[1].split() if element != "''"] # remove empty strings/epsilon derivations
  return len(rhs_elements)                       # return the number of elements on the right hand side

def error_handling(index: int):
    # Get previous three and following three tokens
    prev_tokens = tokens[max(0, index - 3):index]
    next_tokens = tokens[index + 1:index + 4]
    # Print the error message
    print(f"Syntax error at token number: {index}, token: {tokens[index]}") 
    print(f"<<< {' '.join(prev_tokens)} {tokens[index]} {' '.join(next_tokens)} >>>")

    exit() # Exit the program
    
def accept_input(state):    
    # simulate derivation "CODE -> TYPE CODE" for the remaining nodes in the stack
    while node_stack.size() > 1:
        parent_node = TreeNode("CODE")  # simulate parent CODE node
        parent_node.add_child_at(node_stack.pop(), 0) # pop node from stackk and add as child
        parent_node.add_child_at(node_stack.pop(), 0)  
        node_stack.push(parent_node)    # push the parent node on the node stack
    
def reduce(action: str, index: int):    # Reduce based on given derivation rule  
    derivation_rule = int(action[1:])   # get the derivation rule number
    nonTerminal_of_derivation_rule = get_lhs(derivations[derivation_rule]) # get the non terminal of the derivation rule
    number_of_rhs_elements = get_number_of_rhs_elements(derivations[derivation_rule]) # get the number of elements on the right hand side of the derivation rule
    
    if (nonTerminal_of_derivation_rule is None): # if there is no derivation rule found
        error_handling(index)
                
    parent_node = TreeNode(nonTerminal_of_derivation_rule) # create a new parent node for this derivation, with non terminal as data
    
    # remove elements from the stack and add them as children to the parent node
    for _ in range(number_of_rhs_elements):
        stack.pop()                         # remove the state from the stack
        node = node_stack.pop()             # remove the node from the node stack
        parent_node.add_child_at(node, 0)   # add the node as a child to the parent node
        
    current_state = stack.peek() # get the current state
    
    stack.push(goto_map[current_state][nonTerminal_of_derivation_rule]) # push the new state on the stack based on goto map
    node_stack.push(parent_node) # push the parent node on the node stack
    
def shift(action: str, index: int): # Shift based on given action
    stack.push(int(action[1:]))     # push state of action on stack
    node = TreeNode(tokens[index])  # create a new node with the current token
    node_stack.push(node)           # push the node on the node stack
    
    return index + 1 # move the splitter to the right

def check_tokens(tokens: List[str]) -> TreeNode: # try slr parsing for list of token           
    index = 0   # starting index
    accepted = False # flag for accepted input
    
    while(not accepted):
        # check if for the given state and the token there is something in the action map
        current_state = stack.peek()
        next_input_symbol = tokens[index]

        if not tokens[index] in action_map[current_state]:  # if there is no action for the current state and the next input symbol   
            error_handling(index)

        action = action_map[current_state][next_input_symbol] # read the action from the action map 
        if action[0] == 'r':    # if action starts with r -> reduce
            reduce(action, index)

        elif action[0] == 's':  # if action starts with s -> shift
            index = shift(action, index)
                
        elif action == "acc":   # if action is acc -> accept
            accept_input(current_state)
            accepted = True     # set flag to true to exit loop
            
    return node_stack.pop() # return the root node of the parse tree
    
if __name__ == '__main__':
    if len(sys.argv) != 2: # check if input file was given
        print("Usage: python syntax_analyzer.py <path of input_file>")
        exit()
    
    input_file = sys.argv[1] # get the input file path
    
    stack = Stack()      # create a stack for the states
    stack.push(0)        # push start state to stack
    node_stack = Stack() # create a stack for the tree nodes
    
    tokens = read_file_to_word_array(input_file) # read file with tokens for token_list
    parse_tree_root = check_tokens(tokens)       # try slr parsing
    
    print("Parse tree: ")
    parse_tree_root.print_tree() # print the parse tree