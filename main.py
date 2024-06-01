import sys

def read_file_to_word_array(file_path):
    # Initialize an empty list to store the words
    words = []

    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read each line in the file
        for line in file:
            # Split the line into words and extend the list
            words.extend(line.strip().split())

    return words

def main(file_path):
    words_array = read_file_to_word_array(file_path)
    print(words_array)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python syntax_analyzer.py <input file>")
    else:
        input_file = sys.argv[1]
        main(input_file)
