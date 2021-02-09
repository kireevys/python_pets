class Picture:
    def __init__(self, algorithm: str, distance: int, angle: int, title: str):
        self.algorithm = algorithm
        self.distance = distance
        self.angle = angle
        self.title = title

    def __eq__(self, other: "Picture"):
        return all(
            (
                self.algorithm == other.algorithm,
                self.distance == other.distance,
                self.angle == other.angle,
            )
        )

    def __repr__(self):  # pragma: no cover
        return f"{self.algorithm},{self.distance},{self.angle}"
