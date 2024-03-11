import random


def random_walk(direction_probabilities, steps, start=(0, 0), increment=1, decrement=1):
    x, y = start
    for _ in range(steps):
        direction = random.choices(["F", "B", "L", "R"], weights=direction_probabilities)[0]
        if direction == 'F':
            y += increment
        elif direction == 'B':
            y -= decrement
        elif direction == 'L':
            x -= decrement
        else:
            x += increment
        print(f'Choose {direction} now position ({x}, {y})')
    return x, y


def main():
    direction_probabilities = []
    for direction in ['Forward', 'Backward', 'Left', 'Right']:
        d = float(input(f'Enter probability for {direction}: '))
        direction_probabilities.append(d)

    steps = int(input(f'Number of steps: '))

    x = int(input(f'Starting position x: '))
    y = int(input(f'Starting position y: '))
    starting_coordinate = (x, y)

    increment = int(input("Increment value: "))
    decrement = int(input("Decrement value: "))

    x, y = random_walk(direction_probabilities, steps, starting_coordinate, increment, decrement)
    print(f'Final position: {x}, {y}')


if __name__ == '__main__':
    main()
