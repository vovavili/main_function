==============
@main_function
==============


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



A beginner-friendly decorator alternative to ``if __name__ == '__main__': main()`` idiom.


This PyPi is meant to demonstrate a decorator-based alternative to the old-school idiom,
``if __name__ == '__main__': main()``. Traditionally, this idiom indicates that a script
is meant to both be run directly and be imported as a module, but its (possibly unjustified)
prevalence in educational materials nudges beginners to wrap their head around magic methods
and how Python works under the hood before it might be appropriate.  Purely from cursory
overview of beginner-to-intermediate educational content available for free, the idea
of using magic methods for this specific purpose does seem to be the biggest source
of confusion for people new to Python - as of the moment of writing this, YouTube video
explaining what this bit of code does by Corey Schafer is sitting on 1,7 million views
(one of his best), and video explaining the same concept by mCoding is at 865 thousand
views (his most viewed video ever). Question asking what this idiom does on StackOverflow
has more than 7600 upvotes, and more than 3200 bookmarks (second most upvoted Python
question). Furthermore, this improvement fits in line with introduction of dataclasses,
which is basically a way of declaring classes without writing boilerplate magic methods.

This very telling, self-explanatory decorator provides an alternative for people who don’t
want to remove the  ``if __name__ == "__main__": main()`` idiom altogether, be it for lack of
understanding, concerns about future extensibility or any other reason.

Example:
    This (following ``from main_function import main_function``): ::

        @main_function
        def main() -> None:
            print("Hello, world!")


    Is fully equivalent to this::

        def main() -> None:
            print("Hello, world!")

        if __name__ == "__main__":
            main()


For further discussion that has inspired this PyPi, please see this:
   https://discuss.python.org/t/built-in-is-main-function-as-a-more-beginner-friendly-alternative-to-if-name-main/18570




Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


License
-------
MIT
