from functools import reduce


def main():
    EQ = input("\nEnter the chemical equation. ex: CaCl2 = Ca2+ + 2Cl-\n")
    K = float(input("\nEnter the equilibrium constant\n"))
    
    EQ = [[[1, j] if j[0].isalpha() else [int(j[0]), j[1:]] \
        for j in i.split(" + ")] for i in EQ.split(" = ")]
    [[j.append(float(input("\nWhat is the concentration of " + j[1] + "? "))) \
        for j in i] for i in EQ]

    i = min([j[2] for j in EQ[0]] + [j[2] for j in EQ[1]]) / 2
    print("\n", newton(lambda x: f(EQ, K, x), i))
    

def newton(f, i, h = 0.0000000001):
    while abs(f(i)) > h:
        i -= (f(i) * h) / (f(i + h) - f(i))

    return i


def f(EQ, K, n):
    R = reduce(lambda x, y: x * y, [(j[2] - j[0] * n) ** j[0] for j in EQ[0]])
    P = reduce(lambda x, y: x * y, [(j[2] + j[0] * n) ** j[0] for j in EQ[1]])
    
    return P - K * R


if __name__ == "__main__":
    main()