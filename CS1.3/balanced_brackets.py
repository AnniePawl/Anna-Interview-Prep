# Return True is string expression contains correctly balanced parenthesis/ brackets


def balanced_brackets(expression):
   # if we see opening bracket, put it in the stack (.append)
    open_brackets = "{[("
    closed_brackets = "}])"
    bracket_stack = []

    for character in expression:
        if character in open_brackets:
            bracket_stack.append(character)
        # check if open bracket at top matches the closed bracket
        if character in closed_brackets:
            open_bracket_at_top = bracket_stack.pop(len(bracket_stack-1))

            # if nothing left in parentheses stack, we have matches, return TRUE
            # if there a parenthesis left in stack, have are unbalanced, return FALSE


print(balanced_brackets("[(Anna)"))
print(balanced_brackets("[(Anna)]"))
