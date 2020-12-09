class Pop :

    _lives = 0
    _speed = 30.0

    def Test(self):
        print("Hoi")
        print("speed is: ",self._speed)


Pop1 = Pop()
NogeenPop = Pop()

Pop1.Test()

Pop1._speed = 23.32


print("Pop1 Speed:",Pop1._speed)
print("Pop2 Speed:",NogeenPop._speed)

PopLeef = Pop(3)