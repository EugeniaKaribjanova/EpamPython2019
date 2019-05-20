# -*- coding: utf-8 -*-

"""
Реализуйте метод, определяющий, является ли одна строка 
перестановкой другой. Под перестановкой понимаем любое 
изменение порядка символов. Регистр учитывается, пробелы 
являются существенными.
"""

def is_permutation(a: str, b: str) -> bool:
    list1 = list(a)
    list2 = list(b)

    if (len(list1) != len(list2)):
        return False
    try:
     for i in list1:
        list2.remove(i)
    except: return False
    return True


assert is_permutation('baba', 'abab')
assert not is_permutation('abbba', 'abab')
