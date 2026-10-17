import math


def factorial(number):
    if number < 0:
        raise ValueError("Number cannot be negative")
    return math.factorial(number)


def compound_amount(principal, rate, years):
    if principal < 0 or rate < 0 or years < 0:
        raise ValueError("Values cannot be negative")

    return principal * (1 + rate / 100) ** years


def sine(degrees):
    return math.sin(math.radians(degrees))


def cosine(degrees):
    return math.cos(math.radians(degrees))


def tangent(degrees):
    return math.tan(math.radians(degrees))


def circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def rectangle_area(length, width):
    if length < 0 or width < 0:
        raise ValueError("Dimensions cannot be negative")
    return length * width


def triangle_area(base, height):
    if base < 0 or height < 0:
        raise ValueError("Dimensions cannot be negative")
    return 0.5 * base * height