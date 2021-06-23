import glob
import typer
import subprocess

def run(job: str, pr_name: str):
    repos = glob.glob("repos/*")
    for repo_dir in repos:
        env = {"name":repo_dir.split("/")[-1], "dir": repo_dir}
        print(f"Running for {repo_dir}")
        subprocess.run(["git", "checkout", "-b", pr_name], env=env, cwd=repo_dir)
        subprocess.run(["bash", job], env=env)

if __name__ == "__main__":
    typer.run(run)
