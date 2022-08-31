"""main_function - a beginner-friendly decorator alternative to
if __name__ == '__main__': main() idiom.

This PyPi is meant to demonstrate a decorator-based alternative to the old-school idiom,
if __name__ == '__main__': main(), indicating that a script is meant to be run directly,
in a way that that does not force beginners to wrap their head around magic methods
and how Python works under the hood.  Purely from cursory overview of
beginner-to-intermediate educational content available for free, the idea of using
magic methods for this specific purpose does seem to be the biggest source of confusion
for people new to Python - as of the moment of writing this, YouTube video explaining
what this bit of code does by Corey Schafer is sitting on 1,7 million views
(one of his best), and video explaining the same concept by mCoding is at 865 thousand
views (his most viewed video ever). Question asking what this idiom does on StackOverflow
has more than 7600 upvotes, and more than 3200 bookmarks (second most upvoted Python
question). Furthermore, this fits in line with introduction of dataclasses, which
is basically a way of declaring classes without writing boilerplate magic methods.

This module demonstrates a way of attaining the same control flow while not forcing
newcomers to get acquainted with a traditional idiom, relyiong on a very telling
decorator instead.

Example:
    This:
        @main_function
        def main() -> None:
            print("Hello, world!")

    Is fully equivalent to this:
        def main() -> None:
            print("Hello, world!")

        if __name__ == "__main__":
            main()


For further discussion that has inspired this PyPi, please see this:
   https://discuss.python.org/t/built-in-is-main-function-as-a-more-beginner-
   friendly-alternative-to-if-name-main/18570

"""

import inspect
import sys
from collections.abc import Callable
from typing import Generic, ParamSpec, TypeVar

P: ParamSpec = ParamSpec("P")
R: Generic = TypeVar("R")


def main_function(func: Callable[P, R]) -> Callable[P, R]:
    """A beginner-friendly alternative to if __name__ == '__main__': main() idiom."""
    if func.__module__ == "__main__":
        # If main() was not defined to take in sys.argv - run it as is.
        argspec = inspect.getfullargspec(func)
        func() if not argspec.args and not argspec.varargs else func(sys.argv)
    return func
