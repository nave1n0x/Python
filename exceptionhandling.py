result = None
A = str(input("ENter AnyThing Bro :"))
B = int(input("ENter Anythng Bro :"))

try:
  result = A + B
except Exception as e:
    print(e)  
print("----new line---")

print("Your result :", result)
