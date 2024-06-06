import os
import subprocess
from config import TEST_FILES_DIR, TEST_FILE_OUTPUT

# Load the environment variables from the .env file
test_files_dir = TEST_FILES_DIR
output_file = TEST_FILE_OUTPUT

# Open the output file with utf-8 encoding
with open(output_file, "w", encoding="utf-8") as out_file:
    # Iterate over all files in the test_files directory
    for filename in os.listdir(test_files_dir):
        # Construct the full file path
        file_path = os.path.join(test_files_dir, filename)
        # Set the PYTHONIOENCODING environment variable to 'utf-8'
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        # Execute the syntax_analyzer.py script with the file as argument and capture the output as bytes
        result = subprocess.run(["python", "syntax_analyzer.py", file_path], stdout=subprocess.PIPE, env=env)
        # Decode the output using 'utf-8'
        output = result.stdout.decode('utf-8')
        # Split the output into lines and remove unnecessary blank lines while preserving structure
        lines = [line for line in output.split("\n") if line.strip()]
        # If there is output, write the file name and the output to the file
        if lines:
            out_file.write(f"Output for {filename}:\n")
            out_file.write("\n".join(lines) + "\n\n")

