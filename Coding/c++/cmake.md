Make

Make 是一种构建工具，属于 GNU 项目，在 mac 上输入 make -version 可查看 make 工具的版本

Makefile

make命令执行时，需要一个makefile文件，以告诉make命令如何去编译和链接程序

比方说，如果 hello.cpp 依赖 add.cpp div.cpp sub.cpp 那么使用 make 就需要编写 makefile 文件，在源文件下添加 makefile 文件

~~~makefile
hello.out:hello.o sub.o div.o add.o
	gcc hello.o sub.o div.o add.o -o hello.out

div.o:div.cpp
	gcc -c div.cpp -o div.o

sub.o:sub.cpp
	gcc -c sub.cpp -o sub.o

add.o:add.cpp
	gcc -c add.cpp -o add.o

hello.o:hello.cpp
	gcc -c hello.cpp -o hello.o
~~~

