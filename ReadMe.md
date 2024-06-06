# Syntax Analyzer

This Python program is a syntax analyzer that reads an input file containing tokens and then uses a stack-based parsing algorithm to create a parse tree, validating the syntax according to predefined grammar rules.

## Prerequisites

- Python 3.x installed on your system.

## Getting Started

### 1. Clone or Download the Repository

If you are using version control, clone the repository. Otherwise, download the script file `syntax_analyzer.py`.

### 2. Prepare the Input File

Create a text file (e.g., `your_file.txt`) with the content you want to analyze. Here’s an example:

**your_file.txt**
```
vtype id semi vtype id lparen rparen lbrace if lparen boolstr comp boolstr rparen lbrace rbrace
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
vtype id semi
```

The script will output:

```
Parse tree: 
CODE
|  ├── TYPE    
|  |  ├── vtype
|  |  └── CODE'
|  |     └── VDECL
|  |        ├── id
|  |        └── VDECL'
|  |           └── semi
|  └── CODE
```

## Troubleshooting

If you encounter any issues:

1. Ensure that Python 3.x is installed on your system.
2. Verify that the file path to your input file is correct.
3. Check the permissions of your input file to ensure it can be read by the script.
