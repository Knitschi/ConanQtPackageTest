cmake_minimum_required(VERSION 3.14.0)
project(ConanQtTest)

SET(CMAKE_CXX_STANDARD 14)
SET(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(TARGETS)
#conan_basic_setup()
find_package(Qt5 CONFIG REQUIRED COMPONENTS Core Gui Widgets PATHS ${CONAN_LIB_DIRS_QT}/cmake )


add_executable(test test.cpp)
#target_link_libraries(test Qt5::Core Qt5::Gui Qt5::Widgets)
#target_link_libraries(test CONAN_PKG::qt)
target_link_libraries(test Qt5::Widgets)
