__author__ = 'chris'

import fabric, os
from fabric.api import *
from templates.base import base_html, home_html
from templates.errors import error404_html, error500_html
from project.settings import settings_content
from project.local_settings import local_settings
from project.urls import urls


def localhost():
    env.hosts = ['localhost']
    env.directory = '/Users/chris/PycharmProjects'


def customdir(dir):
    env.hosts = ['localhost']
    env.directory = dir


def create_site(name):
    """
    Creates a new Django site
    """
    if os.path.exists("{0}/{1}".format(env.directory, name)):
        print "[ERROR] There is an existing folder named {0}".format(name)

    prefix_command = ""
    virtualenvwrapper = False

    with cd(env.directory):
        if fabric.contrib.console.confirm("Would you like to use virtualenvwrapper?"):
            run("export WORKON_HOME=/srv/www && source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv --no-site-packages --distribute {0}".format(name))
            prefix_command = "export WORKON_HOME=/srv/www && source /usr/local/bin/virtualenvwrapper.sh && workon {0}".format(name)
            virtualenvwrapper = True
        else:
            run("virtualenv --no-site-packages --distribute %s" % name)
            prefix_command = "source {0}/{1}/bin/activate".format(env.directory, name)

        with prefix(prefix_command):
            # install default packages
            run("pip install Django")
            run("pip install django-compressor")
            run("pip install South")

            # prompt user for installing optional apps
            for optional_app in optional_apps:
                if fabric.contrib.console.confirm("Would you like to install {0}?".format(optional_app)):
                    run("pip install {0}".format(optional_app))

            with cd(name):
                # sass
                with prefix('export GEM_HOME={0}/{1} && export GEM_PATH={0}/{1} && export RUBYLIB={0}/{1}/lib/ruby/1.8'.format(env.directory, name)):
                    run('gem install sass && gem install bourbon')
                    run('gem install compass && gem install zurb-foundation')

                # Start Django Project
                run("django-admin.py startproject {0}".format(name))

                #set up static and media folders
                run("mkdir public-www")
                run("mkdir public-www/media")
                run("mkdir public-www/static")

                # within project folder
                with cd(name):
                    pwd = run('pwd')
                    run("pip freeze > requirements.txt")

                    if fabric.contrib.console.confirm("Would you like to initialise a Git repository?"):
                        run("git init")
                        with open("{0}/.gitignore".format(pwd), 'w') as f:
                            f.write(gitignore)
                    elif fabric.contrib.console.confirm("Would you like to initialise a Mercurial repository?"):
                        run("hg init")
                        with open("{0}/.hgignore".format(pwd), 'w') as f:
                            f.write(hgignore)

                    # static & foundation
                    with prefix('export GEM_HOME={0}/{1} && export GEM_PATH={0}/{1} && export RUBYLIB=$PWD/lib/ruby/1.8'.format(env.directory, name)):
                        run('compass create static -r zurb-foundation --using foundation')


                    # create templates
                    run("mkdir templates")
                    with cd('templates'):
                        pwd = run('pwd')

                        with open("{0}/base.html".format(pwd), "w") as f:
                            f.write(base_html.replace("[name]", name))

                        with open("{0}/home.html".format(pwd), "w") as f:
                            f.write(home_html)

                        with open("{0}/500.html".format(pwd), "w") as f:
                            f.write(error500_html)

                        with open("{0}/404.html".format(pwd), "w") as f:
                            f.write(error404_html)

                    # within project app folder
                    with cd(name):
                        pwd = run('pwd')

                        #edit settings file
                        with open("{0}/settings.py".format(pwd), "w") as f:
                            f.write(settings_content.replace('[name]',name))

                        #create new urls
                        with open("{0}/urls.py".format(pwd), "w") as f:
                            f.write(urls)

                        #create local settings
                        with open("{0}/local_settings.py".format(pwd), 'a') as f:
                            f.write(local_settings.replace('[name]',name))

                    if virtualenvwrapper:
                        run('setvirtualenvproject')

                    # TODO copy over /assets
    print "-----------------------------------------------------"
    print "Folder: {0}/{1}".format(env.directory, name)
    print "Create database 'fdb_{0}', run 'python manage.py syncdb' and copy over the /static folder to your projects root directory.".format(name)
    print "-----------------------------------------------------"

optional_apps = [
    'django-debug-toolbar',
    'django-extensions',
    'django-admin-tools',
    'ipython',
    'python-memcached',
    'typogrify',
    'simplejson',
    'slimit',
    'yolk',
    'pillow',
    'django-easy-pjax',
    'django-haystack',
    'raven',
    'django-parsley',
]

gitignore = """.DS_Store
._*
*.pyc
._.DS_Store
local_settings.py
.sass-cache
CACHE/
"""

hgignore = gitignore