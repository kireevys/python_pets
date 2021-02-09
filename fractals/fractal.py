from picture import Picture


class Fractal:
    rules: dict
    angle: int
    axiom: str

    top: int

    def __init__(self, iterations: int):
        if iterations > self.top:
            raise AttributeError("Overhead iterations to this fractal")

        self.iterations = iterations

    def build_picture(self, distance) -> Picture:
        start_string = self.axiom

        for _ in range(self.iterations):
            s = []
            for i in start_string:
                if i in self.rules:
                    s.append(self.rules[i])
                else:
                    s.append(i)

            end_string = "".join(s)
            start_string = end_string

        return Picture(start_string, distance, self.angle, title=self.__class__.__name__)
