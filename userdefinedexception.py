class TeaHotException(Exception):#userdefined exception for both conditions this for hot condition
    def __init__(self, arguu):
        self.msg = arguu


class TeaColdException(Exception):#this is for cold condition bro
    def __init__(self, arguu):
        self.msg = arguu


class Tea:
    def __init__(self, temparature):
        self.__temparature = temparature

    def drink_tea(self):
        if self.__temparature > 85:
            raise TeaHotException ("hott")
        elif self.__temparature < 65:
            raise TeaColdException ("Cold")
        else:
            print("Its Okey TO drink")


cup = Tea(50)
cup.drink_tea()
