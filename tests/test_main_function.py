#!/usr/bin/env python

"""Tests for `main_function` package."""

from typing import Any

from main import main_function


def main():
    raise RuntimeError("This should not break the test")


def main1(argv: list[Any]):
    raise RuntimeError("This should not break the test")


def main2(*args: Any):
    raise RuntimeError("This should not break the test")


try:

    @main_function
    def main_bad():
        raise RuntimeError("This should break the test")

except RuntimeError:
    print("This should break the test")

try:

    @main_function
    def main_bad1(argv: list[Any]):
        raise RuntimeError("This should break the test")

except RuntimeError:
    print("This should break the test")

try:

    @main_function
    def main_bad2(*args: Any):
        raise RuntimeError("This should break the test")

except RuntimeError:
    print("This should break the test")
