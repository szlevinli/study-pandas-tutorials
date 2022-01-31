import argparse
import pandas as pd
from pathlib import Path
from typing import List


def getFilePath() -> str:
    pass


def getGroupBy() -> List[str]:
    pass


def getOutputFileNamePrefix() -> str:
    pass


def getOutputDir() -> str:
    pass


def main() -> None:
    # df = pd.read_excel(getFilePath())
    # grouped = df.groupby(getGroupBy())
    # for name, grp in grouped:
    #     fileName = getOutputFileNamePrefix() + '-'.join(name) + '.xlsx'
    #     grp.to_excel(fileName)
    print(Path.cwd())


if __name__ == "__main__":
    main()
