import subprocess

def parse_default_branch(cwd: str) -> str:
    output = subprocess.run(
        "git rev-parse --abbrev-ref origin/HEAD",
        shell=True,
        cwd=cwd,
        capture_output=True,
    )
    return str(output.stdout.decode()).rstrip().split("/")[-1]

def list_repos():
    return dm.list_gh_repos(account=ACCOUNT, account_type="orgs")

