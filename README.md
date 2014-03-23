Source code for my blog, avaliable at [lexev.org](http://www.lexev.org) and hosted on [openshift cloud](https://openshift.redhat.com)

It is build with python 2.7, django, mysql.

### Runtime Configuration (thanks to [openshift-diy-py27-django example](https://github.com/ehazlett/openshift-diy-py27-django), most install sequence i've got from there)

Create a new OpenShift app:

* `rhc-create-app -a <app_name> -t diy-0.1`

Add mysql, phpmyadmin, cron cartridges:

* `rhc-ctl-app -a <app_name> -e add-mysql-5.1`
* `rhc-ctl-app -a <app_name> -e add-phpmyadmin-3.4`
* `rhc-ctl-app -a <app_name> -e add-cron-1.4`

Login to the application host using the credentials from the above command.  It will look like `ssh://c8812345:123214@<app_name>-username.rhcloud.com`:

* `ssh c8812345:123214@<app_name>-username.rhcloud.com`

Change into the application tmp directory:

* `cd $OPENSHIFT_TMP_DIR`

Download Python2.7 and extract:

* `wget http://python.org/ftp/python/2.7.3/Python-2.7.3.tar.bz2`
* `tar jxf Python-2.7.3.tar.bz2`

Build and install Python

* `cd Python-2.7.3`
* `./configure --prefix=$OPENSHIFT_REPO_DIR/../`
* `make ; make install`

Export new Python path for later configuration (you will need to run this if you logout, etc.):

* `export PATH=$OPENSHIFT_REPO_DIR/../bin:$PATH`

Check that new Python is used (should be `Python 2.7.3`):

* `python -V`

Install setuptools and pip

* `cd $OPENSHIFT_TMP_DIR`
* `wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz`
* `tar zxf setuptools-0.6c11.tar.gz`
* `cd setuptools-0.6c11`
* `python setup.py install`
* `cd $OPENSHIFT_TMP_DIR`
* `wget http://pypi.python.org/packages/source/p/pip/pip-1.1.tar.gz`
* `tar zxf pip-1.1.tar.gz`
* `cd pip-1.1`
* `python setup.py install`

Install uWSGI
* `cd $OPENSHIFT_TMP_DIR`
* `pip install uwsgi`

Install MySQL-python
* `cd $OPENSHIFT_TMP_DIR`
* `pip install MySQL-python`

Cleanup
* `cd ~`
* `rm -rf $OPENSHIFT_TMP_DIR/*`

### Application Setup

Clone / Fork this repo.

Add an upstream to OpenShift:
* Get the `Git URL` from `rhc app show -a <app_name>`
* `git remote add openshift <GIT_URL_from_above>`
* `git push openshift master`

Note: you may get an error during the git push to openshift saying the repo is not in sync.  If you don't have any changes in the OpenShift repo, you can force the push with:

`git push -f openshift master`

### Set custom variables:

```
# linkedin
rhc set-env LINKEDIN_STORE_CACHE="False" -a <app_name>
rhc set-env LINKEDIN_CONSUMER_KEY="TBD" -a <app_name>
rhc set-env LINKEDIN_CONSUMER_SECRET="TBD" -a <app_name>
rhc set-env LINKEDIN_USER_TOKEN='TBD' -a <app_name>
rhc set-env LINKEDIN_USER_SECRET='TBD' -a <app_name>
rhc set-env LINKEDIN_RETURN_URL='TBD' -a <app_name>

# email
rhc set-env EMAIL_HOST='TBD' -a <app_name>
rhc set-env EMAIL_HOST_USER='TBD' -a <app_name>
rhc set-env EMAIL_HOST_PASSWORD='TBD' -a <app_name>
rhc set-env EMAIL_PORT='TBD' -a <app_name>
rhc set-env EMAIL_USE_TLS='True' -a <app_name>

# to list all custom variables
rhc list-env

# to unset cuctom variables
rhc list-unset

# help
rhc help env
```

Get linked-in keys here: [https://www.linkedin.com/secure/developer](https://www.linkedin.com/secure/developer)

### Useful commands

- rhc ssh -a <app_name>


### * Note

If you change the Django application name (in the repo it's named `myblog`) you will also need to update the `.app_name` file with the new name in order for the OpenShift start/stop scripts to work.
