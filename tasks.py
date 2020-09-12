from invoke import run, task


@task
def safety():
    run('safety check')


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
    run('''git ls-files -z |
        grep -av patch |
        xargs -0 -r -n 100 $(shell npm bin)/eclint check''')


@task
def xmllint():
    run('find . -name "*.xml" -exec xmllint --noout {} 2>&1 \\;')


@task
def checkbashisms():
    run('stank . | grep -v node_modules | xargs checkbashisms')


@task
def shellcheck():
    run('stank -exInterp zsh . | grep -v node_modules | xargs shellcheck')


@task
def funk():
    run('funk .')


@task(pre=[
    safety,
    pep8,
    pylint,
    pyflakes,
    flake8,
    editorconfig,
    xmllint,
    checkbashisms,
    shellcheck,
    funk
    ])
def lint():
    pass
