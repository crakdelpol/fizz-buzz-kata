from unittest import TestCase


class FizzBuzz(object):

    def count(self, count):
        result = ""
        for index in range(1, count + 1):
            result = self.convert_to_game_string(index, result)

        return result

    def convert_to_game_string(self, number, result):

        if number % 3 == 0:
            result = result + "Fizz"

        if number % 5 == 0:
            result = result + "Buzz"

        if number % 3 != 0 and number % 5 != 0:
            result = result + str(number)

        return result + "\n"



class Test(TestCase):

    def test_print_first_number(self):
        self.assertEqual(
            "1\n",
            FizzBuzz().count(1)
        )

    def test_print_second_number(self):
        self.assertEqual(
            "1\n"
            "2\n",
            FizzBuzz().count(2)
        )

    def test_print_first_fizz(self):
        self.assertEqual(
            "1\n"
            "2\n"
            "Fizz\n",
            FizzBuzz().count(3)
        )

    def test_print_first_buzz(self):
        self.assertEqual(
            "1\n"
            "2\n"
            "Fizz\n"
            "4\n"
            "Buzz\n",
            FizzBuzz().count(5)
        )

    def test_print_second_fizz(self):
        self.assertEqual(
            "1\n"
            "2\n"
            "Fizz\n"
            "4\n"
            "Buzz\n"
            "Fizz\n",
            FizzBuzz().count(6)
        )

    def test_print_second_buzz(self):
        self.assertEqual(
            "1\n"
            "2\n"
            "Fizz\n"
            "4\n"
            "Buzz\n"
            "Fizz\n"
            "7\n"
            "8\n"
            "Fizz\n"
            "Buzz\n",
            FizzBuzz().count(10)
        )

    def test_acceptance_test(self):
        self.assertEqual(
            "1\n" +
            "2\n" +
            "Fizz\n" +
            "4\n" +
            "Buzz\n" +
            "Fizz\n" +
            "7\n" +
            "8\n" +
            "Fizz\n" +
            "Buzz\n" +
            "11\n" +
            "Fizz\n" +
            "13\n" +
            "14\n" +
            "FizzBuzz\n" +
            "16\n" +
            "17\n" +
            "Fizz\n" +
            "19\n" +
            "Buzz\n",
            FizzBuzz().count(20)
        )
