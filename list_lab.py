# List Lab Starter
# Students: fill in code for Series 1–4 below

def series1():
    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)

    new_fruit = input('Add another fruit: ')
    fruits.append(new_fruit)
    print(fruits)

    num = int(input('Pick a number between 1 and 5: '))
    print(f'You picked {num}, which is {fruits[num - 1]}')

    fruits = ['Cherry'] + fruits
    print(fruits)

    for i in fruits:
        if i.startswith('P'):
            print(i)

def series2():
    # your code continues here, "pass" allows you to test your code with incomplete functions

    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    print(fruits)

    del fruits[3]
    print(f'Once removing the last fruit: {fruits}')

    delete_fruit = input('Enter a fruit to delete: ')
    if delete_fruit in fruits:
        fruits.remove(delete_fruit)
    print(fruits)

    fruits = fruits * 2
    print(fruits)
    while fruits:
        remove_fruit = input('Enter a fruit to remove again: ')
        if remove_fruit in fruits:
            fruits = [i for i in fruits if i != remove_fruit]
            break
        else:
            print('That fruit isn\'t in the list')
    print(fruits)


def series3():
    # your code continues here

    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    for i in fruits[:]:
        while True:
            answer = input(f'Do you like {i.lower()}? (yes or no): ').lower()
            if answer == 'no':
                fruits.remove(i)
                break
            elif answer == 'yes':
                break
            else:
                print("Answer either 'yes' or 'no'.")
    print('Final fruit list:', fruits)

def series4():
    # your code continues here
    pass

    fruits = ['Apples', 'Pears', 'Oranges', 'Peaches']
    reversed_fruits = [word[::-1] for word in fruits]
    print ('Origional list reversed and origional list minus the last item:')
    print(fruits[0:3])
    print(reversed_fruits)
    
def main():
    series1()
    series2()
    series3()
    series4()

# this just tells Python:
# "only run the code below if we are running THIS file directly"
# (not if another file tries to import this file)
# there is nothing to edit here
if __name__ == "__main__":
    main()
