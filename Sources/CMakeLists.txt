cmake_minimum_required(VERSION 3.16.0)

project(ConanQtPackageTest)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)

function( get_dll_location dllPathOut target)
    string(TOUPPER "${CMAKE_BUILD_TYPE}" upperConfig)
    get_property(absDllPath TARGET ${target} PROPERTY IMPORTED_LOCATION_${upperConfig})
    if(NOT absDllPath)
        get_property(absDllPath TARGET ${target} PROPERTY LOCATION_${upperConfig})
    endif()
    set(${dllPathOut} ${absDllPath} PARENT_SCOPE)
endfunction()

conan_basic_setup(TARGETS)
#conan_basic_setup()
message(STATUS "Looking for Qt cmake files at ${CONAN_LIB_DIRS_QT}/cmake/Qt5")
find_package(Qt5 CONFIG REQUIRED COMPONENTS Core Gui Widgets PATHS ${CONAN_LIB_DIRS_QT}/cmake/Qt5 )
message(STATUS "Using qt at ${Qt5_DIR}")


foreach(qtTarget Qt5::Core Qt5::Gui Qt5::Widgets)

    get_dll_location(absDllPath ${qtTarget})
    file(COPY ${absDllPath} DESTINATION ${CMAKE_BINARY_DIR}/bin)

endforeach()

if(${CMAKE_SYSTEM_NAME} STREQUAL Windows)

    get_dll_location(absDllPath Qt5::QWindowsIntegrationPlugin)
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/bin/platforms)
    file(COPY ${absDllPath} DESTINATION ${CMAKE_BINARY_DIR}/bin/platforms)

elseif(${CMAKE_SYSTEM_NAME} STREQUAL Linux)

    get_dll_location(absDllPath Qt5::QXcbIntegrationPlugin)
    file(MAKE_DIRECTORY ${CMAKE_BINARY_DIR}/bin/platforms)
    file(COPY ${absDllPath} DESTINATION ${CMAKE_BINARY_DIR}/bin/platforms)

endif()

set( sourceFiles
    test.cpp
    CMakeToolchainFiles/Clang.cmake
    CMakeToolchainFiles/Gcc.cmake
    CMakeToolchainFiles/MSVC2019.cmake
    Conanfiles/conanfile_Qt5.12.6.txt
    Conanfiles/conanfile_Qt5.12.7.txt
    Conanfiles/conanfile_Qt5.12.8.txt
    Conanfiles/conanfile_Qt5.12.9.txt
    Conanfiles/conanfile_Qt5.13.0.txt
    Conanfiles/conanfile_Qt5.13.1.txt
    Conanfiles/conanfile_Qt5.13.2.txt
    Conanfiles/conanfile_Qt5.14.0.txt
    Conanfiles/conanfile_Qt5.14.1.txt
    Conanfiles/conanfile_Qt5.14.2.txt
    Conanfiles/conanfile_Qt5.15.0.txt
    Conanfiles/conanfile_Qt5.15.1.txt
    ConanProfiles/ConanProfile-Clang-shared-debug
    ConanProfiles/ConanProfile-Clang-static-release
    ConanProfiles/ConanProfile-Gcc-shared-debug
    ConanProfiles/ConanProfile-VS2019-shared-debug
    ConanProfiles/ConanProfile-VS2019-static-release
)

# Add the test executable
add_executable(qtConsumer ${sourceFiles})
#target_link_libraries(test CONAN_PKG::qt)
target_link_libraries(qtConsumer Qt5::Widgets)

install( 
    TARGETS qtConsumer
    EXPORT ConanQtPackageTest
    RUNTIME 
        DESTINATION bin
)

enable_testing()

add_test(NAME run_test_exe COMMAND qtConsumer)

