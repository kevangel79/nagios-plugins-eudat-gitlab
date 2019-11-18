A simple nagios probe that connects to a GitLab liveness endpoint and checks that the response is

```
{"status": "ok"}
```

It returns:

0, if the status was ok.

2, otherwise.

Usage: ./check_gitlab_liveness.sh [-h] -u URL [-t TIMEOUT] [-d]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           debug mode

required arguments:
  -u URL, --url URL     GitLab liveness endpoint to check
  -t TIMEOUT, --timeout TIMEOUT
