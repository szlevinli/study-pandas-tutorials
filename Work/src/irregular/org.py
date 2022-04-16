import pandas as pd


class Org:
    def __init__(
        self,
        df_org: pd.DataFrame,
        df_project: pd.DataFrame,
        root: int = 1001
    ) -> None:
        """
        Parameters:
        -----------
        df_org (DataFrame): organize. columns:
            id (int): org id
            name (str): org name
            pid (int): parent org id
            p_name(str): parent org name

        df_project: projects. columns:
            project_id (int): project id
            project_name (str): project name
            pid (int): parent id

        root: root org id.
        """
        self.df_org = df_org
        self.df_project = df_project
        self.root = root

    def branch(
        self,
    ) -> pd.DataFrame:
        """
        Return branch org.

        Return:
        -------
        df: sub org. columns:
            id (int): org id
            name (str): org name
            pid (int): parent org id
            p_name(str): parent org name
        """
        return self.df_org \
            .loc[self.df_org['pid'] == self.root] \
            .rename(columns={
                'id': 'branch_id',
                'name': 'branch_name'
            }) \
            .reset_index(drop=True)

    def department(
        self,
    ) -> pd.DataFrame:
        """
        Return department org.

        Return:
        -------
        df (DataFrame): organize with branch and department. columns:
            branch_id (int): branch id
            branch_name (str): branch name
            dept_id (int): department id
            dept_name (str): department name
        """
        # branch
        df_branch = self.branch()
        # department
        df_department = pd.merge(
            self.df_org,
            df_branch[['branch_id']],
            left_on='pid',
            right_on='branch_id',
            suffixes=('', '_y')
        )
        # branch -> department
        df = pd.merge(
            df_branch,
            df_department,
            left_on='branch_id',
            right_on='pid',
            suffixes=('', '_y')
        )
        # rename columns
        df = df[[
            'branch_id',
            'branch_name',
            'id',
            'name'
        ]].rename(columns={
            'id': 'dept_id',
            'name': 'dept_name'
        }).reset_index(drop=True)

        return df

    def project(
        self
    ) -> pd.DataFrame:
        """
        Return project with org.

        Returns:
        --------
        df (DataFrame): project with org. columns:
            branch_id (int): branch id
            branch_name (str): branch name
            dept_id (int): department id
            dept_name (str): department name
            project_id (int): project id
            project_name (str): project name

        """
        df = pd.merge(
            self.department(),
            self.df_project,
            left_on='dept_id',
            right_on='pid'
        )
        df = df[[
            'branch_id',
            'branch_name',
            'dept_id',
            'dept_name',
            'project_id',
            'project_name'
        ]].reset_index(drop=True)

        return df
