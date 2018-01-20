import os
import sys

import argparse

try:
    import cStringIO as StringIO
except:
    import StringIO

import struct
import json
import csv


def import_data (import_file):
    '''
    Imports data from import_file.
    Export to find fixed width row
    Sample row: 161322597 038644351896 0042
    '''

    mask = '9s14s5s'
    data = []
    with open(import_file, 'r') as f:
        for line in f:
            # unpack line to tuple
            fields = struct.Struct(mask).unpack_from(line)
            # Strip any whitespace for each field
            #  pack everything in a list and add to full dataset
            data.append(list([f.strip() for f in fields]))
    return data

def write_data(data, export_format):
    '''Dispatches call to a specific transformer and returns dataset.
    Exceptin is xlsx where we have to save data in a file.
    '''
    if export_format == 'csv':
         return write_csv(data)
    elif export_format == 'json':
         return write_json(data)
    elif export_format == 'xlsx':
         return write_xlsx(data)
    else:
         raise Exception("Illegal format defined")
