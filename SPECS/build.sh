
## Get the svn source directory
cd ..
SRC_DIR=$PWD/vendor
echo "SVN Source Directory: " $SRC_DIR
cd trunk

## Select what to build
REBUILD_SRPMS=false
BUILD_FROM_TARBALLS=false

############################
####### SOURCE RPMS ########
############################

if $REBUILD_SRPMS ;
then
	echo "STARTING TO REBUILD FROM SRC.RPMS "
	### LUA ###
	rpmbuild --rebuild ../vendor/lua-5.1.4-4.1.el6.src.rpm

	### FLEXMOCK ###
	yum install rubygems
	rpmbuild --rebuild ../vendor/rubygem-flexmock-0.8.6-2.3.src.rpm

	### RUBYGEM ###
	rpm -i $HOME/rpmbuild/RPMS/noarch/rubygem-flexmock-0.8.6-2.3.noarch.rpm
	rpm -i $HOME/rpmbuild/RPMS/noarch/ruby-flexmock-0.8.6-2.3.noarch.rpm
	rpmbuild --rebuild ../vendor/rubygem-rake-0.8.7-2.1.el6.src.rpm

	### PYTHON ###
	yum install systemtap-sdt-devel 
	yum install tcl-devel
	yum install tk-devel

	rpm -i $HOME/tmp/gdbm-devel-1.8.0-36.el6.x86_64.rpm
	rpm -i $HOME/tmp/valgrind-devel-3.6.0-5.el6.x86_64.rpm
	rpm -i $HOME/tmp/libffi-devel-3.0.5-3.2.el6.x86_64.rpm
	yum install tix
	rpm -i $HOME/tmp/tix-devel-8.4.3-5.el6.x86_64.rpm 
	rpmbuild --rebuild ../vendor/python27-2.7.5-1.ius.el6.src.rpm
fi

###################################
####### SOURCES in TARBALL ########
###################################

if $BUILD_FROM_TARBALLS ;
then
	echo "STARTING TO BUILD FROM TARBALLS "
	### PYTHON-NOSE ###
	sudo rpm -i $HOME/rpmbuild/RPMS/x86_64/python27-libs-2.7.5-1.ius.el6.x86_64.rpm
	sudo rpm -i $HOME/rpmbuild/RPMS/x86_64/python27-2.7.5-1.ius.el6.x86_64.rpm
	sudo rpm -i $HOME/rpmbuild/RPMS/x86_64/python27-devel-2.7.5-1.ius.el6.x86_64.rpm
	sudo rpm -i $HOME/rpmbuild/RPMS/x86_64/tkinter27-2.7.5-1.ius.el6.x86_64.rpm
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-nose.spec
	sudo rpm -i $HOME/rpmbuild/RPMS/noarch/python27-nose-1.3.0-1.el6.noarch.rpm
	### PYTHON-PyYaml ###
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-pyyaml.spec
	### PYTHON-Setuptools ###
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-setuptools.spec
	sudo rpm -i $HOME/rpmbuild/RPMS/x86_64/python27-setuptools-1.1.5-2.el6.x86_64.rpm
	### PYTHON-Dateutil ###
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-dateutil.spec
	### PYTHON-distribute ###
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-distribute.spec
	sudo rpm -i $HOME/rpmbuild/RPMS/noarch/python27-distribute-0.7.3-1.el6.noarch.rpm
	### PYTHON-Netifaces ###  -> TO DO
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-netifaces.spec
	### PYTHON-empy ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-empy.spec
	### PYTHON-catkin ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-catkin-pkg.spec
	### PYTHON-rosdep ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-rosdep.spec
	### PYTHON-rosdistro ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-rosdistro.spec
	### PYTHON-rosinstall ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-rosinstall.spec
	### PYTHON-rosinstall-generator ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-rosinstall-generator.spec
	### PYTHON-rospkg ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-rospkg.spec
	### PYTHON-vcstool ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-vcstool.spec
	### PYTHON-wstool ###  
	rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-wstool.spec
fi

## Currently not building ##
rpmbuild -ba --define="_sourcedir $SRC_DIR" python27-netifaces.spec
