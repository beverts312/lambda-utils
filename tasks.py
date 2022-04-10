from invoke import task


def black(c, check):
    cmd = f"black . --line-length=79 {'--check' if check is True else ''}"
    return c.run(cmd)


@task(aliases=["f"])
def format(c):
    return black(c, False)


@task(aliases=["cf", "fc"])
def check_format(c):
    return black(c, True)


@task(aliases=["l", "lp"])
def lint(c):
    return c.run("pycodestyle .")


@task(aliases=["bp"])
def build_and_publish(c):
    c.run("rm -rf dist")
    c.run("python setup.py bdist_wheel")
    return c.run("python -m twine upload dist/*.whl --verbose")