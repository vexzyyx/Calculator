from builtins import int


print("--Calculator--\nEnter a mathematical expression. (Examples: 50 * 37.578 | 3.67 ^ 5.9 | 60.59 / 57.685)")

def user_input():
    return input("\n\033[34mExercise: \033[0m").lower()


def algorithm(string):
    answer = None
    if not string == "":
        try:
            if "+" in string:
                 operator = "+"
                 exercise = string.split("+")
            elif "-" in string:
                operator = "-"
                exercise = string.split("-")
            elif "*" in string and not "**" in string:
                operator = "*"
                exercise = string.split("*")
            elif "/" in string:
                operator = "/"
                exercise = string.split("/")
            elif "**" in string:
                operator = "**"
                exercise = string.split("**")
            elif "^" in string:
                operator = "**"
                exercise = string.split("^")
            if operator == "+":
                answer = float(exercise[0]) + float(exercise[1])
            elif operator == "-":
                answer = float(exercise[0]) - float(exercise[1])
            elif operator == "*":
                answer = float(exercise[0]) * float(exercise[1])
            elif operator == "/":
                answer = float(exercise[0]) / float(exercise[1])
                print("\033[31mError 02: Dividing by 0 equals infinity\033[0m\n")
                answer = None
            elif operator == "**":
                answer = float(exercise[0]) ** float(exercise[1])
                   
            if isinstance(answer, float) and answer.is_integer():
                answer = int(answer)

        except ValueError:
            print("\033[31mError 03: Invalid Input\033[0m")
            answer = None

        except UnboundLocalError:
            print("\033[31mError 03: Invalid Input\033[0m")
            answer = None
        
        except ZeroDivisionError:
            print("\033[31mError 02: Dividing by 0 equals infinity\033[0m")
        
        except OverflowError:
            print("\033[31mError 01: Result too large\033[0m")

    else:
        print("\033[31mError 04: No Input\033[0m")

    return answer
    

while True:
    answer = algorithm(user_input())
    if not answer == None:
        print(f"\033[32mSolution:\033[0m {answer}")
