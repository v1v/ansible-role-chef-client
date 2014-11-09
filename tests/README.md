Commands
===========================================

For Docker testing purposes :

	$ docker build --rm=true -t chef-client:latest .
	$ docker run -i --privileged -p -v `pwd`/..:/playbook chef-client
	$ containerid=`docker ps -a | grep Exited | head -n 1 | cut -d" " -f 1`
	$ docker start ${containerid}
	$ docker attach ${containerid}

For Vagrant testing purposes :

	$ vagrant up
	$ vagrant provision

For Test Kitchen testing purposes :

	$ ln -fs .kitchen.vagrant.yml .kitchen.yml
	$ kitchen list all
	$ kitchen converge all

If you get some weird issues about some ports (which have already been allocated) then:

	$ sudo service docker restart
