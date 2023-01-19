#!usr/bin/python3
"""
New module to learn inheritance

Inherited class and perfom tests
"""


class MyList(list):
    """
    Mylist that inherits from list class
    """

    def print_sorted(self):
        """
        sort the list (asc)
        """

        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
