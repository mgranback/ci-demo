import os
import sys

def count_errors(lines):
    return sum(1 for line in lines if "ERROR" in line)

