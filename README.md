## shapeabot

To clone all the repos:
```
python clone.py
```

To run a bash job/script:
```
python run.py [job_path] [pr_name]
```

The following env vars are exposed:
```
$name
$dir
$GIT_AUTHOR_NAME
$GIT_AUTHOR_EMAIL
$GIT_COMMITTER_NAME
$GIT_COMMITTER_EMAIL
```

Example usage:
```
python clone.py
python run.py jobs/test-echo.sh test
```

