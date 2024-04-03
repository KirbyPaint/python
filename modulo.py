# modulo.py

import sys
assert sys.version_info >= (3, 10)

def main():
    modulo_day = int(sys.argv[1]) % 7
    match modulo_day:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        pass

main()
