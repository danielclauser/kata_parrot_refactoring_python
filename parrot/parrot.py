from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:
    _BASE_SPEED: float = 12.0
    _LOAD_FACTOR: float = 9.0

    def __init__(
        self,
        type_of_parrot: int | ParrotType,
        number_of_coconuts: int,
        voltage: float,
        nailed: bool,
    ) -> None:
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def speed(self) -> float | ValueError:
        match self._type:
            case ParrotType.EUROPEAN:
                return self._BASE_SPEED
            case ParrotType.AFRICAN:
                return max(
                    0,
                    self._BASE_SPEED - self._LOAD_FACTOR * self._number_of_coconuts,
                )
            case ParrotType.NORWEGIAN_BLUE:
                return 0 if self._nailed else self._compute_base_speed_for_voltage()
            case _:
                raise ValueError(f"Parrot not found {self._type}")

    def cry(self) -> str | ValueError:
        match self._type:
            case ParrotType.EUROPEAN:
                return "Sqoork!"
            case ParrotType.AFRICAN:
                return "Sqaark!"
            case ParrotType.NORWEGIAN_BLUE:
                return "Bzzzzzz" if self._voltage > 0 else "..."
            case _:
                raise ValueError(f"Parrot not found {self._type}")

    def _compute_base_speed_for_voltage(self) -> float:
        return min([24.0, self._voltage * self._BASE_SPEED])


def create_parrot(
    type_of_parrot: int | ParrotType,
    number_of_coconuts: int,
    voltage: float,
    nailed: bool,
):
    return Parrot(type_of_parrot, number_of_coconuts, voltage, nailed)
