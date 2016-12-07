import math
import matplotlib.pyplot as plt


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
        self.angle_a = math.degrees(math.acos((math.pow(side_b, 2) + math.pow(side_c, 2) - math.pow(side_a, 2)) / (2 * side_b * side_c)))
        self.angle_b = math.degrees(math.acos((math.pow(side_c, 2) + math.pow(side_a, 2) - math.pow(side_b, 2)) / (2 * side_c * side_a)))
        self.angle_c = math.degrees(math.acos((math.pow(side_a, 2) + math.pow(side_b, 2) - math.pow(side_c, 2)) / (2 * side_a * side_b)))

    def display(self):
        plt.axes()

        circle = plt.Circle((0, 0), radius=0.75, fc='y')
        plt.gca().add_patch(circle)

        plt.axis('scaled')
        plt.show()



def main():
    t = Triangle(
        side_a=8,
        side_b=6,
        side_c=7
    )
    t.display()


if __name__ == "__main__":
    main()
