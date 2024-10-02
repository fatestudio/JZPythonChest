import subprocess

# Run a simple shell command and capture the output
result = subprocess.run(["echo", "Hello, World!"],
                        capture_output=True,
                        text=True)

# Print the output and return code
print(f"Output: {result.stdout}")
print(f"Return Code: {result.returncode}")
