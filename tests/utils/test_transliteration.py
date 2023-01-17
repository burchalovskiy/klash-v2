from app.utils.transliteration import translate_string_to_cyrillic, translate_string_to_latin

from tests.utils.fixtures import *


def test_translate_to_cyrillic():
    assert test_cyrillic == translate_string_to_cyrillic(test_latin)


def test_translate_ti_latin():
    assert test_latin == translate_string_to_latin(test_cyrillic)
