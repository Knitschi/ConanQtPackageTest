cmake_minimum_required(VERSION 3.16.0)
project(ConanQtPackageTest)

SET(CMAKE_CXX_STANDARD 14)
SET(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(TARGETS)
#conan_basic_setup()
find_package(Qt5 CONFIG REQUIRED COMPONENTS Core Gui Widgets PATHS ${CONAN_LIB_DIRS_QT}/cmake )

# Copy conan provided dlls into the build tree.
file(COPY ${CONAN_BIN_DIRS_QT}/Qt5Core.dll DESTINATION ${CMAKE_BINARY_DIR}/bin)
file(COPY ${CONAN_BIN_DIRS_QT}/Qt5Gui.dll DESTINATION ${CMAKE_BINARY_DIR}/bin)
file(COPY ${CONAN_BIN_DIRS_QT}/Qt5Widgets.dll DESTINATION ${CMAKE_BINARY_DIR}/bin)

if(${CMAKE_SYSTEM} STREQUAL Windows)

    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/bin/platforms)
    file(COPY ${CONAN_BIN_DIRS_QT}/../plugins/platforms/qwindows.dll DESTINATION ${CMAKE_BINARY_DIR}/bin/platforms)

    elseif(${CMAKE_SYSTEM} STREQUAL Linux)

endif()

# Add the test executable
add_executable(test test.cpp)
#target_link_libraries(test CONAN_PKG::qt)
target_link_libraries(test Qt5::Widgets)
