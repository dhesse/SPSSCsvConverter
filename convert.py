#!/usr/bin/env python
"""
This script solves two issues often encountered when dealing with .csv
files generated by IBM SPSS Modeler from e.g. a table output node.

* NULL values are encoded by the string '$null$'.
* The file encoding is not utf-8 for some crazy reason.

This script replaces the string '$null$' by either the empty string or
by a user-defined string, and ecodes from a user-defined encoding
(default: latin-1) to utf-8.

Usage:

Run this script with the -h option.
"""
import io
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Fix SPSS Modeler's messy .csv files.")
    parser.add_argument('source', help="Source file from Modeler.")
    parser.add_argument('dest',
                        help=("Destination file. "
                              "Must be different from source."))
    parser.add_argument('--source_enc', '-e', default='latin1',
                        help="source file encoding (default: latin1)")
    parser.add_argument('--null_str', '-n', default='',
                        help="NULL string (default: '')")
    args = parser.parse_args()
    if args.source == args.dest:
       print ("ERROR: Source file and destination"
              " files must be different.")
       sys.exit(1)
    with io.open(args.source, encoding=args.source_enc) as inputFile:
        with io.open(args.dest, 'w', encoding='utf8') as outputFile:
            for line in inputFile:
                outputFile.write(line.replace('$null$', args.null_str))
