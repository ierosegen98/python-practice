"""Модуль для фильтрации разности множеств."""

from collections.abc import Callable


def filtered_set_diff(
    source_set: set[int], excluded_set: set[int], filter_func: Callable[[int], bool]
) -> frozenset[int]:
    """Возвращает неизменяемое множество элементов разности двух множеств,
    удовлетворяющих заданному условию фильтрации.
    """
    return frozenset(filter(filter_func, source_set - excluded_set))


def is_even(value: int) -> bool:
    """Проверяет, является ли число чётным."""
    return value % 2 == 0


if __name__ == "__main__":
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6}

    print("Тест:", filtered_set_diff(set_a, set_b, is_even))
