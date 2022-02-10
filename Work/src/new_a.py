import argparse
from pathlib import Path
import pandas as pd

arg_parser = argparse.ArgumentParser(
    description='根据本期数据和上期数据统计不规范合同操作情况.'
)

# 位置参数
arg_parser.add_argument(
    'Tp',
    metavar='tp',
    type=str,
    help='本期数据文件名称(含扩展名).'
)

arg_parser.add_argument(
    'Lp',
    metavar='lp',
    type=str,
    help='上期数据文件名称(含扩展名).'
)

# 可选参数
arg_parser.add_argument(
    '-d',
    '--data',
    action='store',
    default='data',
    help='文件目录. 基于当前目录.'
)

args = arg_parser.parse_args()
