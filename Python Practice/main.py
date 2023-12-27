
pricebond : dict = {
    '123456': {
        'name': 'umer',
        'city': 'islamabad',
        'number': 123456,
        'price': 'Rs 1500',
        'date': '12/09/24',
        'CNIC': '37405-8642766-1'
    },
    '234567': {
        'name': 'ali',
        'city': 'karachi',
        'number': 234567,
        'price': 'Rs 2000',
        'date': '15/06/18',
        'CNIC': '54321-9876543-2'
    },
    '345678': {
        'name': 'zara',
        'city': 'lahore',
        'number': 345678,
        'price': 'Rs 1000',
        'date': '19/11/10',
        'CNIC': '98765-4321098-4'
    },
    '456789': {
        'name': 'ahmed',
        'city': 'rawalpindi',
        'number': 456789,
        'price': 'Rs 1500',
        'date': '20/04/05',
        'CNIC': '87654-3210987-5'
    },
    '567890': {
        'name': 'fariha',
        'city': 'quetta',
        'number': 567890,
        'price': 'Rs 1000',
        'date': '18/08/12',
        'CNIC': '23456-7890123-6'
    },
    '678901': {
        'name': 'saad',
        'city': 'peshawar',
        'number': 678901,
        'price': 'Rs 2000',
        'date': '22/02/28',
        'CNIC': '65432-1098765-7'
    },
    '789012': {
        'name': 'chief',
        'city': 'multan',
        'number': 789012,
        'price': 'Rs 1500',
        'date': '16/10/15',
        'CNIC': '10987-6543210-8'
    },
    '890123': {
        'name': 'ali',
        'city': 'sialkot',
        'number': 890123,
        'price': 'Rs 1000',
        'date': '17/03/22',
        'CNIC': '21098-7654321-9'
    },
    '901234': {
        'name': 'sadia',
        'city': 'gujranwala',
        'number': 901234,
        'price': 'Rs 1500',
        'date': '14/07/01',
        'CNIC': '32109-8765432-0'
    },
    '012345': {
        'name': 'usman',
        'city': 'faisalabad',
        'number': 12345,
        'price': 'Rs 2000',
        'date': '23/05/09',
        'CNIC': '43210-9876543-1'
    },
    '1234567': {
        'name': 'saba',
        'city': 'hyderabad',
        'number': 1234567,
        'price': 'Rs 1000',
        'date': '13/12/04',
        'CNIC': '54321-0987654-2'
    },
    '2345678': {
        'name': 'asad',
        'city': 'rawalakot',
        'number': 2345678,
        'price': 'Rs 1500',
        'date': '21/09/21',
        'CNIC': '65432-1098765-3'
    },
    '3456789': {
        'name': 'sana',
        'city': 'bahawalpur',
        'number': 3456789,
        'price': 'Rs 1000',
        'date': '15/02/14',
        'CNIC': '87654-3210987-4'
    },
    '4567890': {
        'name': 'umar',
        'city': 'sukkur',
        'number': 4567890,
        'price': 'Rs 2000',
        'date': '19/06/27',
        'CNIC': '98765-4321098-5'
    },
    '5678901': {
        'name': 'nida',
        'city': 'abbottabad',
        'number': 5678901,
        'price': 'Rs 1500',
        'date': '20/11/03',
        'CNIC': '23456-7890123-6'
    },
    '6789012': {
        'name': 'hamza',
        'city': 'muzaffarabad',
        'number': 6789012,
        'price': 'Rs 1000',
        'date': '18/04/08',
        'CNIC': '65432-1098765-7'
    },
    '7890123': {
        'name': 'tania',
        'city': 'jhelum',
        'number': 7890123,
        'price': 'Rs 2000',
        'date': '22/08/16',
        'CNIC': '10987-6543210-8'
    },
    '8901234': {
        'name': 'imran',
        'city': 'kasur',
        'number': 8901234,
        'price': 'Rs 1500',
        'date': '16/01/11',
        'CNIC': '21098-7654321-9'
    },
    '9012345': {
        'name': 'sadia',
        'city': 'attock',
        'number': 9012345,
        'price': 'Rs 1000',
        'date': '17/05/26',
        'CNIC': '32109-8765432-0'
    }
}
pricevalue : str = input("please enter your prizebond number:\t")
# print(f"Your prize bond number is {pricevalue}")

for i in pricebond:
   if pricevalue == i:
     print(f"{i} {pricebond[i]}")
     break
   else:
      print(f"The {pricevalue} you enter does not match")
      break


    
