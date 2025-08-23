import os


def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(full_path)

        if working_directory not in absolute_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory\n'

        directory = os.path.dirname(full_path)

        if directory and not os.path.exists(directory):
            os.makedirs(directory, exist_ok=True)

        with open(full_path, "w") as f:
            f.write(content)

    except Exception as e:
        return f"Error: {e}"

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
