from invoke import run, task


@task
def pep8():
    run('pep8 .')


@task
def pylint():
    run('find . -name "*.py" -exec pylint {} \\;')


@task
def pyflakes():
    run('pyflakes .')


@task
def flake8():
    run('flake8 .')


@task
def editorconfig():
    run('git ls-files -z | grep -av patch | xargs -0 -r -n 100 $(shell npm bin)/eclint check')


@task
def xmllint():
    run('find . -name "*.xml" -exec xmllint --noout {} 2>&1 \\;')


@task
def bandit():
    run('find . -name \'*.py\' | xargs bandit')


@task
def shlint():
    run('find . \\( -wholename \'*/node_modules*\' \\) -prune -o -type f \( -name \'*.sh\' -o -name \'*.bashrc*\' -o -name \'.*profile*\' -o -name \'*.envrc*\' \) -print | xargs shlint')


@task
def checkbashisms():
    run('find . \\( -wholename \'*/node_modules*\' \\) -prune -o -type f \( -name \'*.sh\' -o -name \'*.bashrc*\' -o -name \'.*profile*\' -o -name \'*.envrc*\' \) -print | xargs checkbashisms -n -p')


@task
def shellcheck():
    run('find . \\( -wholename \'*/node_modules*\' \\) -prune -o -type f \( -name \'*.sh\' -o -name \'*.bashrc*\' -o -name \'.*profile*\' -o -name \'*.envrc*\' \) -print | xargs shellcheck')


@task(pre=[pep8, pylint, pyflakes, flake8, editorconfig, xmllint, bandit, shlint, checkbashisms, shellcheck])
def lint():
    pass
