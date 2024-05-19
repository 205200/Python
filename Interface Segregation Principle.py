# Interface Segregation Principle (ISP)
# Clients should not be forced to depend on methods they do not use.

# Violating ISP: IShape interface forces all shapes to implement unnecessary methods.
class IShape:
    def draw_square(self):
        raise NotImplementedError

    def draw_rectangle(self):
        raise NotImplementedError

    def draw_circle(self):
        raise NotImplementedError


class Circle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Square(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


class Rectangle(IShape):
    def draw_square(self):
        pass

    def draw_rectangle(self):
        pass

    def draw_circle(self):
        pass


# Conforming to ISP: Separate interfaces for different shapes.
class IDrawSquare:
    def draw_square(self):
        raise NotImplementedError


class IDrawRectangle:
    def draw_rectangle(self):
        raise NotImplementedError


class IDrawCircle:
    def draw_circle(self):
        raise NotImplementedError


class Square(IDrawSquare):
    def draw_square(self):
        pass


class Rectangle(IDrawRectangle):
    def draw_rectangle(self):
        pass


class Circle(IDrawCircle):
    def draw_circle(self):
        pass

# Each shape class now implements only the methods it needs, conforming to ISP.
