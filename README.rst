=============
Main Function
=============


.. image:: https://img.shields.io/pypi/v/main_function.svg
        :target: https://pypi.python.org/pypi/main_function

.. image:: https://img.shields.io/travis/vovavili/main_function.svg
        :target: https://travis-ci.com/vovavili/main_function

.. image:: https://readthedocs.org/projects/main-function/badge/?version=latest
        :target: https://main-function.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/vovavili/main_function/shield.svg
     :target: https://pyup.io/repos/github/vovavili/main_function/
     :alt: Updates



A beginner-friendly decorator alternative to if __name__ == '__main__': main() idiom.


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




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


License
-------
MIT
