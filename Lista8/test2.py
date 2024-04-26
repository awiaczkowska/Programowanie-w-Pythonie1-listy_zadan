from z2l8 import guess_language


if __name__ == "__main__":
    languages = {'english': ('e', 't', 'a'),
                 'spanish': ('e', 'a', 'o'),
                 'polish': ('a', 'i', 'e')}

    # Wyjasnienie: `assert <warunek>` rzuca wyjatek AssertionError,
    # jesli warunek jest falszywy. Dla poprawnego rozwiazania,
    # ponizsze cztery testy nie powinny rzucac zadnego wyjatku.
    assert guess_language('english.txt', languages) == 'english'
    assert guess_language('spanish.txt', languages) == 'spanish'
    assert guess_language('polish.txt', languages) == 'polish'
    assert guess_language('german.txt', languages) == 'unknown'

    print("Wszystko ok!")
