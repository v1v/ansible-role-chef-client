Ansible Role: Chef-client  [![Build Status](https://travis-ci.org/v1v/ansible-role-chef-client.svg?branch=master)](https://travis-ci.org/v1v/ansible-role-chef-client) [![Galaxy](http://img.shields.io/badge/galaxy-v1v.chef-client.svg?style=flat-square)](https://galaxy.ansible.com/list#/roles/2267)

=========

This cookbook is used to configure the system to be a Chef Client. For more information on how Chef itself works, see the [Chef Wiki](http://wiki.opscode.com)

Requirements
------------

NA

Role Variables
--------------

```yaml
# Basic settings
chef_client_install_type: package
chef_client_installer_dir: '/tmp'
chef_client_version: latest

# List of package per OS (You shouldn´t change them!!)
chef_client_package:
  platform:
  platform_version:
  arch:
  installer_dest:
```

Dependencies
------------

NA

Example Playbook
----------------

Including an example of how to use chef-client:

    - hosts: chef_clients
      roles:
         - { role: v1v.chef-client, chef_client_version: latest }

License
-------

GNUv3

Thanks
------

To the Chef community:
- [Chef-Client recipe](https://github.com/opscode-cookbooks/chef-client)

Callbacks plugins:
- [profile-tasks](https://github.com/jlafon/ansible-profile)
- [timestamp](https://github.com/ginsys/ansible-plugins)
- [human_logs](https://github.com/ginsys/ansible-plugins)

Feedback, bugs, requests
------------------------

Are [welcome](https://github.com/v1v/ansible-role-chef-client/issues)!

Author Information
------------------

This role was created in 2014 by [Victor Martinez](http://uk.linkedin.com/in/victormartinezrubio).
