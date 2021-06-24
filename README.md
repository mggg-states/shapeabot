## shapeabot

To clone all the repos:
```
python shapeabot.py clone
```

To run a bash job/script:
```
python shapeabot.py run [job_path] [pr_name]
```

The following env vars are exposed to the executable $[job_path]$:
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
python shapeabot.py clone
python shapeabot.py run jobs/test-echo.sh test
```

