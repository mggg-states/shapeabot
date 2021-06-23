import glob
import typer
import subprocess

def run(job: str, pr_name: str, message: str = ""):
    repos = glob.glob("repos/*")
    for repo_dir in repos:
        env = {
                "name":repo_dir.split("/")[-1], 
                "GIT_AUTHOR_NAME": "shapeabot",
                "GIT_AUTHOR_EMAIL": "contact@mggg.org",
                "GIT_COMMITTER_NAME": "shapeabot",
                "GIT_COMMITTER_EMAIL": "contact@mggg.org",
                "EMAIL": "contact@mggg.org",
                "dir": repo_dir
              }
        print(f"Running for {repo_dir}")
        subprocess.run(["git", "checkout", "-b", pr_name], env=env, cwd=repo_dir)
        subprocess.run(["bash", job], env=env)
        subprocess.run(["git", "add", "-A"], env=env, cwd=repo_dir)

        subprocess.run(["git", "commit", f"-m", "{message} (automated run of {}"], env=env, cwd=repo_dir)
        subprocess.run(["git", "checkout", "master"], env=env, cwd=repo_dir)


if __name__ == "__main__":
    typer.run(run)
