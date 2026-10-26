from binary_search import itog
from dual_binary import dual_binary
from exp_search import exp_search
from two_trackers import two_track


def run_tests():
    tests = [
        ("Пересечение в начале", [1, 2, 3], [1, 4, 5], True),
        ("Пересечение в конце", [1, 2, 4], [0, 3, 4], True),
        ("Пересечение в середине", [1, 5, 10], [2, 5, 8], True),
        ("Общих элементов нет", [1, 3, 5], [2, 4, 6], False),
        ("Один пустой массив", [], [1, 2, 3], False),
        ("Оба массива пустые", [], [], False),
        ("Массивы из одного одинакового элемента", [7], [7], True),
        ("Массивы из одного разного элемента", [3], [8], False),
        (
            "Короткий и длинный массив (есть совпадение)",
            [100, 200],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 200],
            True,
        ),
        (
            "Короткий и длинный массив (нет совпадений)",
            [100, 200],
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
            False,
        ),
        ("Массивы с дубликатами (есть)", [2, 2, 2], [1, 2, 3], True),
        ("Массивы с дубликатами (нет)", [2, 2, 2], [1, 3, 5], False),
        ("Худший случай: разная четность", [0, 2, 4, 6], [1, 3, 5, 7], False),
    ]

    algorithms = [
        (two_track, "Два указателя"),
        (itog, "Бинарный поиск"),
        (exp_search, "Экспоненциальный"),
        (dual_binary, "Двойной бинарный"),
    ]

    all_passed = True
    print("ЗАПУСК ТЕСТОВ РАБОТОСПОСОБНОСТИ АЛГОРИТМОВ\n")

    for func, name in algorithms:
        print(f"Тестирование алгоритма: {name}...")
        func_passed = True
        for test_name, a, b, expected in tests:
            result = func(a, b)
            if result != expected:
                print(f"  ОШИБКА {test_name}: ожидалось {expected}, получено {result}")
                func_passed = False
                all_passed = False
        if func_passed:
            print(f"...Все тесты для '{name}' успешно пройдены...\n")
    if all_passed:
        print("ВСЕ 4 АЛГОРИТМА УСПЕШНО ПРОШЛИ ВСЕ ТЕСТЫ")
    else:
        print("Есть упавшие тесты")
if __name__ == "__main__":
    run_tests()