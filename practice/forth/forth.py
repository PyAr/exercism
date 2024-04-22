import operator

class StackUnderflowError(Exception):
    """Exception raised when attempting to pop from an empty stack."""
    def __init__(self, message):
        self.message = message

def evaluate(input_data):
    """
    Evaluate Forth-like expressions.

    Args:
        input_data (list): List of Forth-like expressions.

    Returns:
        list: Resulting stack after evaluating the input data.
    """
    data = [i.lower() for i in input_data]
    stack = []
    operators = {"+": operator.add, "-": operator.sub,
                 "*": operator.mul, "/": operator.floordiv}
    manipulations = {"dup": operator.getitem, "drop": operator.delitem,
                     "over": operator.getitem}
    index = {"dup": -1, "drop": -1, "over": -2}
    user_defined = {}

    # Define user-defined operations
    for i in data:
        if i[0] == ":" and i[-1] == ";":
            definition = i[1:-1].split()
            if definition[0].isnumeric() or (definition[0][0] == "-" and definition[0][1:].isnumeric()):
                raise ValueError("illegal operation")
            else:
                instructions = []
                for op in definition[1:]:
                    if op in user_defined:
                        instructions += user_defined[op]
                    else:
                        instructions.append(op)
                user_defined[definition[0]] = instructions

    # Evaluate input expressions
    for i in data[-1].split():
        try:
            stack.append(int(i))
        except ValueError:
            if i in operators and i not in user_defined:
                try:
                    second, first = stack.pop(), stack.pop()
                    stack.append(operators[i](first, second))
                except IndexError:
                    raise StackUnderflowError("Insufficient number of items in stack")
                except ZeroDivisionError:
                    raise ZeroDivisionError("divide by zero")
            elif i == "swap" and "swap" not in user_defined:
                try:
                    first, second = stack.pop(), stack.pop()
                    stack += [first, second]
                except IndexError:
                    raise StackUnderflowError("Insufficient number of items in stack")
            elif i in manipulations:
                try:
                    new = manipulations[i](stack, index[i])
                    if new:
                        stack.append(new)
                except IndexError:
                    raise StackUnderflowError("Insufficient number of items in stack")
            elif i in user_defined:
                stack = evaluate([" ".join([str(i) for i in stack] + user_defined[i])])
            else:
                raise ValueError("undefined operation")

    return stack
