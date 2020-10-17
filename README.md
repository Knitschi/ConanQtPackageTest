# ConanQtPackageTest
This project is used for testing the Qt package that is provided by the conan package manager.

before building this you need to manually download and install Conan, CMake and the required build tools.


# Tests

All test cases contain commands for getting the qt package. Building the test project and running the built
executable.


# Working Qt package configurations

| Conanfile | VS2019-shared-debug | VS2019-static-release | Clang-shared-debug | Clang-static-release | Gcc-shared-debug |
| :--- |:---:| :---:|:---:|:---:|:---:|
| conanfile_Qt5.12.6.txt | X | X | 4 |  | - |
| conanfile_Qt5.12.7.txt | - | X |  |  | 1 |
| conanfile_Qt5.12.8.txt | X | - |  |  |  |
| conanfile_Qt5.12.9.txt | - | - |  |  |  |
| conanfile_Qt5.13.0.txt | X | X | 0 |  |  |
| conanfile_Qt5.13.1.txt | - | - |  |  |  |
| conanfile_Qt5.13.2.txt | X | X | 2 |  |  |
| conanfile_Qt5.14.0.txt | X | X |  |  |  |
| conanfile_Qt5.14.1.txt | X | X | 2 |  | X |
| conanfile_Qt5.15.0.txt | 6 | 6 | X | X | X |
| conanfile_Qt5.15.1.txt | - | - | X |  | 5 |

### Legend
**<number>**: Qt Package could not be build. A short description of the error can be found in the *Encountered Build Errors* section below.  
**X**: Qt Package can be build.  

# Conan Versions

  * Windows: 1.26.0
  * Ubuntu: 1.29.2

# How to run the tests?

This project relies on the CMakeProjectFramework to provide some helper build-scripts.  
For further information see [Working with a CPF project](https://knitschi.github.io/CMakeProjectFramework/LastBuild/doc/sphinx/html/documentation/WorkingWithACPFProject.html)

## Linux

```bash
git clone --recursive https://github.com/Knitschi/ConanQtPackageTest.git
cd ConanQtPackageTest
python3 Sources/CPFBuildScripts/0_CopyScripts.py
python3 1_Configure.py Gcc-shared-debug
python3 3_Generate.py
python3 4_Make.py --target runAllTests_QtTestConsumer
```

## Windows

```batch
git clone --recursive https://github.com/Knitschi/ConanQtPackageTest.git
cd ConanQtPackageTest
python Sources/CPFBuildScripts/0_CopyScripts.py
python 1_Configure.py VS2019-shared-debug
python 3_Generate.py
python 4_Make.py --target runAllTests_QtTestConsumer
```

# Encountered Build Errors

### 1 Somewhere in platform plugins

Not sure what really caused the first error. Error occurred sometime when compiling platform plugins.

```
make[10]: *** [Makefile.xcb_qpa_lib:5240: .obj/qxcbkeyboard.o] Error 1

```

### 2 Somewhere in xcb-util-wm

```
checking for m4 that supports -I option... configure: error: could not find m4 that supports -I option

```

### 3 Version Conflict for bzip2

```
ERROR: Conflict in pcre/8.41:
    'pcre/8.41' requires 'bzip2/1.0.8' while 'pcre2/10.32@bincrafters/stable' requires 'bzip2/1.0.8@conan/stable'.
```

### 4 Missing module _lzma in package xkbcommon

```
xkbcommon/0.8.4@bincrafters/stable: Calling build()
Traceback (most recent call last):
  File "/home/knitschi/.conan/data/meson/0.52.0/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/bin/meson.py", line 26, in <module>
    from mesonbuild import mesonmain
  File "/home/knitschi/.conan/data/meson/0.52.0/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/bin/mesonbuild/mesonmain.py", line 25, in <module>
    from . import mconf, mdist, minit, minstall, mintro, msetup, mtest, rewriter, msubprojects, munstable_coredata
  File "/home/knitschi/.conan/data/meson/0.52.0/_/_/package/5ab84d6acfe1f23c4fae0ab88f26e3a396351ac9/bin/mesonbuild/mdist.py", line 16, in <module>
    import lzma
  File "/usr/local/lib/python3.6/lzma.py", line 27, in <module>
    from _lzma import *
ModuleNotFoundError: No module named '_lzma'
```

### 5 Somewhere in qxkbcommon

```
make[9]: *** [Makefile:789: .obj/qxkbcommon.o] Error 1
make[9]: Leaving directory '/home/knitschi/.conan/data/qt/5.15.1/bincrafters/stable/build/0cf2aaff5c853a207513d9a75f673c2b67fca823/qtbase/src/platformsupport/input/xkbcommon'
make[8]: *** [Makefile:48: sub-xkbcommon-make_first-ordered] Error 2
make[8]: Leaving directory '/home/knitschi/.conan/data/qt/5.15.1/bincrafters/stable/build/0cf2aaff5c853a207513d9a75f673c2b67fca823/qtbase/src/platformsupport/input'
make[7]: *** [Makefile:209: sub-input-make_first] Error 2
```

### 6 '_CppInfo' object does not support item assignment

```
CUSTOMBUILD : error : opengl/system: Error in package_info() method, line 67 [C:\dev\ConanQtPackageTest\Generated\VS2019-shared-debug\QtTestConsumer\runTest_Qt5.15.0TestConsumer.vcxproj]
        self.cpp_info.filenames["cmake_find_package"] = "opengl_system"
        TypeError: '_CppInfo' object does not support item assignment
```