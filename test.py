class Vector:
    def __init__(self, x, y):
            self.__x = x
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self , value):
        if isinstance(value, int) :
            self.__x = value
        else:
            print("invalid")    

    @property
    def y(self):
        return self.__y
    
    @x.setter
    def y(self , value):
        if isinstance(value, int) :
            self.__y = value
        else:
            print("invalid")    

    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Vector(new_x,new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Vector(new_x,new_y)

    def __str__(self):
        xstr = f"{self.x:+}"
        ystr = f"{self.y:+}"
        if self.x == 0 :
            xstr = ""
        if self.y == 0 :
            ystr = ""
        return f"{xstr}i {ystr}j"

class Zvector(Vector):
    def __init__(self, x, y ,z):
        super().__init__(x, y)
        self.z = z

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self , value):
        if isinstance(value, int) :
            self.__z = value
        else:
            print("invalid")

    def __str__(self):
        zstr = f"{self.z:+}"
        if self.z == 0 :
            ystr = ""
        return super().__str__() + f" {zstr}k"


