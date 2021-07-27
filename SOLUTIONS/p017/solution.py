def get_length_of_longest_absolut_path_for_a_file(file_system_represenation: str) -> int:
    stack = list()
    stack.append(0)
    longest_path_length = 0
    delimiter = '/'
    for item in file_system_represenation.split('\n'):
        num_tabs = __get_number_of_tabs(item)
        if not __is_valid_indented(len(stack) - 1, num_tabs):
            raise InvalidFormatError

        for _ in range((len(stack) - 1) - num_tabs):
            stack.pop()
        item = item[num_tabs:]
        if __is_directory(item):
            stack.append(stack[-1] + len(item) + len(delimiter))
        elif __is_file(item):
            longest_path_length = max(stack[-1] + len(item), longest_path_length)
        else:
            assert True 'This case is not coverd in this solution'
    return longest_path_length


def __is_file(item :str)-> bool:
    return '.' in item and item[-1] != '.'

def __is_directory(item :str) -> bool:
    return '.' not in item

def __is_valid_indented(current_indentation_level :int, num_tabs :int) -> bool:
    return 0 <= current_indentation_level - num_tabs

def __get_number_of_tabs(item :str) -> int:
    for i,c in enumerate(item):
        if c != '\t':
            return i
    return len(item)


class InvalidFormatError(ValueError):
    pass


import unittest


class TestBoundedOrderLog(unittest.TestCase):

    def test_given_example(self):
        file_system = """
        dir
        \tsubdir1
        \t\tfile1.ext
        \t\tsubsubdir1
        \tsubdir2
        \t\tsubsubdir2
        \t\t\tfile2.ext
        """.replace(" ", "")
        longest_path = "dir/subdir2/subsubdir2/file2.ext"
        self.assertEqual(get_length_of_longest_absolut_path_for_a_file(file_system), len(longest_path))


    def test_invalid_format_error(self):
        file_system = """
        dir
        \tsubdir
        \t\t\tsubsubsubdir
        \t\tsubsubdir
        """.replace(" ", "")
        with self.assertRaises(InvalidFormatError):
            get_length_of_longest_absolut_path_for_a_file(file_system)
        
        file_system = """
        dir
        \tsubdir
        \t\tfile.ext
        \t\t\tsubfile
        """.replace(" ", "")
        with self.assertRaises(InvalidFormatError):
            get_length_of_longest_absolut_path_for_a_file(file_system)

    
    def test_no_file(self):
        file_system = """
        dir
        \tsubdir1
        \t\tsubsubdir11
        \t\tsubsubdir12
        \tsubdir2
        \t\tsubsubdir2
        \t\t\tsubsubsubdir2
        """.replace(" ", "")
        longest_path = ""
        self.assertEqual(get_length_of_longest_absolut_path_for_a_file(file_system), len(longest_path))
    

    def test_empty_input(self):
        file_system = ""
        longest_path = ""
        self.assertEqual(get_length_of_longest_absolut_path_for_a_file(file_system), len(longest_path))


if __name__ == "__main__":
    unittest.main()