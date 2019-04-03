def handle_numbers(number1, number2, number3):
  return [x for x in range(number1,number2+1) if x % number3 == 0]
print(handle_numbers(1,10,2))


def handle_string (text):
    return {
      "digits": len([x for x in text if x.isdigit()]),
      "letters": len([x for x in text if x.isalpha()])
      }
print(handle_string('Hello, World! 123!'))


def handle_list_of_tuples(list):
    list.sort(key=lambda tup: tup[0])
    return list
print(handle_list_of_tuples([
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
    ]))