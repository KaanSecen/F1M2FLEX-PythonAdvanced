class character :

    speed = 15
    points = 0
    jumpheight = 23
    items = []

    def __init__(self) :
        print("Constructor van de Character")

    def BasicItem(self) :
        self.items.append("Coin")
        print(self.items)

    def SlotCounter(self) :
        self.items.append("3")
        print(self.items)

class Mario (character) :

    lives = 3
    time = 300

    def __init__(self) :
        self.speed = 30
        self.items.append("Mushroom")
        print(self.items)

    def BasicItem(self) : 
        print("Changed")

    def SlotCounter(self) :
        super().__init__()
        self.items.append("Green Mushroom")
        print(self.items)

    
ClassA = character()
ClassB = Mario()

ClassA.BasicItem()
ClassB.BasicItem()
ClassB.SlotCounter()