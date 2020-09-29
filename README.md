# ConanQtPackageTest
This project is used for testing the Qt package that is provided by the conan package manager.

before building this you need to manually download and install Conan, CMake and the required build tools.


# Tests

All test cases contain commands for getting the qt package. Building the test project and running the built
executable.

## Test Case Windows and Visual Studio 2019

* Visual Studio 16.6.0
* Conan 1.25.2
* python 3.6.6
* CMake 3.16.5

```
>conan install -pr VS2019-profile -if VS2019 . --build=missing conanfile_1.txt
>cmake -H. -BVS2019 -G"Visual Studio 16 2019"
>cmake --build VS2019
>VS2019\bin\test.exe
```
-> Works!
