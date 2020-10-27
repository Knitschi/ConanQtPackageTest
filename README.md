

# ConanQtPackageTest
This project is used for testing the Qt package that is provided by the conan package manager.

before building this you need to manually download and install Conan, CMake and the required build tools.

# How to build and run the test project?

Before building the project you will have to install the conan package manager.

Then you can run the following commands:

```
git clone --recursive https://github.com/Knitschi/ConanQtPackageTest.git
cd ConanQtPackageTest
conan remote add bincrafters https://api.bintray.com/conan/bincrafters/public-conan 
conan install Sources --profile "Sources/ConanProfiles/VS2019-shared-debug" --install-folder build --build=missing --options qtVersion=5.15.1
conan build Sources --build-folder build
```

Depending on the system you run the test you may need to change the profile file to one of the Linux profiles.

# Tests

All test cases contain commands for getting the qt package. Building the test project and running the built
executable. The conanfiles can be found under Sources/Conanfiles.

## Build results

The github actions of this project build the test consumer with various versions of Qt and various compilers and build-options.
The configurations can be found in the conan profile files in the Sources/ConanProfiles directory.

| Qt Version | VS2019-shared-debug | VS2019-static-release | Clang-shared-debug | Clang-static-release | Gcc-shared-debug |
| :--- |:---:| :---:|:---:|:---:|:---:|
| 5.12.6 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.6-Gcc-shared-debug) |
| 5.12.9 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.12.9-Gcc-shared-debug) |
| 5.13.2 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.13.2-Gcc-shared-debug) |
| 5.14.2 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.14.2-Gcc-shared-debug) |
| 5.15.1 | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-VS2019-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-VS2019-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-Clang-shared-debug) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-Clang-static-release) | ![GitHub Workflow Status](https://img.shields.io/github/workflow/status/knitschi/ConanQtPackageTest/Qt5.15.1-Gcc-shared-debug) |



