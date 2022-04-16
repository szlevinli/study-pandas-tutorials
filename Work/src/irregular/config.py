import pandas as pd
from pathlib import Path
from typing import Dict, List
from enum import Enum

RenameColumnsDict = Dict[str, str]


class ConfigType(Enum):
    # organization source to code
    ORG_SRC_CDE = 0
    # project source to code
    PRJ_SRC_CDE = 1
    # contract source to code
    CTC_SRC_CDE = 2
    # excel file sheet name to data frame
    FIL_SRC_CDE = 3
    # contract code to report
    CTC_CDE_RPT = 100
    # analysis result row name code to report
    ANR_CDE_RPT = 101
    # analysis result column name code to report
    ANC_CDE_RPT = 102


class Config:
    """
    Attributes:
    -----------
    df_config (DataFrame): config paramters for this app.
        source_name (str): source name
        destination_name (str): destination name
        order (int): sorted by
        type (int): config type
        illustrate (str): config type illustrate
    """

    def __init__(
        self,
        path: Path
    ) -> None:
        self.path = path
        self.df_config: pd.DataFrame = None
        self.load()

    def load(self, sheet_name: int = 0) -> None:
        if not self.path.exists():
            raise FileNotFoundError
        self.df_config = pd.read_excel(
            self.path,
            sheet_name=sheet_name
        )

    def map_to_dict(self, type: ConfigType) -> RenameColumnsDict:
        df = self.df_config.loc[
            self.df_config['type'] == type.value
        ].sort_values(by=['order']) \
            .reset_index(drop=True)

        return dict(zip(
            df['source_name'].values,
            df['destination_name'].values
        ))

    def contract_report_dict(
        self,
        type: ConfigType = ConfigType.CTC_CDE_RPT
    ) -> RenameColumnsDict:
        return self.map_to_dict(type)

    def org_code_dict(
        self,
        type: ConfigType = ConfigType.ORG_SRC_CDE
    ) -> RenameColumnsDict:
        return self.map_to_dict(type)

    def project_code_dict(
        self,
        type: ConfigType = ConfigType.PRJ_SRC_CDE
    ) -> RenameColumnsDict:
        return self.map_to_dict(type)

    def contract_code_dict(
        self,
        type: ConfigType = ConfigType.CTC_SRC_CDE
    ) -> RenameColumnsDict:
        return self.map_to_dict(type)

    def excel_sheet_dict(
        self,
        type: ConfigType = ConfigType.FIL_SRC_CDE
    ) -> RenameColumnsDict:
        return self.map_to_dict(type)

    def analysis_row_dict(
        self,
        type: ConfigType = ConfigType.ANR_CDE_RPT
    ) -> RenameColumnsDict:
        return self.map_to_dict(type)

    def analysis_column_dict(
        self,
        type: ConfigType = ConfigType.ANC_CDE_RPT
    ) -> RenameColumnsDict:
        return self.map_to_dict(type)

    def get_field_name(
        self,
        type: ConfigType
    ) -> List[str]:
        df = self.df_config.loc[
            self.df_config['type'] == type.value
        ].sort_values(by=['order']) \
            .reset_index(drop=True)
        return df['source_name'].values

    def contract_source_field(
        self,
        type: ConfigType = ConfigType.CTC_SRC_CDE
    ) -> List[str]:
        return self.get_field_name(type)

    def contract_code_field(
        self,
        type: ConfigType = ConfigType.CTC_CDE_RPT
    ) -> List[str]:
        return self.get_field_name(type)

    def excel_file_sheets(
        self,
        type: ConfigType = ConfigType.FIL_SRC_CDE
    ) -> List[str]:
        return self.get_field_name(type)
