# Напишите функцию modified_func, которая принимает функцию (обозначим ее func),
# а также произвольный набор позиционных (назовем их fixated_args) и именованных
# (назовем их fixated_kwargs) аргументов и возвращает новую функцию,
# которая обладает следующими свойствами:
#
# 1.При вызове без аргументов повторяет поведение функции func, вызванной
# с fixated_args и fixated_kwargs.
# 2.При вызове с позиционными и именованными аргументами дополняет ими
# fixed_args (приписывает в конец списка fixated_args), и fixated_kwargs
# (приписывает новые именованные аргументы и переопределяет значения старых)
# и далее повторяет поведение func с этим новым набором аргументов.
# 3.Имеет __name__ вида func_<имя функции func>
# 4.Имеет docstring вида:
#
# """
# A func implementation of <имя функции func>
# with pre-applied arguments being:
# <перечисление имен и значений fixated_args и fixated_kwargs>
# source_code:
#    ...
# """

import inspect


def sample_func(*targs, **tkwargs):
    print(targs, tkwargs)


def modified_func(func, *fixated_args, **fixated_kwargs):

    def new_func(*fixed_args, **fixed_kwargs):
        new_args = list(fixated_args+fixed_args)
        for key in fixed_kwargs:
            fixated_kwargs[key] = fixed_kwargs[key]
        fixated_kwargs.update(fixed_kwargs)
        sample_func(new_args, fixated_kwargs)

    new_func.__name__ = 'func_' + func.__name__
    source_code = inspect.getsource(new_func)

    new_func.__doc__ = f'A func implementation of {func.__name__}\n' \
        f'with pre-applied arguments being:\n' \
        f'{str(fixated_args), str(fixated_kwargs)}\n' \
        f'source_code:\n' \
        f'{source_code}'
    print(new_func.__doc__)
    return new_func


result = modified_func(sample_func, 1, 2, warg1='p', warg2='h', warg3='=', warg4='7')
result(3, 4, 5, warg4='10', warg5='acid')



