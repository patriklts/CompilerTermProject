# Syntax Analyzer

This script reads a text file and stores each word in an array. It then prints the array to the console.

## Prerequisites

- Python 3.x installed on your system.

## Getting Started

### 1. Clone or Download the Repository

If you are using version control, clone the repository. Otherwise, download the script file `syntax_analyzer.py`.

### 2. Prepare the Input File

Create a text file (e.g., `your_file.txt`) with the content you want to analyze. Here’s an example:

**your_file.txt**
```
Hello World
This is a test file
With multiple lines
```

### 3. Run the Script

Open your terminal or command prompt, navigate to the directory where `syntax_analyzer.py` and your input file (e.g., `your_file.txt`) are located, and run the following command:

```sh
python syntax_analyzer.py your_file.txt
```

If `python` defaults to Python 2.x on your system, use `python3` instead:

```sh
python3 syntax_analyzer.py your_file.txt
```

### Example Output

For an input file `your_file.txt` with the following content:

```
Hello World
This is a test file
With multiple lines
```

The script will output:

```
['Hello', 'World', 'This', 'is', 'a', 'test', 'file', 'With', 'multiple', 'lines']
```

## Usage

```sh
python syntax_analyzer.py <input_file>
```

Replace `<input_file>` with the path to your text file.

## Code Explanation

The script contains two main functions:

1. `read_file_to_word_array(file_path)`: Reads the file at `file_path`, splits its content into words, and returns a list of words.
2. `main(file_path)`: Calls `read_file_to_word_array(file_path)` and prints the resulting list of words.

The script also includes an execution block that handles command-line arguments:

```python
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python syntax_analyzer.py <input file>")
    else:
        input_file = sys.argv[1]
        main(input_file)
```

This ensures that the script is executed with the correct number of arguments and provides usage instructions if the arguments are incorrect.

## Troubleshooting

If you encounter any issues:

1. Ensure that Python 3.x is installed on your system.
2. Verify that the file path to your input file is correct.
3. Check the permissions of your input file to ensure it can be read by the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
