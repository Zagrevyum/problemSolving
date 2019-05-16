class Factorial:
    def Factorial(self, number):
        if number == 0:
            return 1
        else:
            return number * self.Factorial(number-1)

    def Factorialloop(self, number):
        result = 1
        for i in range(number, 1, -1):
            result *= i
        return result

    def fibonacci(self, limit):
        result = [0, 1]
        for i in range(2, limit):
            result.append(result[i-2]+result[i-1])
        return result

    def fibonacciRec(self, n=-1):
        if 0 == n:
            return 0
        elif 1 == n:
            return 1
        else:
            return self.fibonacciRec(n-1) + self.fibonacciRec(n-2)




solved = Factorial()

print(solved.Factorial(5))
print(solved.Factorialloop(5))
print(solved.fibonacci(5))
print(solved.fibonacciRec(6))


