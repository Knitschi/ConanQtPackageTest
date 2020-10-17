include("CPFCMake/cpfInitCIProject.cmake")
cmake_minimum_required(VERSION ${CPF_MINIMUM_CMAKE_VERSION}) 

project(ConanQtPackageTest)

cpfAddPackages(GLOBAL_FILES "../README.md" "../LICENSE" "WorkingConfigs.md" ) 