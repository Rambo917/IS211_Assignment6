
def convertCelsiusToKelvin(celsius):
    return celsius + 273.15


def convertCelsiusToFahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32.0


def convertFahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0


def convertFahrenheitToKelvin(fahrenheit):
    return (fahrenheit - 32.0) * 5.0 / 9.0 + 273.15


def convertKelvinToCelsius(kelvin):
    return kelvin - 273.15


def convertKelvinToFahrenheit(kelvin):
    return (kelvin - 273.15) * 9.0 / 5.0 + 32.0
