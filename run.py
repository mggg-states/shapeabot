import glob
import typer
import subprocess
import shapeabot
from shapeabot import env


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
            ["git", "checkout", shapeabot.parse_default_branch(repo_dir)],
            env=env,
            cwd=repo_dir,
        )


if __name__ == "__main__":
    typer.run(run)
