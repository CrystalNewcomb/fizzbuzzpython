# build a function
# returns Fizz when int divisible by 3
# returns Buzz when int divisible by 5
# returns FizzBuzz when int divisible by 3 + 5
# returns Taco when not divisible

def fizz_buzz(num) -> list[str]:
    answer = []
    for num in range(0, num):
        if num % 15 == 0:
            answer.append('FizzBuzz')
        elif num % 3 == 0:
            answer.append('Fizz')
        elif num % 5 == 0:
            answer.append('Buzz')
        else:
            answer.append('Taco')
    return answer


# pass a list


def fizz_buzz_list(random_list) -> [str]:
    answer = []
    for i in random_list:
        if i % 15 == 0:
            answer.append('FizzBuzz')
        elif i % 3 == 0:
            answer.append('Fizz')
        elif i % 5 == 0:
            answer.append('Buzz')
        else:
            answer.append('Taco')
    return answer

# pass a dict


def fizz_buzz_dict(random_dict) -> {}:
    answer = []
    for value in random_dict.values():
        if value % 15 == 0:
            answer.append('FizzBuzz')
        elif value % 3 == 0:
            answer.append('Fizz')
        elif value % 5 == 0:
            answer.append('Buzz')
        else:
            answer.append('Taco')
    return answer




