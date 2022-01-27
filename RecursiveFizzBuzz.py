def FizzBuzz(Start: int = 1 , End: int = 100):
    result = ""
    if Start-1 == End: return None
    if Start%3 == 0:  result +="Fizz"
    if Start%5 == 0:  result +="Buzz"
    if result == "": result = Start
    print(result)
    return FizzBuzz(Start +1, End)

FizzBuzz()
