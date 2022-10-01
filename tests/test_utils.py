from dash_local_react_components._utils import change_function_name


def test_name():
    def my_function():
        pass

    assert my_function.__name__ == "my_function"


def test_has_different_name():
    def my_function():
        pass

    my_function = change_function_name(my_function)

    assert my_function.__name__ != "my_function"


def test_starts_with_old_name():
    def my_function():
        pass

    my_function = change_function_name(my_function)

    assert my_function.__name__.startswith("my_function")


def test_creates_unique_names_each_time():
    def my_function():
        pass

    my_function_a = change_function_name(my_function)
    my_function_b = change_function_name(my_function)

    assert my_function_a.__name__ != my_function_b.__name__


def test_wraps_original_function():
    invoked = False

    def my_function():
        nonlocal invoked
        invoked = True

    my_function = change_function_name(my_function)
    my_function()

    assert invoked


def test_passes_positional_arguments():
    sum = 0

    def my_function(a, b):
        nonlocal sum
        sum = a+b

    my_function = change_function_name(my_function)
    my_function(2, 5)

    assert sum == 7


def test_passes_named_arguments():
    sum = 0

    def my_function(a, b):
        nonlocal sum
        sum = a+b

    my_function = change_function_name(my_function)
    my_function(a=2, b=5)

    assert sum == 7


def test_returns_result():
    def my_function():
        return 9

    my_function = change_function_name(my_function)
    result = my_function()

    assert result == 9
