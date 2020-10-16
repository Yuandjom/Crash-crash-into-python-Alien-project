import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ Tests for 'name_function.py' """
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        fomratted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(fomratted_name,'Janis Joplin')

    def test_first_middle_last_name(self):
        """ Do names likfe 'Wolfgang Amadeus Mozart' work? """
        formatted_name = get_formatted_name(
            'wolfgang','mozart','amadeus'
        )
        self.assertEqual(formatted_name,"Wolfgang Amadeus Mozart")

if __name__ == '__main__' :
    unittest.main()