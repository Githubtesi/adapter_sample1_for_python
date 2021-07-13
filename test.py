from dataclasses import dataclass, field, fields


# 摂氏○○度というデータクラス
@dataclass
class CelsiusTemperature:
    temperature: float


# 仕様変更
# ・摂氏-華氏に変換できるようにしろ。
# ・華氏について temperatureで表示できるようにしろ
@dataclass
class FahrenheitTemperature:
    """
    >>> cel = CelsiusTemperature(100)
    >>> fah = FahrenheitTemperature(cel)
    >>> cel.temperature
    100
    >>> fah.temperature
    212.0
    >>> fah.temperature=32
    >>> cel.temperature
    0.0
    """

    celsiusTemperature: CelsiusTemperature

    # 華氏のデータをtemperatureで設定。
    @property
    def temperature(self) -> float:
        return self.convertCelsiusToFahrenheit(self.celsiusTemperature.temperature)

    # 華氏temperatureを設定したら(set)摂氏の設定も変更。
    @temperature.setter
    def temperature(self, fah_temperature: int):
        self.celsiusTemperature.temperature = self.convertFahrenheitToCelsius(fah_temperature)

    def convertFahrenheitToCelsius(self, f: int):
        return (f - 32) * 5 / 9

    def convertCelsiusToFahrenheit(self, c: int):
        return (c * 9 / 5) + 32


if __name__ == '__main__':
    import doctest

    doctest.testmod()
