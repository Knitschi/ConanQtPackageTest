cmake_minimum_required(VERSION 3.16.0)
project(ConanQtPackageTest)

#SET(CMAKE_CXX_STANDARD 14)
#SET(CMAKE_CXX_STANDARD_REQUIRED ON)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

conan_basic_setup(TARGETS)
#conan_basic_setup()
find_package(Qt5 CONFIG REQUIRED COMPONENTS Core Gui Widgets PATHS ${CONAN_LIB_DIRS_QT}/cmake/Qt5 )

string(TOUPPER ${COMPILER_CONFIG} COMPILER_CONFIG)

foreach(qtTarget Qt5::Core Qt5::Gui Qt5::Widgets)
    
    get_property(absDllPath TARGET ${qtTarget} PROPERTY IMPORTED_LOCATION_${COMPILER_CONFIG})
    file(COPY ${absDllPath} DESTINATION ${CMAKE_BINARY_DIR}/bin)

endforeach()

if(${CMAKE_SYSTEM_NAME} STREQUAL Windows)

    get_property(absDllPath TARGET Qt5::QWindowsIntegrationPlugin PROPERTY IMPORTED_LOCATION_${COMPILER_CONFIG})
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/bin/platforms)
    file(COPY ${absDllPath} DESTINATION ${CMAKE_BINARY_DIR}/bin/platforms)

elseif(${CMAKE_SYSTEM_NAME} STREQUAL Linux)

endif()

# Add the test executable
add_executable(test test.cpp "${CMAKE_BINARY_DIR}/conanbuildinfo.cmake" "${CMAKE_BINARY_DIR}/conanbuildinfo.txt" "${CMAKE_BINARY_DIR}/conaninfo.txt" )
#target_link_libraries(test CONAN_PKG::qt)
target_link_libraries(test Qt5::Widgets)
