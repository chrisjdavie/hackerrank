
class Brackets:

    def __init__(self, brackets_str):
        self.brackets_str = brackets_str


    def balanced(self):

        bracket_pairs = { '[' : ']', '{' : '}', '(' : ')' }
        opening_brackets = set()

        for opening in bracket_pairs.keys():
            opening_brackets.add(opening)

        stack = []

        is_balanced = False

        for bracket in self.brackets_str:
            if bracket in opening_brackets:
                stack.append(bracket)
            else:
                if stack and bracket == bracket_pairs[stack[-1]]:
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                is_balanced = True

        return is_balanced

