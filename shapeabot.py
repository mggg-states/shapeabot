import subprocess
import gdutils.datamine as dm
import typer
import subprocess
import glob
from utils import *
from conf import *

app = typer.Typer()

@app.command()
def clone():
    repos = [x for x in list_repos() if x[0].endswith("-shapefiles")]

    if not os.path.isdir("repos"):
        os.mkdir("repos")

    for each_repo_name, each_repo_url in repos:
        subprocess.run(["git", "clone", each_repo_url], cwd="repos", env=env)

@app.command()
def run(job: str, pr_name: str, message: str = "", test: bool = True):
    repos = glob.glob("repos/*")
    for repo_dir in repos:
        if test and not "test" in repo_dir:
            continue

        env["name"] = repo_dir.split("/")[-1]
        env["state"] = env["name"].split("-")[0]
        env["dir"] = repo_dir

        print(f"Running for {repo_dir}")

        subprocess.run(["git", "checkout", "-b", pr_name], env=env, cwd=repo_dir)

        subprocess.run([job], env=env)

        subprocess.run(["git", "add", "-A"], env=env, cwd=repo_dir)
        subprocess.run(
            ["git", "commit", f"-m", "{message} (automated run of {}"],
            env=env,
            cwd=repo_dir,
        )

        subprocess.run(
            ["git", "checkout", parse_default_branch(repo_dir)],
            env=env,
            cwd=repo_dir,
        )

@app.command()
def push():
    repos = glob.glob("repos/*")
    for repo_dir in repos:
        env["name"] = repo_dir.split("/")[-1]
        env["dir"] = repo_dir

        subprocess.run(["git", "push"], env=env, cwd=repo_dir)

if __name__ == "__main__":
    app()
