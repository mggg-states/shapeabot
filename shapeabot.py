import subprocess


def parse_default_branch(cwd: str) -> str:
    output = subprocess.run(
        "git rev-parse --abbrev-ref origin/HEAD",
        shell=True,
        cwd=cwd,
        capture_output=True,
    )
    return str(output.stdout.decode()).rstrip().split("/")[-1]


env = {
    "GIT_AUTHOR_NAME": "shapeabot",
    "GIT_AUTHOR_EMAIL": "contact@mggg.org",
    "GIT_COMMITTER_NAME": "shapeabot",
    "GIT_COMMITTER_EMAIL": "contact@mggg.org",
    "EMAIL": "contact@mggg.org",
}
