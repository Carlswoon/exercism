"""Functions used in preparing Guido's gorgeous lasagna."""

EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the remaining baking time.

    Args:
        elapsed_bake_time (int): Minutes already spent baking.

    Returns:
        int: Minutes remaining.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    """Calculate the time needed to prepare the lasagna.

    Args:
        number_of_layers (int): Number of lasagna layers.

    Returns:
        int: Total preparation time in minutes.
    """
    return number_of_layers * PREPARATION_TIME


def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the total time spent preparing and baking.

    Args:
        number_of_layers (int): Number of lasagna layers.
        elapsed_bake_time (int): Minutes already spent baking.

    Returns:
        int: Total elapsed time in minutes.
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time