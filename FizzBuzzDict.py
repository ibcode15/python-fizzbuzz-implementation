def FizzBuzz(range_: range = range(1,101), fizzdict: dict={3: "fizz",5:"buzz"}):
    for x in range_:
        if x == 0: continue
        result = ""
        for y in fizzdict.keys():
            if x%y == 0: result += fizzdict[y]
        if result == "": result = x
        print(result)
        
FizzBuzz()
