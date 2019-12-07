import os
import sys
from pprint import pprint as pp
import pandas
import pickle
import datetime

here_dir = os.path.dirname(os.path.realpath(__file__))

def test_func(x):

    x = x * 2

    print("hello")

    return x + 3

def explore_object(obj):

    print("{}\n----------------\n".format(obj.__name__))

    obj_dir = dir(obj)

    for i in obj_dir:

        y = getattr(obj, i)

        print("\n------------------------------")
        print("\n------------------------------")

        print("{}: \n".format(i))

        print("Type: \n{}".format(type(y)))

        print("Repr: \n{}".format(y))

        print("\ndir({}) list: ".format(i))
        pp(dir(y))

        print("------------------------------\n")
        print("------------------------------\n")

        opt = input("\n8 => next item in {}\n5 => explore {}\n-> ".format(obj.__name__, i))

        if opt == "8":

            continue

        elif opt == "5":

            explore_object(y)


