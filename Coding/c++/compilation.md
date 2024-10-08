CmakeLists.txt 和 Makefile 的区别

CMakeLists.txt 和 Makefile 是两种不同的构建系统配置文件，他们勇于不同的构建工具。下面是他们的区别和用途

`CMakeLists.txt`

1. 用途
   1. CMakeLists.txt 是 CMake 构建系统的配置文件。CMake 是一个跨平台的构建系统生成器，可以生成不同平台的构建文件 如 MakeFile，Visual Studio 项目文件等
2. 特点
   1. 跨平台 CMake可以生成适用不同操作系统和编译器的构建文件
   2. 灵活性 CMake 提供了丰富的配置选项和宏，可以处理复杂的构建需求
   3. 可移植性 CMake 生成的构建文件可以在不同的平台上使用，减少了平台的配置工作
3. 示例

~~~cmake
cmake_minimum_required(VERSION 3.10)
project(MyProject)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

include_directories(include)

set(SOURCE_FILES
	src/main.cpp
	src/utils.cpp
)

add_executable(my_program ${SOURCE_FILES})
~~~



`Makefile`

1. 用途
   1. Makefile 是 GNU Make 构建工具的配置文件。Make是一个经典的构建工具。用于自动化编译和链接过程
2. 特点
   1. 简单直接 Makefile 语法相对简单，适合小型项目或者不需要跨平台的项目
   2. 依赖管理 Makefile 通过依赖关系自动管理编译过程，只有当源文件发生变化时才会重新编译
   3. 平台相关 Makefile 通常是平台相关的，不同平台可能需要不同的配置
3. 示例

~~~cmake
CC = g++
CFLAGS = -std=c++17 -Iinclude
LDFLAGS = 
SRC = src/main src/utils.cpp
OBJ = $(SRC:.cpp=.o)

all: my_program

my_program: $(OBJ)
	$(CC) $(LDFLAGS) -o $@ $^

%.o: $.cpp
	$(CC) $(CFLAGS) -c -o $@ $<

clean:
	rm -f $*(OBJ) my_program

~~~



区别总结

1. 构建工具
   1. CMakeLists.txt 用于 CMake 构建系统
   2. Makefile 用于GNU Make 构建工具
2. 跨平台性
   1. CMake 可以生成适用于不同平台的构建文件，具有更好的跨平台性
   2. Make 通常是平台相关的，不同平台可能需要不同的配置
3. 灵活性
   1. CMake 提供了丰富的配置选项和宏，适合处理复杂的构建需求
   2. Make 语法相对简单，适合小型项目或者不需要跨平台的项目
4. 可移植性
   1. CMake 生成的构建文件可以在不同的平台上使用，减少了平台相关的配置工作
   2. Make 生成的构建文件通常是平台相关的

**选择建议**

跨平台项目推荐使用 CMake 因为他可以生成适用于不同平台的构建文件。

小型项目或者不需要跨平台的项目：可以使用 Make，因为它语法简单，易于上手

复杂项目 推荐使用 CMake，因为它提供了丰富的配置选项和宏，适合处理复杂的构建需求

**结合使用**

在实际项目中，CMake 和 Make 可以结合使用。CMake 可以生成 Makefile 然后使用 Make 进行构建。这种方式结合了两者的优点，既可以利用 CMake 的跨平台性和灵活性，又可以利用 Make 的简单行和依赖管理





































