---
layout: page
title: Build Software
subtitle: GNU Build System
minutes: 25
---

> ## Learning Objectives {.objectives}
>
> * Build the python interpreter
> * Learn the three steps to configure and build software using GNU's build system
> * Learn to build software without superuser privileges


## Download the python interpreter

We need to download the latest version of the python interpreter.  Which is 
located at.

[Python Download Page](https://www.python.org/downloads/release/python-351)


We want version 3.5.1.  On the 3.5.1 download page, we choose the 'Gzipped 
source tarball'.  It's important to note that this is a 'Source release', which 
is often the version you need for Linux operating systems (Ubuntu, Red Hat).

![python download page](img/python-download.png)

> ## Binary or Installer Downloads {.callout}
>
> If you are installing on a Windows or Mac OS X machine; you still can use the 
> source release and then compile for your system.  However, this tends to be a 
> little more difficult since these operating systems do not come packaged with 
> development tools like a compiler.  For convienance, you can choose the 
> installer for the appropriate OS.  These are precompiled packages that work 
> on the designated OS.  Sometimes pakages even have these for specific linux 
> distributions.


## Unpackage the source directory

~~~ {.bash}
$ tar xzvf Python-3.5.1.tgz
$ cd Python-3.5.1
$ ls
~~~

~~~ {.output}
Doc      LICENSE  Makefile.pre.in  Objects  Parser    README      config.guess  configure.ac   setup.py
Grammar  Lib      Misc             PC       Programs  Tools       config.sub    install-sh
Include  Mac      Modules          PCbuild  Python    aclocal.m4  configure     pyconfig.h.in
~~~

## GNU build steps

The GNU build system is broken into three distinct steps.

1. Configure
2. Build
3. Install

The configure step sets up all of the file dependencies for the package on your 
system.  This is the basis of portable software.  If the configure step 
completes successfully, the Build and Install steps should always work.

### Configure

There will be a number of directories and files.  The main file we are 
interested in is the `configure` script.  This will setup the compile time 
dependencies.  The script can take numerous options.

~~~ {.bash}
$ ./configure --help
~~~

You may notice a large number of options.  If you don't know what these options 
do; then you do not need to be concerned with them.  The general rule, is that 
the default (configure with no options) is perfectly appropriate for the 
majority of use cases.

We are intertested in the `--prefix` option, however.  As a segment of the help 
message dictates.

~~~ {.output}
By default, `make install' will install all the files in
`/usr/local/bin', `/usr/local/lib' etc.  You can specify
an installation prefix other than `/usr/local' using `--prefix',
for instance `--prefix=$HOME'.
~~~

Without superuser privileges, you will not be able to install the package in 
`/usr/local`.  Additionally, the `/usr` directory tends to be a system package, 
and it is almost never a good idea to put packages in there.

So let's configure the build to install in a subdirectory `python2` in our home 
directory.

~~~ {.bash}
$ ./configure --prefix=$HOME/python2
~~~

![python configure output](img/python-configure.png)


### Build

Notice the directory now has a `Makefile` in it

~~~ {.bash}
$ ls
~~~
~~~ {.output}
Doc      LICENSE  Makefile         Misc     PC       Programs  Tools         config.log     configure     
Grammar  Lib      Makefile.pre     Modules  PCbuild  Python    aclocal.m4    config.status  configure.ac  
Include  Mac      Makefile.pre.in  Objects  Parser   README    config.guess  config.sub     install-sh
~~~

The generated `Makefile` is what contains all of the compiling commands with 
correct dependences.  The `make` command, will interpret and execute the 
`Makefile`.

~~~ {.bash}
$ make
~~~

A bunch of compiling commands, will almost always see warnings; usually can be 
ignored.

### Install

~~~ {.bash}
$ make install
~~~

A bunch of `install` commands coupled with `rm` and `cp`.

~~~ {.bash}
$ cd $HOME/python3
$ ls
~~~
~~~ {.output}
bin  include  lib  share
~~~

## Test our installation

~~~ {.bash}
$ cd bin
$ ./python3
~~~

~~~ {.output}
Python 3.5.1 (default, Jun  8 2016, 11:23:55) [GCC 6.1.1 20160501] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
~~~

To quit the python interpreter type `quit()` at the prompt and press enter.
Notice that the version in the header matches the version we just installed.  
However, the problem with this install is that it is not available for use 
without an absolute path.

~~~ {.bash}
$ python3
~~~
~~~ {.output}
bash: python3: command not found
~~~


