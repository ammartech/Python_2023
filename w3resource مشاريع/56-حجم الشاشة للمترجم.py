import subprocess

def get_console_size():
    try:
        output = subprocess.check_output(["mode", "con"], shell=True).decode("utf-8")

        # Find the width and height values in the command output
        width_line = next(line for line in output.splitlines() if "Columns:" in line)
        height_line = next(line for line in output.splitlines() if "Lines:" in line)
        width = int(width_line.split(":", 1)[1])
        height = int(height_line.split(":", 1)[1])

        return width, height

    except:
        pass

    # Return default values if console size cannot be obtained
    return 80, 24

# Call the function to get the console size
console_width, console_height = get_console_size()

# Print the console width and height
print("Console Width:", console_width)
print("Console Height:", console_height)
