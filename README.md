

# ConanQtPackageTest
This project is used for testing the Qt package that is provided by the conan package manager.

before building this you need to manually download and install Conan, CMake and the required build tools.

# Tests

All test cases contain commands for getting the qt package. Building the test project and running the built
executable. The conanfiles can be found under Sources/Conanfiles.

# Working Qt package configurations

| Qt Version | VS2019-shared-debug | VS2019-static-release | Clang-shared-debug | Clang-static-release | Gcc-shared-debug |
| :--- |:---:| :---:|:---:|:---:|:---:|
| 5.12.6 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-Gcc-shared-debug) |
| 5.12.9 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-Gcc-shared-debug) |
| 5.13.2 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-Gcc-shared-debug) |
| 5.14.1 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-Gcc-shared-debug) |
| 5.15.1 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-Gcc-shared-debug) |

# Conan Versions

  * Windows: 1.30.2
  * Ubuntu: 1.29.2

# How to build and run the test project?

Before building the project you will have to install the conan package manager.

Then you can run the following commands:

```
git clone --recursive https://github.com/Knitschi/ConanQtPackageTest.git
cd ConanQtPackageTest
conan install -pr "Sources/ConanProfiles/ConanProfile-VS2019-shared-debug" -if "build" "Sources/Conanfiles/conanfile_Qt5.12.6.txt" --build=missing
```
Currently this only builds the qt package without testing its consumption.

TODO: implement conan build-interface to build and run the test consumer project.

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
