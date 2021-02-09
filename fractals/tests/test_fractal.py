from unittest import TestCase

from koch_snowflake import Snowflake
from picture import Picture


class TestFractal(TestCase):
    def test_build_picture(self):
        fractal = Snowflake(1)

        self.assertEqual(
            fractal.build_picture(10), Picture("F+F--F+F--F+F--F+F--F+F--F+F", 10, 60)
        )

    def test_overhead_iteration(self):
        with self.assertRaises(AttributeError):
            Snowflake(Snowflake.top + 1)
