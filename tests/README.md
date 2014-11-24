chef-client role TESTING
========================

Bundler
-------
A ruby environment with Bundler installed is a prerequisite for using
the testing harness shipped with this role. At the time of this
writing, it works with Ruby 2.0 and Bundler 1.7.4. All programs
involved, with the exception of Vagrant and Docker, can be installed by cd'ing
into the tests directory of this role and running "bundle install"


Style Testing
-------------
Ansible style can be performed by [Ansible-lint](https://github.com/willthames/ansible-lint) by issuing
```
ansible-lint site.ci.yml
```

Integration Testing
-------------------
Integration testing is performed by [Test Kitchen](http://kitchen.ci/). Test Kitchen will
use either the Vagrant driver or Docker drivers to instantiate
machines and apply roles. Tests should be designed to
ensure that a role has accomplished its goal.

Integration Testing using Vagrant
---------------------------------
Integration tests can be performed on a local workstation using
Virtualbox or VMWare. Detailed instructions for setting this up can be
found at the [Bento](https://github.com/opscode/bento) project web site.

Integration tests using Vagrant can be performed with either
```
export KITCHEN_YAML=.kitchen.vagrant.yml
bundle exec kitchen test
```
or
```
export KITCHEN_YAML=.kitchen.vagrant.yml
kitchen test
```

Integration Testing using Docker
--------------------------------
Integration tests can be performed on [Docker provider](https://github.com/portertech/kitchen-docker) using
Test Kitchen plugins.

Integration tests using docker driver can be performed with either
```
export KITCHEN_YAML=.kitchen.docker.yml
bundle exec kitchen test
```
or
```
export KITCHEN_YAML=.kitchen.docker.yml
kitchen test
```

Words about Docker testing
--------------------------
In order for Docker to perform manual tests, the below list of commands need to happen:

```
export DOCKERFILE=Dockerfile.[centos|fedora|ubuntu|debian]
docker build --rm=true -t chef-client:latest $DOCKERFILE
docker run -i --privileged -v `pwd`/..:/playbook chef-client
```

Then, in order to test the idempotent:
```
containerid=`docker ps -a | grep Exited | head -n 1 | cut -d" " -f 1`
docker start ${containerid}
docker attach ${containerid}
```

Words about Vagrant testing
--------------------------
In order for Vagrant to perform manual tests, the below list of commands need to happen:

```
vagrant up
vagrant provision
```
