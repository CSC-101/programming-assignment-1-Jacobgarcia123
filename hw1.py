import data

# Write your functions for each part in the space below.

# Part 1
# will find the vowels in a word capital and lower case
# input : any string in the case of my unittests input is Hello WORld?! and ICE cREaM
# output : the # of vowels in the input in the form of an integer type
def vowel_count(user_word:str) -> int:
    vowels = 'aeiouAEIOU'
    counter = sum(1 for vowel in user_word if vowel in vowels)
    return counter


# Part 2
# will take a list with type integers and create a new list from those
# with length 2 (contain two separate int)
# input : a list within a list of type integers
# output : a new list with only those lists in the list with a length of 2
def short_lists(lists:list[list[int]])-> list[list[int]]:
    return [newlist for newlist in lists if len(newlist) == 2]

# Part 3
# will take a list with lists of type int and
# reorder them from least to greatest
# input: a list within a list of type integers
# output: a new list with the reordered list of those with
# length = 2 from least to greatest *others left the same*
def ascending_pairs(lists:list[list[int]]) -> list[list[int]]:
    return [sorted(newlist) if len(newlist) == 2 else newlist for newlist in lists]


# Part 4
# will take two prices and add them together
# making sure that if the cents is > 99 it becomes a dollar
# input: two inputs *for two prices* of type int
# output: both prices added up and
# if the cents surpass 99 it becomes a dollar
def add_prices(price_1:int,price_2:int) -> int:
    total_dollars = price_1[0] + price_2[0]
    total_cents = price_1[1] + price_2[1]
    total_dollars += total_cents // 100
    total_cents = total_cents % 100
    return (total_dollars,total_cents)



# Part 5
# calculate the area of a rectangle
# input: all 4 coordinates of the corner of the rectangle
# output: the area of the rectangle
def rectangle_area(rect:int) -> int:
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    return width * height

# Part 6
# Give you books by the given author
# input: the authors name so it can search for which books
# are associated with that author
# output: give you a list of books which correlate to the given author
def books_by_author(author_name:str,books:list) -> list:
    return [book for book in books if book[1] == author_name]


# Part 7
# need help



# Part 8
# Calculate which employees are being paid less than the average
# input: different employees and their salary
# output: who of the employee(s) are being being paid less
def below_pay_average(employees:list) -> list[str]:
    if not employees:
        return[]
    total_pay = sum(employee[1] for employee in employees)
    average_pay = total_pay / len(employees)
    below_average_pay = [employee[0] for employee in employees if employee[1] < average_pay]
    return below_average_pay



