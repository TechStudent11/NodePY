# NodePY
The NodeJS of Python.

## How does it work?
Well I'm glad you asked! NodePY is a simple CLI tool. Helps for script management and whatnot.

> And soon, maybe even package control...

But for now... script management. When NodePY initializes a project (see [init command](#init)), it creates a `project.json` which is what differentiates different projects. The `project.json` file contains some information about the project. Like the `name` or the `scripts`.

## How do I install it?
It's easy! Just run:
```shell
pip install git+https://github.com/TechStudent11/NodePY.git#egg_info=nodepy
```
Yeah, I know...
### Long
But that's because, this isn't on [PyPI](https://pypi.org).

## Okay, I installed it. But how do I use it?
Once NodePY is installed, you will have access to the `nodepy` command.

If you just run, `nodepy`, you will get some help text.

## Example help text:
```
Usage: nodepy [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  init  Initializes a project.
  run   Runs a script within the project.
```

## What commands are there?
Below, you will find a list of all the commands that I've added.

### init
This command initializes a NodePY project.

Example usage:
```bash
nodepy init
```

It will then ask for some information like the name, etc.

### run
This command runs a script within a project.

Example usage:
```bash
nodepy run main
```

This will run the `main` script inside of the `project.json`.
