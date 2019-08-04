class Tea:
    def __init__(self,temparature):
        self.__temparature = temparature

    def drink_tea(self):
        if self.__temparature > 85:
           raise ValueError("Too Hot")#exception raised here we can also defined our own exception like if low balance in wallet it will show insufficient balacne that is an exception bro
        elif self.__temparature < 65:
            print("TOo COld")
        else:
            print("Okey to drink")

cup = Tea(100)
cup.drink_tea()            
