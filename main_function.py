"""main_function - a beginner-friendly decorator alternative to
if __name__ == '__main__': main() idiom.

This PyPi is meant to demonstrate a decorator-based alternative to the old-school idiom,
if __name__ == '__main__': main(). Traditionally, this idiom indicates that a script
is meant to both be run directly and be imported as a module, but its (possibly unjustified)
prevalence in educational materials nudges beginners to wrap their head around magic methods
and how Python works under the hood before it might be appropriate.  Purely from cursory
overview of beginner-to-intermediate educational content available for free, the idea of
using magic methods for this specific purpose does seem to be the biggest source of confusion
for people new to Python - as of the moment of writing this, YouTube video explaining
what this bit of code does by Corey Schafer is sitting on 1,7 million views
(one of his best), and video explaining the same concept by mCoding is at 865 thousand
views (his most viewed video ever). Question asking what this idiom does on StackOverflow
has more than 7600 upvotes, and more than 3200 bookmarks (second most upvoted Python
question). Furthermore, this improvement  fits in line with introduction of
dataclasses, which is basically a way of declaring classes without writing boilerplate
magic methods.

This very telling, self-explanatory decorator provides an alternative for people who don’t
want to remove the if __name__ == "__main__": main() idiom altogether, be it for lack of
understanding, concerns about future extensibility or any other reason.


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

import atexit
import inspect
import sys
from collections.abc import Callable
from functools import partial
from typing import Any, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def main_function(func: Callable[P, R]) -> Callable[P, R]:
    """A beginner-friendly alternative to if __name__ == '__main__': main() idiom."""

    def _atexit_clean_excepthook(etype: Any, value: Any, tb: Any) -> None:
        """Defers the execution of the main function until clean, no-error termination
        of the program."""
        atexit.unregister(func)
        sys.__excepthook__(etype, value, tb)

    if func.__module__ == "__main__":
        # If main() was not defined to take in sys.argv - run it as is.
        argspec: inspect.FullArgSpec = inspect.getfullargspec(func)
        if argspec.args or argspec.varargs:
            func = partial(func, sys.argv)
        sys.excepthook = _atexit_clean_excepthook
        atexit.register(func)
    return func
