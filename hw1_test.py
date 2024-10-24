import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    #part 1
    def test_vowel_count_1(self):
        input = 'Hello WORld?!'
        result = hw1.vowel_count(input)
        expected = 3
        self.assertEqual(expected,result)
    def test_vowel_count_2(self):
        input = 'ICE cREaM'
        result = hw1.vowel_count(input)
        expected = 4
        self.assertEqual(expected,result)

   #part 2
    def test_short_lists_1(self):
        input = [[4,3],[],[5],[99,45]]
        result = hw1.short_lists(input)
        expected = [[4,3],[99,45]]
        self.assertEqual(expected,result)
    def test_short_lists_2(self):
        input = [[6,7,8],[56,1],[1],[888]]
        result = hw1.short_lists(input)
        expected = [[56,1]]
        self.assertEqual(expected,result)

    #part 3
    def test_ascending_pairs_1(self):
        input = [[5,2],[3],[9,8],[0,0],[3,4,2]]
        result = hw1.ascending_pairs(input)
        expected = [[2,5],[3],[8,9],[0,0],[3,4,2]]
        self.assertEqual(expected,result)
    def test_ascending_pairs_2(self):
        input = [[7,3],[],[5,5],[2,1]]
        result = hw1.ascending_pairs(input)
        expected = [[3,7],[],[5,5],[1,2]]
        self.assertEqual(expected,result)

    #part 4
    def test_add_prices_1(self):
        input = (6,50)
        input2 = (8,20)
        result = hw1.add_prices(input,input2)
        expected = (14,70)
        self.assertEqual(expected,result)
    def test_add_prices_2(self):
        input = (4,99)
        input2 = (5,60)
        result = hw1.add_prices(input,input2)
        expected = (10,59)
        self.assertEqual(expected,result)

    #Part 5
    def test_rectangle_area_1(self):
        input = (1,2,4,5)
        result = hw1.rectangle_area(input)
        expected = 9
        self.assertEqual(expected,result)
    def test_rectangle_area_2(self):
        input = (3,4,8,9)
        result = hw1.rectangle_area(input)
        expected = 25
        self.assertEqual(expected,result)

    # part 6
    def test_books_by_author_1(self):
        book1 = ('Just Kids','Patti Smith')
        book2 = ('M Train','Patti Smith')
        book3 = ('The Bluest Eye','Toni Morrison')
        input = ("Patti Smith")
        input2 = [book1,book2,book3]
        result = hw1.books_by_author(input,input2)
        expected = [('Just Kids', 'Patti Smith'), ('M Train', 'Patti Smith')]
        self.assertEqual(expected,result)
    def test_books_by_author_2(self):
        book1 = ('Beloved','Toni Morrison')
        book2 = ('M Train','Patti Smith')
        book3 = ('The Bluest Eye','Toni Morrison')
        input = ("Toni Morrison")
        input2 = [book1,book2,book3]
        result = hw1.books_by_author(input,input2)
        expected = [('Beloved', 'Toni Morrison'), ('The Bluest Eye', 'Toni Morrison')]
        self.assertEqual(expected,result)

    # part 8
    def test_below_pay_average_1(self):
        employees_working = [('Ben', 3000), ('Henry',9000),('Jane',7000)]
        input = (employees_working)
        result = hw1.below_pay_average(input)
        expected = ['Ben']
        self.assertEqual(expected,result)

    def test_below_pay_average_2(self):
        employees_working = [('Janet', 5000), ('Jake', 5000), ('Mary', 5000)]
        input = (employees_working)
        result = hw1.below_pay_average(input)
        expected = []
        self.assertEqual(expected, result)





if __name__ == '__main__':
    unittest.main()
