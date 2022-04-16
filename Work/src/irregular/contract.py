import pandas as pd
from irregular.config import Config
from irregular.org import Org


class Contract:
    def __init__(
        self,
        df_contract: pd.DataFrame,
        config: Config
    ) -> None:
        """
        Parameters:
        -----------
        df_contract (DataFrame): contracts data, must be include:
            project_id (int): project id
            resource_name (str): resource name
            contract_no (str): contract NO.
            part_A (str): part A
            part_B (str): part B
            category (str): irregular contract's category
            illustrate (str): irregular constract's illustrate
        """
        self.df_contract = df_contract
        self.config = config

    def report(
        self,
        df_project: pd.DataFrame
    ) -> pd.DataFrame:
        """
        Parameters:
        -----------
        df_project (DataFrame): project with org.
            branch_id (int): branch id
            branch_name (str): branch name
            dept_id (int): department id
            dept_name (str): department name
            project_id (int): project id
            project_name (str): project name
        """
        df = pd.merge(
            self.df_contract,
            df_project,
            on='project_id',
            suffixes=('', '_y')
        )
        df = df[self.config.contract_code_field()] \
            .rename(columns=self.config.contract_report_dict()) \
            .reset_index(drop=True)

        return df

    def counted(
        self
    ) -> pd.DataFrame:
        """
        Group by project and category.
        """
        df = self.df_contract \
            .groupby([
                'project_id',
                'category'])[['contract_no']] \
            .count() \
            .rename(columns={'contract_no': 'count'}) \
            .reset_index()
        return df

    def counted_with_org(
        self,
        org: Org
    ) -> pd.DataFrame:
        return pd.merge(
            org.project(),
            self.counted(),
            on='project_id'
        )
