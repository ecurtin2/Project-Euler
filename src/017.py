"""

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

"""

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used? 
NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

"""

import itertools
class NumConverter(object):

    numbers = {
        (0,0): '',
        (0,0,0):'-',
        (1,) : 'one',
        (2,) : 'two',
        (3,) : 'three', 
        (4,) : 'four',
        (5,) : 'five',
        (6,) : 'six',
        (7,) : 'seven',
        (8,) : 'eight',
        (9,) : 'nine',
        (1,0): 'ten',
        (1,1): 'eleven', 
        (1,2): 'twelve',
        (1,3): 'thirteen',
        (1,4): 'fourteen',
        (1,5): 'fifteen',
        (1,6): 'sixteen',
        (1,7): 'seventeen',
        (1,8): 'eighteen',
        (1,9): 'nineteen',
        (2,0): 'twenty',
        (3,0): 'thirty', 
        (4,0): 'forty',
        (5,0): 'fifty',
        (6,0): 'sixty',
        (7,0): 'seventy',
        (8,0): 'eighty',
        (9,0): 'ninety'    
    }

    
    def to_words(self, number):
        try: 
            number = tuple(int(i) for i in str(number).lstrip('0'))
        except:
            number = tuple(itertools.dropwhile(lambda x:x==0, number))
        if len(number) == 0:
            return ''
        
        if number in __class__.numbers.keys():
            return __class__.numbers[number]
        else:
            if len(number) == 2:
                return self.to_words_tens(number)
            if len(number) == 3:
                return self.to_words_hundreds(number)
            if len(number) == 4:
                return self.to_words_thousands(number)

            
    def to_words_tens(self, number):
        assert(len(number) == 2)
        l = []
        if number[0] != 0:
            l.append(__class__.numbers[(number[0], 0)])
            l.append('-')
        l.append(__class__.numbers[(number[1],)])
        return ''.join(l)
    
    def to_words_hundreds(self, number):
        assert(len(number) == 3)
        l = []
        l.append(__class__.numbers[number[0],])
        l.append(' hundred ')
        if (number[1] != 0) or number[2] != 0:
            l.append('and ')
        l.append(self.to_words(number[1:]))
        return ''.join(l)
    
    def to_words_thousands(self, number):
        assert(len(number) == 4)
        l = []
        l.append(__class__.numbers[number[0],])
        l.append(' thousand ')
        l.append(self.to_words(number[1:]))
        return ''.join(l)

N = 1000
n = NumConverter()
numbers = [n.to_words(i).replace(' ', '').replace('-', '')
           for i in range(1, 1001)]
print(sum(len(num) for num in numbers))