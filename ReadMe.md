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
### Run the Test Script

For your convenience, we have provided a test script to automate the execution of multiple test cases. To use the test script, follow these steps:

1. **Configuration**:
   - Locate the `config.py.sample` file in the repository.
   - Copy this file and rename it to `config.py`.
   - Open `config.py` and update the following details:
     - **Test Files Directory**: Specify the path to the directory containing your test files.
     - **Results File Location**: Specify the preferred location where the results file should be created.

2. **Running the Test Script**:
   - Open your terminal or command prompt.
   - Navigate to the directory where the test script is located.
   - Run the following command:

   ```sh
   python test_script.py
   ```

   If `python` defaults to Python 2.x on your system, use `python3` instead:

   ```sh
   python3 test_script.py
   ```

   This script will execute all the test cases found in your specified test files directory and generate a results file at the location specified in `config.py`.

By following these steps, you can easily manage and automate the testing process for the syntax analyzer using our provided test-cases.
## Troubleshooting

If you encounter any issues:

1. Ensure that Python 3.x is installed on your system.
2. Verify that the file path to your input file is correct.
3. Check the permissions of your input file to ensure it can be read by the script.
