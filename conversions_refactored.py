
class ConversionNotPossible(Exception):
    pass


def convert(fromUnit, toUnit, value):
    temperature_units = ["celsius", "fahrenheit", "kelvin"]
    distance_units = ["miles", "yards", "meters"]

    fromUnit = fromUnit.lower()
    toUnit = toUnit.lower()
    value = float(value)

    if fromUnit == toUnit:
        if fromUnit in temperature_units + distance_units:
            return value
        raise ConversionNotPossible("Unknown unit")

    if fromUnit in temperature_units and toUnit in temperature_units:
        if fromUnit == "celsius":
            celsius = value
        elif fromUnit == "fahrenheit":
            celsius = (value - 32.0) * 5.0 / 9.0
        else:
            celsius = value - 273.15

        if toUnit == "celsius":
            return float(celsius)
        elif toUnit == "fahrenheit":
            return float(celsius * 9.0 / 5.0 + 32.0)
        else:
            return float(celsius + 273.15)

    if fromUnit in distance_units and toUnit in distance_units:
        factors = {
            "miles": 1609.344,
            "yards": 0.9144,
            "meters": 1.0
        }

        meters = value * factors[fromUnit]
        return float(meters / factors[toUnit])

    raise ConversionNotPossible(
        "Cannot convert from {} to {}".format(fromUnit, toUnit)
    )
