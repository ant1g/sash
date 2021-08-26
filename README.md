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

This will set a `SAY` variable available in the environment of the script (call it the deployment environment).

## Advanced usage

### Runbooks

A set of targets can be bundled together in runbooks.

Runbooks are just text files that list the hosts and targets to run in order and their configuration.

Example content of a runbook:
```
SAY="Hi!"

example.host ../hello
example.host ../hello SAY="Goodbye"
```

Variables defined at the top of the file will be set to all targets in the runbook.

Variables defined on the host / target line will apply only to that target / host combination.

Important, all paths to targets need to be relative to the runbook file itself.

To execute a runbook simply point to it as first argument:
```bash
sash examples/runbooks/hello
```

If a variable is set on the command line, it will take precedence over the variables in the runbook, if already defined there.

```bash
sash examples/runbooks/hello SAY="Something else"
```

The order of variable precedence is as follows:

`Command line` > `Host / Target line in runbook` > `Top level variables in runbook`

### Templates

Any file that ends with the extension `*.tpl`, `*.templ` or `*.template` in the target will be parsed and environment variables it contains will be expanded to the variables available during deployment (the variables put in runbooks or on the command line).

The file will be available on the remote host at the same relative location, but without the template extension.

For example a file called `vars.json.tpl`, containing:
```json
{
    "lang": "${HELLO_LANG}",
    "env": "${HELLO_ENV}"
}
```

Will be deployed as `vars.json` and the environment variables `${HELLO_LANG}` and `${HELLO_ENV}` will be expended to their respective value available in the deployment environment.

Important, if these variables are not set, the expension will result in an empty string.

### Includes

Includes are useful when a target needs to deploy files that cannot be put in the target folder itself, or when some files need to be shared between targets.

In a file that ends with the extension `*.inc`, `*.incl`, `*.include` or `*.includes`, simply put references to the files that need to be included in the deployment. All paths need to be relative to the include file itself.

Example content of an include file:
```
../hello.shared.json
```

This will include the file `../hello.shared.json` and put it at the root of the remote deployment folder.
Note that file paths in the include file are relative to the folder where the include file itself is located.

It is possible to use includes to do rename or move operations for convenience.
```
../hello.shared.json sub/hello.json
```

The destination parent folder will be created if it does not exist.

### Flavors

It can be useful sometimes to have multiple variations of the same deployment target. A good example of that is when deployment slightly vary between running environments such as acceptance and production.

Flavors can be defined for that purpose.

Flavors are simply sub-folders that are put in a `flavors/` folder in the target.

A target with a specific flavor can be deployed like this:
```bash
sash example.host hello-flavors:acc
```
or
```bash
sash example.host hello-flavors SASH_FLAVOR=acc
```

When a flavor is selected as such, its content will be available on the remote host in the `flavor/` folder.

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
