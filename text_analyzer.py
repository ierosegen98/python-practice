"""Модуль для анализа текстовых данных."""

from collections import Counter
from typing import TypedDict


class TextAnalysis(TypedDict):
    """Описывает структуру результата анализа текста."""

    unique_words: set[str]
    word_counts: Counter[str]
    lines: int
    longest_word: str | None


def analyze_text(text: str) -> TextAnalysis:
    """Анализирует текст и возвращает статистику по словам и строкам."""
    translator = str.maketrans("", "", '.,!?:;-()[]{}"""\'…')
    words = text.translate(translator).lower().split()

    return {
        "unique_words": set(words),
        "word_counts": Counter(words),
        "lines": len(text.splitlines()),
        "longest_word": max(words, key=len, default=None),
    }


if __name__ == "__main__":
    test_text = "Hello, world! Python is great!"
    print("Тест:", analyze_text(test_text))
