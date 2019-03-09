#!/usr/bin/env python3

#import
import argparse
import yaml

from src.argparsGraph import argparseGraph as agG

def parsarg():
    parser = argparse.ArgumentParser(description="random option for senarios")
    parser.add_argument("-q", dest="argv1", help="test", type=int)
    parser.add_argument("-w", dest="argv2", help="test", type=int, action='append')
    parser.add_argument("-e", dest="argv3", help="test", type=str, default="test3")
    parser.add_argument("-t", dest="argv4", help="test", type=str, default=False)
    parser.add_argument("-a", dest="argv5", help="test", type=str)
    parser.add_argument("-s", dest="argv6", help="test", type=bool)
    parser.add_argument("-d", dest="argv7", help="test", type=str, action='append')
    args = parser.parse_args()

    return args

def main():
    res_args = parsarg()
    agg = agG("senarios_examples.yml", res_args, verbose=False)
    agg.choose()

if __name__ == '__main__':
    main()
