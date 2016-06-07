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


[Python Download Page](https://www.python.org/downloads/release/python-2711)


~~~ {.bash}
$ tar xzvf Python-2.7.11.tgz
~~~


~~~ {.bash}
$ cd Python-2.7.11
$ ls
~~~

There will be a number of directories and files.  The main file we are 
interested in is the `configure` script.  This will setup the compile time 
dependencies.  The script can take numerous options.

~~~ {.bash}
$ ./configure --help
~~~

~~~ {.output}
By default, `make install' will install all the files in
`/usr/local/bin', `/usr/local/lib' etc.  You can specify
an installation prefix other than `/usr/local' using `--prefix',
for instance `--prefix=$HOME'.
~~~

So let's configure the build to install in our a subdirectory `python2` in our 
home directory.

~~~ {.bash}
$ ./configure --prefix=$HOME/python2
~~~

Notice the directory now has a `Makefile` in it

~~~ {.bash}
$ make
~~~

A bunch of compiling commands, will almost always see warnings; usually can be 
ignored.

~~~ {.bash}
$ make install
~~~

A bunch of `install` commands coupled with `rm` and `cp`.

~~~ {.bash}
$ cd $HOME/python2
$ ls
~~~



