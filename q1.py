import sys

def priority(op): # Priority of Operator
    return 1 if op in "+-" else 2 if op in "*/%" else 0


def str_to_list(infix): # Infix String -> Infix List
    infix_list = []
    tmp_value = 0

    for c in range(len(infix)):
        if infix[c] in number:
            if c+1 < len(infix):
                if infix[c+1] in number:
                    tmp_value = (tmp_value + int(infix[c])) * 10
                else:
                    tmp_value += int(infix[c])
            else:
                tmp_value = tmp_value + int(infix[c])
            
            if infix[c] == '0' and tmp_value == 0: infix_list.append('0')
        else:
            if tmp_value > 0: 
                infix_list.append(str(tmp_value))
            infix_list.append(infix[c])
            tmp_value = 0
            
    if tmp_value > 0: infix_list.append(str(tmp_value))
    return infix_list
    


def toPostfix(infixlist): # Infix List -> Postfix List
    stack = []
    postlist = []

    for i in range(len(infixlist)):
        if infixlist[i] == '(': 
            stack.append(infixlist[i])

        elif infixlist[i] in '+-*/%':
            while(len(stack) > 0 and priority(stack[-1]) >= priority(infixlist[i])):
                postlist.append(stack[-1])
                stack.pop() 
            stack.append(infixlist[i])

        elif infixlist[i] == ')': 
            while (stack[-1] != '('):
                postlist.append(stack[-1])
                stack.pop()
            stack.pop() # remove '('

        else: # number
            postlist.append(infixlist[i])
            
    top = len(stack) - 1 
    while(top >= 0):
        postlist.append(stack[top])
        top -= 1

    return postlist



def cal_postfix (pfix):
    stack = []

    for i in range(len(pfix)):
        if pfix[i] in ['+', '-', '*', '/', '%']:
            op = pfix[i]
            b = int(stack[-1])
            stack.pop()
            a = int(stack[-1])
            stack.pop()

            if op == '+': c = a + b
            elif op == '-': c = a - b
            elif op == '*': c = a * b
            elif op == '%': c = a % b
            else:
                if b == 0: sys.exit('除數不可為零') # division by zero
                c = a / b

            stack.append(c)

        else:
            stack.append(int(pfix[i]))

    return stack[-1]



if __name__ == '__main__':
    global number
    number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    while True:
        infix_str = input("請輸入非負整數之數學運算式，結束請輸入0：")
        if infix_str == '0': break
        infix_str = infix_str.replace(' ', '').replace('=', '')
        print(f'= {cal_postfix(toPostfix(str_to_list(infix_str)))}')


    
