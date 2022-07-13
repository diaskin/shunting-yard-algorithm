# Dictonary to store variables
varMem = {}

# Checking if the input is first_one number
def isDigit(numToCheck):
    try:
        isFloat = float(numToCheck)   
    except ValueError:
        return False
    return True

# Setting priority of operators
def priorityCheck(charToCheck):
    priorityDict = {'^' : 4, '*' : 3, '/' : 2, '+' : 1, '-' : 0}
    return priorityDict[charToCheck]

# Postfix to infix conversion
def PostfixForm(exp):
    Stack = ['!']
    postfixForm = []
    
    for exp in exp:
        if isDigit(exp) or exp.isalpha():
            postfixForm.append(exp)
        elif exp =='(' or exp == ')':
            if exp == '(':
                Stack.append(exp)
            else:
                 while Stack[-1] != '!' and Stack[-1] != '(':
                     postfixForm+=Stack.pop()
                 if Stack[-1] == '(':
                    Stack.pop()
        else:
            # Checking if the operator is higher priority than the top of the stack
            while Stack[-1] != '!' and Stack[-1] != '(':
                    if priorityCheck(Stack[-1]) > priorityCheck(exp):
                        postfixForm.append(Stack.pop())
                    else:
                        break
            Stack.append(exp)
    while Stack[-1] != '!':
        Stack.pop() if Stack[-1] == '(' else postfixForm.append(Stack.pop())
    return postfixForm

# Postfix evaluation
def evaluation(postfixForm):
    op = []
    for expr in postfixForm:
        if isDigit(expr):
            op.append(float(expr)) if "." in expr else op.append(int(expr))
        elif expr.isalpha():
            op.append(varMem[expr]) if expr in varMem else op.append(0)
        elif expr == '*':   
            second_one,first_one = op.pop(), op.pop()
            op.append(first_one*second_one)
        elif expr == '-':
            second_one,first_one = op.pop(), op.pop()
            op.append(first_one-second_one)
        elif expr == '+':
            second_one,first_one = op.pop(), op.pop()
            op.append(first_one+second_one)
        elif  expr == '/':
            second_one,first_one = op.pop(), op.pop()
            op.append(first_one/second_one)
        elif  expr == '^':
            second_one,first_one = op.pop(), op.pop()
            op.append(first_one**second_one)
    return op[0]

while 1:
    try:
        exp = input()

        if exp == "!":
            break
    
        ip = []
        var = newVariable = ""
        i = 0
        leftOperator = assign = False

        while i < len(exp):
            # Check if i is first_one number to check
            if isDigit(exp[i]) or (leftOperator and priorityCheck(exp[i])!=-1):
                while isDigit(exp[i]) or exp[i] == "." or leftOperator:
                    var+=exp[i]
                    i+=1
                    if leftOperator:
                        leftOperator = False
                    if i>=len(exp):
                        break
                ip.append(var)
                var = ""
            elif priorityCheck(exp[i])!=-1:
                if not leftOperator:
                    ip.append(exp[i])
                    i+=1
                    leftOperator = True
            elif exp[i] =='(' or exp[i] == ')':
                ip.append(exp[i])
                i += 1
            elif exp[i].isalpha():
                leftOperator = False
                while exp[i].isalpha() :
                    var+=exp[i]
                    i+=1
                    if i >= len(exp):
                        ip.append(var)
                        var = ""
                        break
                if i < len(exp):
                    if exp[i] == "=":
                        leftOperator = assign = True
                        newVariable = var
                        i+=1
                    else:
                        ip.append(var)
                var = ""
            elif exp[i] == "=":
                leftOperator = assign = True
                newVariable =  ip[-1]
                ip.pop()
                i+=1
            elif exp[i] == " ":
                i+=1
            else:
                i+=1
                raise Exception
        postfixForm = PostfixForm(ip)

        if assign:
            varMem[newVariable] = evaluation(postfixForm)
            newVariable = ""
            assign = False
        else:
            pass
            print(evaluation(postfixForm))
    except:
        print(0)
        continue