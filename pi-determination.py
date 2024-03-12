import random


def pi_determination(r, steps):
    M, N = 0, steps
    for _ in range(steps):
        R1 = random.uniform(0, r)
        R2 = random.uniform(0, r)

        if R1 ** 2 + R2 ** 2 <= r ** 2:
            M += 1

    return M, N


def main():
    r = int(input("Input radius: "))
    steps = int(input("Num simulations: "))
    M, N = pi_determination(r, steps)

    pi = (M / N) * 4
    print(f'Pi value: {pi}')


if __name__ == '__main__':
    main()
