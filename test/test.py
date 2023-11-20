import unittest
from area_calc import Shape

class TestAreaCalc(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        rect = Shape("rectangle")
        rect.set_dimensions(l=4, w=5)
        circ = Shape("circle")
        circ.set_dimensions(r=3)
        tri = Shape("triangle")
        tri.set_dimensions(b=2,h=3)
        self.shapes = [rect, circ, tri]

    def test_define_shapes(self):
        for shape in self.shapes:
            self.assertIsInstance(shape, Shape, f"Shape not parsing input")

    def test_area(self):
        self.assertEquals(self.shapes[0].get_area(), 20)
        self.assertEquals(self.shapes[1].get_area(), 28.2744)
        self.assertEquals(self.shapes[2].get_area(), 3)

    def test_perim(self):
        self.assertEquals(self.shapes[0].get_perim(), 18)
        self.assertEquals(self.shapes[1].get_perim(), 18.8495)
        self.assertEquals(self.shapes[2].get_perim(), 6)

if __name__ == "__main__":
    unittest.main()