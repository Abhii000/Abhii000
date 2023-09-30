import subprocess

# Specify the name of the batch file
batch_file_name = "ip.bat"

# Run the batch file using subprocess and capture the output
completed_process = subprocess.run(batch_file_name, text=True, capture_output=True)

# Get the captured standard output
output = completed_process.stdout

# Print the captured output

print(output)
