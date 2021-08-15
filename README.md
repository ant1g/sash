# sash - setup and administer your hosts over SSH

A simple utility to deploy targets (configuration, scripts) to remote hosts over SSH.

## Installation

Installing it is straighforward, because sash consists only of a single script.

```bash
curl -O --output-dir /usr/local/bin/ https://raw.githubusercontent.com/ant1g/sash/master/sash
```
or
```bash
wget -P /usr/local/bin/ https://raw.githubusercontent.com/ant1g/sash/master/sash
```

Note that `/usr/local/bin/` can be replaced with a different directory that is on your `$PATH`, such as `~/bin/` or `~/.local/bin`.

Don't forget to make it executable:
```bash
chmod +x /usr/local/bin/sash
```

To uninstall, simply remove the sash script:
```bash
rm /usr/local/bin/sash
```

## Getting started

A deployment target is simply a folder, say `hello`, that contains an executable file called `deploy`.

In this `deploy` executable contains the deployment logic that the developer sees fit.

Example:
```bash
sash example.host examples/hello
```

This will upload the `hello` target and run the `deploy` executable on the remote host `example.host`, over the SSH protocol with the OpenSSH client.

The SSH authentication configuration should be done by the developer in `~/.ssh/config`, for more information please consult the [official documentation](https://www.ssh.com/academy/ssh/config).

Configuration can be given to the deployment script as follows:
```bash
sash example.host examples/hello SAY="Hi!"
```

This will set a `SAY` variable available in the environment of the script.

## Help screen

```bash
Usage: sash [-hvpd] <RUNBOOK|HOSTNAME> <TARGET> [OPTIONS] [ENV_VARIABLES]

Deploy files and scripts (targets) on remote hosts over SSH.

  -h, --help                        show this help
  -v, --version                     display version
  -d, --deploy  RUNBOOK             targets defined in FILE or a specific
                HOSTNAME TARGET     TARGET to be deployed on HOSTNAME
  -p, --package TARGET              create an archive with the TARGET ready
                                    to be deployed

If no argument is provided, the deploy action will run.
```
