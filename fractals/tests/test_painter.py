from unittest import TestCase
from unittest.mock import patch, MagicMock

from painter import Painter
from picture import Picture


class TestPainter(TestCase):
    def setUp(self) -> None:
        self.mock_sleep = patch("time.sleep", return_value=None)
        self.mock_turtle = patch("turtle.Turtle", new=MagicMock())
        self.mock_screen = patch("turtle.Screen", new=MagicMock())

        self.mock_sleep.start()
        self.mock_turtle.start()
        self.mock_screen.start()
        self.painter = Painter()

    def tearDown(self) -> None:
        self.mock_sleep.stop()
        self.mock_turtle.stop()
        self.mock_screen.stop()

    def test_run_forward(self):
        self.painter.t.forward = MagicMock()

        line = Picture("F", 10, 90)

        self.painter.draw(line)
        self.painter.t.forward.assert_called_once_with(10)

    def test_left(self):
        self.painter.t.left = MagicMock()

        line = Picture("-", 10, 90)

        self.painter.draw(line)
        self.painter.t.left.assert_called_once_with(90)

    def test_right(self):
        self.painter.t.right = MagicMock()

        line = Picture("+", 10, 90)

        self.painter.draw(line)
        self.painter.t.right.assert_called_once_with(90)
