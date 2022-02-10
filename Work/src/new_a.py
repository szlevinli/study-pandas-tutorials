import argparse
from pathlib import Path
import pandas as pd

# lp: last period
# tp: this period

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

arg_parser.add_argument(
    '--tp-sheet',
    action='store',
    help='本期工作表名称. 默认第一个工作表'
)

arg_parser.add_argument(
    '--lp-sheet',
    action='store',
    help='上期工作表名称. 默认第一个工作表'
)

arg_parser.add_argument(
    '--keys',
    action='store',
    nargs='+',
    type=str,
    default='合同编号',
    help='关键字. 多个用空格分隔. 默认: 合同编号'
)


def get_data_path(p: str) -> Path:
    return Path.cwd() / p


def get_lp_path(p: str) -> Path:
    return Path.cwd() / p


if __name__ == '__main__':
    args = arg_parser.parse_args()
    print(vars(args))
