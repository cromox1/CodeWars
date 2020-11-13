decode1 = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL",
                           10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}

print('decode1 = ', decode1)

decode2 = {v:k for k,v in decode1.items()}
print('decode2 = ',decode2)

decode2a = {v:k for k,v in decode1.items() if len(v) == 1}
print('decode2a = ',decode2a)

decode2b = {v:k for k,v in decode1.items() if len(v) > 1}
print('decode2b = ',decode2b)

decode3 = {v:k for k,v in decode1.items() if len(v) == 2}
print('decode3 = ',decode3)

obj1 = ["Even" if i%2==0 else "Odd" for i in range(10)]
print(obj1)

obj2 = [str(i)+":Even" if i%2==0 else str(i)+":Odd" for i in range(30) if i%3 != 0 and i%5 != 0]
print(obj2)

obj3 = tuple(str(i) if i%2==0 else i for i in range(30) if i%3 != 0 and i%5 != 0)
print(obj3)


