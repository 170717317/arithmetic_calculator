import re


def arithmetic_arranger(problems, solve=True):
    string = ""
    primero = ""
    segundo = ""
    lines = ""
    sumx = ""

    for problem in problems:
        if re.search("[^\s0-9,+-]", problem):
            print("Error! Only Digits Are Accepted! ")
            # break
            if re.search("[/]", problem) or re.search("[*]", problem):
                print("Error! Cannot Multiply Or Divide!")
            break
        numbers = problem.split(" ")
        first = numbers[0]
        op = numbers[1]
        second = numbers[2]

        if len(first) >= 5 or len(second) >= 5:
            print("Error! Each Number Needs 5 Or Less Digits")

        solution = ""
        first = int(first)
        second = int(second)

        if op == '+':
            solution = str(first + second)
        elif op == '-':
            solution = str(first - second)

        first = str(first)
        second = str(second)
        length = max(len(first), len(second))

        top = first.rjust(length + 2)
        bottom = op + second.rjust(length + 1)
        line = ""
        answer = solution.rjust(length + 2)

        for s in range(length + 2):
            line += "-"

        if problem != problems[-1]:
            primero += top + '     '
            segundo += bottom + '     '
            lines += line + '     '
            sumx += answer + '     '
        else:
            primero += top
            segundo += bottom
            lines += line
            sumx += answer

        if solve == True:
            string = primero + '\n' + segundo + '\n' + lines + '\n' + sumx
        else:
            string = primero + '\n' + segundo + '\n' + lines
    return string


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(['3801 - 2', '123 + 49']))
print(arithmetic_arranger(['1 + 2', '1 - 9380']))
print(arithmetic_arranger(['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['11 + 4', '3801 - 2999', '1 + 2', '123 + 49', '1 - 9380']))
print(arithmetic_arranger(['44 + 815', '909 - 2', '45 + 43', '123 + 49', '888 + 40', '653 + 87']))
print(arithmetic_arranger(['3 / 855', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
print(arithmetic_arranger(['3 + 855', '988 + 40'], True))
print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))
