
def print_sequence_until(last):
    """Prints the sequence of numbers taking into account 
    if they are even numbers it adds "buzz" to the line, 
    if its a multiple of 5, it adds "bazz"

    Args:
        last (int): the last number to be printed and checked.
    """
    for i in range(0, last+1):
        message = str(i)
        if i % 2 == 0:
            message += " buzz"
        if i % 5 == 0:
            message += " bazz"
        print(message)

if __name__ == '__main__':
    print_sequence_until(100)