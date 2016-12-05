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
    run('find . \\( -wholename \'*/bin/*\' -o -wholename \'*/ts/*.js\' -o -wholename \'*/dash/lib/*\' -o -wholename \'*/ash/lib/*\' -o -name \'*.gem\' -o -name \'*.bc\' -o -name \'*.aux\' -o -name \'*.jad\' -o -name \'*.m\' -o -name \'*.snu\' -o -name \'*.txt\' -o -name \'*.md\' -o -name \'*.rkt\' -o -name \'*.clj\' -o -name \'*.lsp\' -o -name .yaws -o -name \'*.pdf\' -o -name \'*.ps\' -o -wholename \'*/.idea/*\' -o -name \'*.iml\' -o -name \'*.ser\' -o -name \'*.[ps]k\' -o -name \'*.flip\' -o -name \'*.db\' -o -name \'*.log\' -o -wholename \'*/bower_components/*\' -o -wholename \'*/vendor/*\' -o -wholename \'*/*.xcodeproj/*\' -o -wholename \'*/*.dSYM/*\' -o -wholename \'*/build/*\' -o -wholename \'*/*.app/*\' -o -name \'*.scpt\' -o -wholename \'*/perl/Makefile\' -o -wholename \'*/CMakeFiles/*\' -o -name \'*.cmake\' -o -name \'*.lock\' -o -name \'*.cm[io]\' -o -name \'*.hi\' -o -name \'*.swiftdoc\' -o -name \'*.swiftmodule\' -o -name \'*.rlib\' -o -name \'*.dylib\' -o -name \'*.so\' -o -name \'*.o\' -o -name \'*.beam\' -o -name \'*.dump\' -o -name \'*.pyc\' -o -name \'*.jar\' -o -name \'*.class\' -o -name \'*.bin\' -o -wholename \'*/tmp/*\' -o -name .gitmodules -o -wholename \'*/.git/*\' -o -wholename \'*/node_modules/*\' -o -wholename \'*/.cabal/*\' -o -name \'*.ttf\' -o -name \'*.plist\' -o -name \'*.dot\' -o -name \'*.svg\' -o -name \'*.wav\' -o -name \'*.jpeg\' -o -name \'*.jpg\' -o -name \'*.ico\' -o -name \'*.png\' -o -name \'*.gif\' -o -name .DS_Store -o -name Thumbs.db \\) -prune -o -type f -print | pargs -n 100 node_modules/.bin/editorconfig-tools check')


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
