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




