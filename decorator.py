from datetime import datetime


def decor(func):
    def new_func(*args, **kwargs):
        with open("log/some.log", 'a', encoding='UTF-8') as log:
            start = datetime.now()
            args_foo = [repr(i) for i in args]
            kwargs_foo = [f'{k}={v}' for k, v in kwargs.items()]
            result = func(*args, **kwargs)
            log.write(
                f'Время вызова функции {start}\n Имя вызванной функции {func.__name__}\n Аргументы вызванной функции {args_foo, kwargs_foo}\n Функция {func.__name__!r} возвращает {result!r}\n')
            return result

    return new_func
