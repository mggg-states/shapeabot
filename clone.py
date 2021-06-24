import gdutils.datamine as dm
import typer
import subprocess
from env import env

ACCOUNT = "mggg-states"


def list_repos():
    return dm.list_gh_repos(account=ACCOUNT, account_type="orgs")


def clone():
    repos = [x for x in list_repos() if x[0].endswith("-shapefiles")]

    for each_repo_name, each_repo_url in repos:
        subprocess.run(["git", "clone", each_repo_url], cwd="repos", env=env)


if __name__ == "__main__":
    typer.run(clone)
