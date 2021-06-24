import glob
import typer
import subprocess
from env import env


def push():
    repos = glob.glob("repos/*")
    for repo_dir in repos:
        env["name"] = repo_dir.split("/")[-1]
        env["dir"] = repo_dir

        subprocess.run(["git", "push"], env=env, cwd=repo_dir)


if __name__ == "__main__":
    typer.run(push)
