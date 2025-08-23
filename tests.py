import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file


class TestFunctions(unittest.TestCase):
    def test_one(self):
        result = get_files_info("calculator", ".")
        expected_result = (
            "Result for current directory:\n"
            "- tests.py: file_size=1343, is_dir=False\n"
            "- pkg: file_size=4096, is_dir=True\n"
            "- main.py: file_size=576, is_dir=False\n"
        )
        self.assertEqual(result, expected_result)

    def test_two(self):
        result = get_files_info("calculator", "pkg")
        expected_result = (
            "Result for 'pkg' directory:\n"
            "- calculator.py: file_size=1738, is_dir=False\n"
            "- render.py: file_size=783, is_dir=False\n"
        )
        self.assertEqual(result, expected_result)

    def test_outside_of_working_directory(self):
        result = get_files_info("calculator", "/bin")
        expected_result = (
            "Result for '/bin' directory:\n"
            "Error: Cannot list \"/bin\" as it is outside the permitted working directory\n"
        )
        self.assertEqual(result, expected_result)

    def test_outside_of_working_directory2(self):
        result = get_files_info("calculator", "../")
        expected_result = (
            "Result for '../' directory:\n"
            "Error: Cannot list \"../\" as it is outside the permitted working directory\n"
        )
        self.assertEqual(result, expected_result)

    def test_file_outside_of_working_directory(self):
        result = get_file_content("calculator", "/bin/cat")
        expected_result = 'Error: Cannot read "/bin/cat" as it is outside the permitted working directory\n'
        self.assertEqual(result, expected_result)

    def test_file_that_does_not_exist(self):
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        expected_result = 'Error: File not found or is not a regular file: pkg/does_not_exist.py\n'
        self.assertEqual(result, expected_result)

    def test_writing_to_file(self):
        result = write_file("calculator", "lorem.txt",
                            "wait, this isn't lorem ipsum")
        print(result)
        result = write_file("calculator", "pkg/morelorem.txt",
                            "lorem ipsum dolar sit amet")
        print(result)

    def test_writing_to_non_permitted_location(self):
        result = write_file("calculator", "/tmp/tmp.txt",
                            "this should not be allowed")
        expected_result = 'Error: Cannot write to "/tmp/tmp.txt" as it is outside the permitted working directory\n'
        self.assertEqual(result, expected_result)
        print(result)


if __name__ == "__main__":
    unittest.main()
