#arithmetic formater 


def arithmetic_arranger(problems, show_answers=False):
    top_line = []
    bottom_line = []
    dash_line = []
    answer_line = []
    
    if len(problems) > 5: 
        return "Error: Too many problems."
    for problem in problems:
        parts = problem.split()
        operand1,operator, operand2 = parts[0], parts[1],parts[2]
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(operand1)>4 or len(operand2)>4:
            return "Error: Numbers cannot be more than four digits." 
        width = max(len(operand1), len(operand2)) + 2
        top = ' ' * (width - len(operand1)) + operand1
        bottom = operator + ' ' * (width - 1 - len(operand2)) + operand2
        dash = '-' * width

        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:  
                result = str(int(operand1) - int(operand2))
        
            answer_piece = ' ' * (width - len(result)) + result
            answer_line.append(answer_piece)
        
        top_line.append(top)
        bottom_line.append(bottom)
        dash_line.append(dash)
    
    arranged_problems = '    '.join(top_line) + '\n' + \
                        '    '.join(bottom_line) + '\n' + \
                        '    '.join(dash_line)
    if show_answers:
        arranged_problems += '\n' + '    '.join(answer_line)

    return arranged_problems

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')



