from ArithmeticLibrary import math_it

def math_it_wrap(type, x, y, ):
    if type(x)==list:
        if type=="ADD":
            total = 0
            for i in x:
                total += math_it(type, i, 0)
            return total
        else:
            raise NotImplementedError

    elif not y:
        y = x
        return math_it(type, x, y) 


class Shape:
    def __init__(self, type: str):
        shape_types = ["rectangle", "circle", "triangle"]
        self.dimensions = {}
        if type=="rectangle":
            self.dimensions["l"] = None
            self.dimensions["w"] = None
        elif type=="circle":
            self.dimensions["r"] = None
        elif type=="triangle":
            self.dimensions["b"] = None
            self.dimensions["h"] = None
        else:
            raise Exception(f"Must be of type {shape_types}")
    def set_dimensions(self, **kwargs):
        for key in kwargs:
            if key not in self.dimensions.keys():
                raise Exception(f"Must enter one or multiple of the following keys {self.dimensions.keys()} followed by a value")
        self.dimensions = kwargs
        return self.dimensions.__str__()
    def get_area(self):
        if not self.dimensions:
            raise Exception("Must enter dimensions first!")
        if type=="rectangle":
            self.area = math_it_wrap("MULT", self.dimensions["l"], self.dimensions["w"])
        elif type=="circle":
            import math
            self.area = math_it_wrap("MULT", math_it_wrap("MULT", math.pi, self.dimensions["r"]), self.dimensions["r"]) 
        elif type=="triangle":
            self.area = math_it_wrap("MULT", math_it_wrap("DIV", 1, 2), math_it_wrap("MULT", self.dimensions["b"], self.dimensions["h"]))
        return self.area
    def get_perim(self):
        if not self.dimensions:
            raise Exception("Must enter dimensions first!")
        if type=="rectangle":
            self.perim = math_it_wrap("ADD", [self.dimensions["l"], self.dimensions["w"]])
        elif type=="circle":
            import math
            self.perim = math_it_wrap("MULT", 2, math_it_wrap("MULT", math.pi, self.dimensions["r"]))
        elif type=="triangle":
            self.perim = math_it_wrap("ADD", [self.dimensions["b"], self.dimensions["h"], self.dimensions["h"]])
        return self.perim
        

