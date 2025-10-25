import csv
import math
import sys
import argparse
import unittest
from collections import defaultdict
from typing import Dict, List, Any, Tuple

def read_csv_file(filename):
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

data = read_csv_file("penguins.csv")
print(data)
