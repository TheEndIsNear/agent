
import os
MAX_CHARS = 10000


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.join(working_directory, file_path)
        absolute_path = os.path.abspath(full_path)

        if working_directory not in absolute_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory\n'

        if not os.path.isfile(full_path):
            return f"Error: File not found or is not a regular file: {file_path}\n"

        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)

    except Exception as e:
        return f"Error: {e}"

    if len(file_content_string) == MAX_CHARS:
        return file_content_string + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'

    return file_content_string
