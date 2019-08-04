result = None
A = int(input("ENter AnyThing Bro :"))
B = str(input("ENter Anythng Bro :"))

try:
  result = A + B
except Exception as e:
    print(e)
else:
    print("inside else")
finally:
    print("inside finally")        
print("----new line---")

print("Your result :", result)
