import os
import subprocess
import sys

def run3(cmd, stdin_data=b"", env={}):
    e = dict(os.environ)
    e.update(env)

    p = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=e)
    stdout_data, stderr_data = p.communicate(stdin_data)
    rc = p.returncode

    return (rc, stdout_data, stderr_data)


def run(cmd, stdin_data=b"", env={}, acceptable_returncodes=[0]):
    (rc, stdout_data, stderr_data) = run3(cmd, stdin_data, env)

    if not rc in acceptable_returncodes:
        sys.stderr.write(stderr_data.decode())
        raise subprocess.CalledProcessError(rc, cmd, stderr_data)

    return stdout_data


def path_to_tests():
    this_path = os.path.abspath(__file__)
    return os.path.dirname(this_path)
