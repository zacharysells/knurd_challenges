import math
try:
   input = raw_input
except NameError:
   pass


class Triangle:


    def __init__(self, side_a, side_b, side_c):
        """
        We need 3 pieces of info to create the triangle. Either 2 sides and 1 angle,
        or 2 angles and 1 side. This init function takes 3 strings as input.
        """

        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        # law of cosines http://www.mathsisfun.com/algebra/trig-solving-sss-triangles.html
        try:
            self.angle_a = math.degrees(math.acos((math.pow(side_b, 2) + math.pow(side_c, 2) - math.pow(side_a, 2)) / (2 * side_b * side_c)))
            self.angle_b = math.degrees(math.acos((math.pow(side_c, 2) + math.pow(side_a, 2) - math.pow(side_b, 2)) / (2 * side_c * side_a)))
            self.angle_c = math.degrees(math.acos((math.pow(side_a, 2) + math.pow(side_b, 2) - math.pow(side_c, 2)) / (2 * side_a * side_b)))

            if self.angle_a + self.angle_b + self.angle_c != 180.0:
                raise ValueError("Invalid triangle: %f, %f, %f" % (self.side_a, self.side_b, self.side_c))
            if any([a == 0 for a in {self.angle_a, self.angle_b, self.angle_c}]):
                raise ValueError("Invalid triangle: %f, %f, %f" % (self.side_a, self.side_b, self.side_c))
        except ValueError:
            raise ValueError("Invalid triangle: %f, %f, %f" % (self.side_a, self.side_b, self.side_c))

    def is_congruent(self, t):
        return "%.5f" % self.angle_a == "%.5f" % t.angle_a and "%.5f" % self.angle_b ==  "%.5f" % t.angle_b and "%.5f" % self.angle_c == "%.5f" % t.angle_c and self.is_similar(t)
    def is_similar(self, t):
        return "%.5f" % self.angle_a == "%.5f" % t.angle_a and "%.5f" % self.angle_b ==  "%.5f" % t.angle_b and "%.5f" % self.angle_c == "%.5f" % t.angle_c

    def properties(self):
        properties = []
        if self.is_equilateral():
            properties.append("Equilateral")
        elif self.is_isosceles():
            properties.apend("Isosceles")
        elif self.is_scalene():
            properties.append("Scalene")

        if self.is_right():
            properties.append("Right")
        elif self.is_obtuese():
            properties.append("Obtuse")
        elif self.is_acute():
            properties.append("Acute")

        return properties

    def is_right(self):
        num_90 = 0
        for a in {self.angle_a, self.angle_b, self.angle_c}:
            if a == 90.0:
                num_90 +=1
        return num_90 == 1
    def is_equilateral(self):
        return self.side_a == self.side_b == self.side_c
    def is_isosceles(self):
        return self.side_a == self.side_b or self.side_a == self.side_c or self.side_b == self.side_c
    def is_scalene(self):
        return not self.is_equilateral() and not self.is_isosceles()
    def is_obtuese(self):
        return any([a > 90 for a in {self.angle_a, self.angle_b, self.angle_c}])
    def is_acute(self):
        return not self.is_obtuese()


def main():
    _menu = """
    1.) Add triangle
    2.) Describe triangles
    3.) Compare triangles
    4.) Exit
    """
    triangles = []
    while True:
        print(_menu)
        option = input("Selection: ")
        if option == "1":
            try:
                side_a, side_b, side_c = input("Dimensions(comma delimited): ").split(',')
                t = Triangle(float(side_a), float(side_b), float(side_c))
            except ValueError as e:
                print(e)
                continue
            triangles.append(t)
        elif option == "2":
            i = 1
            if len(triangles) == 0:
                print("No triangles have been input yet!")
            for t in triangles:
                print("%d.) (%.2f, %.2f), (%.2f, %.2f), (%.2f, %.2f): " % (i, t.side_a, t.angle_a, t.side_b, t.angle_b, t.side_c, t.angle_c), t.properties())
                i += 1
        elif option == "3":
            try:
                triangle_a, triangle_b = input("Triangles to compare(comma delimited): ").split(',')
                if triangles[int(triangle_a)-1].is_congruent(triangles[int(triangle_b)-1]):
                    print("The two triangles are congruent")
                if triangles[int(triangle_a)-1].is_similar(triangles[int(triangle_b)-1]):
                    print("The two triangles are similar")
                else:
                    print("The triangles are not similar nor congruent :(")

            except ValueError:
                print("Invalid input")
                continue
            except IndexError:
                print("Invalid triangle selection")
                continue

        elif option == "4":
            break
        else:
            print("Invalid input. Try again")
            continue



if __name__ == "__main__":
    main()
