# sash - setup and administer your hosts over ssh

A simple utility to deploy targets (configuration, scripts) to remote hosts over ssh.

## Installation

```bash
curl -O --output-dir /usr/local/bin https://raw.githubusercontent.com/ant1g/sash/master/sash
```
or
```bash
wget -P /usr/local/bin https://raw.githubusercontent.com/ant1g/sash/master/sash
```

Note that `/usr/local/bin` can be replaced with a different directory that is on your `PATH`.

Make it executable:

```bash
chmod +x /usr/local/bin/sash
```

## Help

```
Usage: sash [-hvpd] <RUNBOOK|HOSTNAME> <TARGET> [OPTIONS] [ENV_VARIABLES]

Deploy files and scripts (targets) on remote hosts over SSH.

  -h, --help                        show this help
  -v, --version                     display version
  -d, --deploy  RUNBOOK             targets defined in FILE or a specific
                HOSTNAME TARGET     TARGET to be deployed on HOSTNAME
  -p, --package TARGET              create an archive with the TARGET ready
                                    to be deployed

If no argument is provided, the deploy action will run.

A TARGET is a folder containing files to be deployed, as well as an executable
named 'deploy'. The whole content of the TARGET will be deployed to the remote
host and the 'deploy' command will be executed.
It is possible to setup different variants or flavors for a TARGET.
See documentation and examples for more details.

Environment variables can be set in the RUNBOOK directly, or as extra
command line arguments directly as key-value pairs.
These variables will be placed in a 'deploy.env' file on the remote host,
as well as being sourced before executing the 'deploy' script.

This sash script will also be uploaded to the remote host during deployment,
where it can be sourced and used for its utility functions, or used again to deploy
targets to other remote hosts.

Examples:

sash etc/hosts.prd MY_VERSION=1.0.0 MY_INSTALL_DIR=/opt/myapp
sash example.com flavor1:my-target MY_INSTALL_DIR=/opt/myapp
sash example.com my-target SASH_FLAVOR=flavor1 MY_INSTALL_DIR=/opt/myapp
sash --package my-target VERSION=2.0.0 MY_INSTALL_DIR=/opt/myapp > package.tgz
sash --package my-target --file package.tgz VERSION=2.0.0 MY_INSTALL_DIR=/opt/myapp

The SSH authentication is for the user to arrange (~/.ssh/config)
```
