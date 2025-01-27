from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:
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

    def speed(self) -> float:
        match self._type:
            case ParrotType.EUROPEAN:
                return self._base_speed()
            case ParrotType.AFRICAN:
                return max(
                    0,
                    self._base_speed() - self._load_factor() * self._number_of_coconuts,
                )
            case ParrotType.NORWEGIAN_BLUE:
                return 0 if self._nailed else self._compute_base_speed_for_voltage()

    def cry(self) -> str:
        match self._type:
            case ParrotType.EUROPEAN:
                return "Sqoork!"
            case ParrotType.AFRICAN:
                return "Sqaark!"
            case ParrotType.NORWEGIAN_BLUE:
                return "Bzzzzzz" if self._voltage > 0 else "..."

    def _compute_base_speed_for_voltage(self) -> float:
        return min([24.0, self._voltage * self._base_speed()])

    def _load_factor(self) -> float:
        return 9.0

    def _base_speed(self) -> float:
        return 12.0
