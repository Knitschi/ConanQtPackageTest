# ConanQtPackageTest
This project is used for testing the Qt package that is provided by the conan package manager.

before building this you need to manually download and install Conan, CMake and the required build tools.


# Tests

All test cases contain commands for getting the qt package. Building the test project and running the built
executable.


# Working Qt package configurations

| Conanfile | VS2019-shared-debug | VS2019-static-release | Clang-shared-debug | Clang-static-release | Gcc-shared-debug |
| :--- |:---:| :---:|:---:|:---:|:---:|
| conanfile_Qt5.12.6.txt | X | X |  |  |  |
| conanfile_Qt5.12.7.txt | - | X |  |  |  |
| conanfile_Qt5.12.8.txt | X | - |  |  |  |
| conanfile_Qt5.12.9.txt | - | - |  |  |  |
| conanfile_Qt5.13.0.txt | X | X |  |  |  |
| conanfile_Qt5.13.1.txt | - | - |  |  |  |
| conanfile_Qt5.13.2.txt | X | X |  |  |  |
| conanfile_Qt5.14.0.txt | X | X |  |  |  |
| conanfile_Qt5.14.1.txt | X | X |  |  |  |
| conanfile_Qt5.15.0.txt | - | - |  |  |  |
| conanfile_Qt5.15.1.txt | - | - |  |  |  |

### Legend
**-**: Qt Package has build errors.  
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


