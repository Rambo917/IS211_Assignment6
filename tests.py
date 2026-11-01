
import unittest

from conversions import (
    convertCelsiusToKelvin,
    convertCelsiusToFahrenheit,
    convertFahrenheitToCelsius,
    convertFahrenheitToKelvin,
    convertKelvinToCelsius,
    convertKelvinToFahrenheit
)

from conversions_refactored import convert, ConversionNotPossible


class TestConversions(unittest.TestCase):

    def check_cases(self, function, cases):
        for value, expected in cases:
            with self.subTest(value=value):
                print("Testing {} with {}".format(
                    function.__name__, value
                ))
                self.assertAlmostEqual(function(value), expected, places=5)

    def testCelsiusToKelvin(self):
        self.check_cases(convertCelsiusToKelvin, [
            (0, 273.15),
            (100, 373.15),
            (-40, 233.15),
            (300, 573.15),
            (25, 298.15)
        ])

    def testCelsiusToFahrenheit(self):
        self.check_cases(convertCelsiusToFahrenheit, [
            (0, 32),
            (100, 212),
            (-40, -40),
            (300, 572),
            (25, 77)
        ])

    def testFahrenheitToCelsius(self):
        self.check_cases(convertFahrenheitToCelsius, [
            (32, 0),
            (212, 100),
            (-40, -40),
            (572, 300),
            (77, 25)
        ])

    def testFahrenheitToKelvin(self):
        self.check_cases(convertFahrenheitToKelvin, [
            (32, 273.15),
            (212, 373.15),
            (-40, 233.15),
            (572, 573.15),
            (77, 298.15)
        ])

    def testKelvinToCelsius(self):
        self.check_cases(convertKelvinToCelsius, [
            (273.15, 0),
            (373.15, 100),
            (233.15, -40),
            (573.15, 300),
            (298.15, 25)
        ])

    def testKelvinToFahrenheit(self):
        self.check_cases(convertKelvinToFahrenheit, [
            (273.15, 32),
            (373.15, 212),
            (233.15, -40),
            (573.15, 572),
            (298.15, 77)
        ])


class TestRefactoredConversions(unittest.TestCase):

    def testTemperatureConversions(self):
        cases = [
            ("celsius", "kelvin", 0, 273.15),
            ("celsius", "fahrenheit", 100, 212),
            ("fahrenheit", "celsius", 32, 0),
            ("fahrenheit", "kelvin", 212, 373.15),
            ("kelvin", "celsius", 273.15, 0),
            ("kelvin", "fahrenheit", 373.15, 212)
        ]

        for fromUnit, toUnit, value, expected in cases:
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                print("Testing {} to {}".format(fromUnit, toUnit))
                self.assertAlmostEqual(
                    convert(fromUnit, toUnit, value),
                    expected,
                    places=5
                )

    def testDistanceConversions(self):
        cases = [
            ("miles", "yards", 1, 1760),
            ("miles", "meters", 1, 1609.344),
            ("yards", "miles", 1760, 1),
            ("yards", "meters", 1, 0.9144),
            ("meters", "miles", 1609.344, 1),
            ("meters", "yards", 0.9144, 1)
        ]

        for fromUnit, toUnit, value, expected in cases:
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                print("Testing {} to {}".format(fromUnit, toUnit))
                self.assertAlmostEqual(
                    convert(fromUnit, toUnit, value),
                    expected,
                    places=5
                )

    def testSameUnit(self):
        units = [
            "celsius", "fahrenheit", "kelvin",
            "miles", "yards", "meters"
        ]

        for unit in units:
            with self.subTest(unit=unit):
                print("Testing same unit:", unit)
                self.assertEqual(convert(unit, unit, 100), 100.0)

    def testInvalidConversions(self):
        cases = [
            ("celsius", "meters"),
            ("miles", "fahrenheit"),
            ("kelvin", "yards"),
            ("meters", "celsius"),
            ("invalid", "invalid")
        ]

        for fromUnit, toUnit in cases:
            with self.subTest(fromUnit=fromUnit, toUnit=toUnit):
                print("Testing invalid conversion:",
                      fromUnit, "to", toUnit)
                with self.assertRaises(ConversionNotPossible):
                    convert(fromUnit, toUnit, 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)
