import os


def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.join(working_directory, directory)
        absolute_path = os.path.abspath(full_path)

        if directory == ".":
            formatted_directory = "current"
        else:
            formatted_directory = f"'{directory}'"

        result = f"Result for {formatted_directory} directory:\n"

        if working_directory not in absolute_path:
            return result + f'Error: Cannot list "{directory}" as it is outside the permitted working directory\n'

        if not os.path.isdir(full_path):
            return result + f"Error: {directory} is not a directory\n"

        for file in os.listdir(full_path):
            new_file = os.path.join(full_path, file)
            result += f"- {file}: file_size={os.path.getsize(new_file)}, is_dir={
                os.path.isdir(new_file)}\n"

    except Exception as e:
        return f"Error: {e}"

    return result
