include(cpfAddFilePackage)

cpfInitPackageProject()

set(qtVersions
    5.12.6
    5.12.7
    5.12.8
    5.12.9
    5.13.0
    5.13.1
    5.13.2
    5.14.0
    5.14.1
    5.15.0
    5.15.1
)

set(conanfiles)
foreach(version ${qtVersions})
    cpfListAppend(conanfiles conanfile_Qt${version}.txt)
endforeach()

set( sources
    TestProject/CMakeLists.txt
    TestProject/test.cpp
)

cpfAddFilePackage(
	SOURCES ${sources} ${conanfiles}
)

set(index 0)
foreach(conanfile ${conanfiles})
 
    add_test(
        NAME InstallDependencyTest${index}
        COMMAND conan install -pr Sources/CIBuildConfigurations/ConanProfile-${CPF_CONFIG} -if Generated/${CPF_CONFIG} ${CMAKE_CURRENT_SOURCE_DIR}/${conanfile} --build=missing
        WORKING_DIRECTORY ${CPF_ROOT_DIR}
    )

    cpfIncrement(index)

endforeach()


