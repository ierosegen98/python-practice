"""Модуль для анализа текстовых данных."""

from collections import Counter


def analyze_text(text: str) -> dict:
    """Анализирует текст и возвращает статистику по словам и строкам."""
    translator = str.maketrans("", "", '.,!?:;-()[]{}"""\'…')
    words = text.translate(translator).lower().split()
    return {
        "unique_words": set(words),
        "word_counts": Counter(words),
        "lines": text.count("\n") + 1,
        "longest_word": max(words, key=len),
    }


if __name__ == "__main__":
    test_text = "Hello, world! Python is great!"
    print("Тест:", analyze_text(test_text))
