Ansible Role: Chef-client  [![Build Status](https://travis-ci.org/v1v/ansible-role-chef-client.svg?branch=master)](https://travis-ci.org/v1v/ansible-role-chef-client)
=========

This cookbook is used to configure the system to be a Chef Client. For more information on how Chef itself works, see the [Chef Wiki](http://wiki.opscode.com)


Requirements
------------

Any pre-requisites that may not be covered by Ansible itself or the role should be mentioned here. For instance, if the role uses the EC2 module, it may be a good idea to mention in this section that the boto package is required.

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

A list of other roles hosted on Galaxy should go here, plus any details in regards to parameters that may need to be set for other roles, or variables that are used from other roles.

`chef::client` is tested on Ubuntu 8.04+, Debian 5.0, CentOS 5.x, Fedora 10+, OpenBSD 4.6, FreeBSD 7.1 and Gentoo.

`runit` cookbook is suggested for RubyGems installation. No other cookbooks are required for clients.


Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

GNUv3

Author Information
------------------

This role was created in 2014 by [Victor Martinez](http://uk.linkedin.com/in/victormartinezrubio).
