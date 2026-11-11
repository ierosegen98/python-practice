"""Модуль для фильтрации разности множеств."""


def filtered_set_diff(set1: set, set2: set, filter_func: callable) -> frozenset[int]:
    """Возвращает неизменяемое множество элементов разности двух множеств, удовлетворяющих заданному условию фильтрации."""
    return frozenset(filter(filter_func, set1 - set2))


if __name__ == "__main__":
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6}
    is_even = lambda value: value % 2 == 0

    print("Тест:", filtered_set_diff(set_a, set_b, is_even))
