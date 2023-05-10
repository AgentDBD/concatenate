firstNum = "2"
secondNum = "2"
# firstNum = "15"
# secondNum = "
if len(firstNum) < len(secondNum):
    numZeros = len(secondNum) - len(firstNum)
    for x in range(numZeros):
        firstNum = "0" + firstNum

if len(secondNum) < len(firstNum):
    numZeros = len(firstNum) - len(secondNum)
    for x in range(numZeros):
        secondNum = "0" + secondNum

def add(a,b):
    carry = 0
    answer = ""
    for x in reversed(range(len(a))):
        temp = int(a[x]) + int(b[x]) + carry
        answer = str(temp % 10) + answer 
        carry = 0
        if temp > 9:
            carry = 1
    return answer


print(add(firstNum,secondNum))
print("Ayaan Nobody like u ")