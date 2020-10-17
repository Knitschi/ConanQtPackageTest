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

set(runTestTargets)
set(index 0)
foreach(conanfile ${conanfiles})
 
    list(GET qtVersions ${index} qtVersion)

    set(absConanFile "${CMAKE_CURRENT_SOURCE_DIR}/${conanfile}")
    set(stampFile ${CMAKE_CURRENT_BINARY_DIR}/run_qt${qtVersion}Test.stamp)

    set(testProjectBuildDir "${CMAKE_CURRENT_BINARY_DIR}/TestProject/run_qt${qtVersion}Test")

    add_custom_command(
        DEPENDS ${sources} ${conanfile}
        # Build the conan qt package 
        COMMAND conan install -pr Sources/CIBuildConfigurations/ConanProfile-${CPF_CONFIG} -if ${testProjectBuildDir} ${absConanFile} --build=missing 
        # Run CMake Generate for the consumer package
        COMMAND "${CMAKE_COMMAND}" -S "${CMAKE_CURRENT_SOURCE_DIR}/TestProject" -B ${testProjectBuildDir} -DCMAKE_TOOLCHAIN_FILE=${CMAKE_TOOLCHAIN_FILE} -DCOMPILER_CONFIG=${CMAKE_CONFIGURATION_TYPES} -G "${CMAKE_GENERATOR}"
        # Build the consumer package.
        COMMAND "${CMAKE_COMMAND}" --build ${testProjectBuildDir}
        # Run the consumer package executable.
        COMMAND ${testProjectBuildDir}/bin/test.exe 
        # Create a stamp file.
        COMMAND "${CMAKE_COMMAND}" -E touch ${stampFile}
        OUTPUT ${stampFile}
        WORKING_DIRECTORY ${CPF_ROOT_DIR}
    )

    set(targetName runTest_Qt${qtVersion}TestConsumer)
    add_custom_target(
        ${targetName}
        DEPENDS ${stampFile} 
    )
    set_property(TARGET ${targetName} PROPERTY FOLDER ${PROJECT_NAME})
    cpfListAppend(runTestTargets ${targetName})

    cpfIncrement(index)

    message(STATUS "Add package test target ${targetName}.")
    
endforeach()

set(bundleTargetName runAllTests_${PROJECT_NAME})
cpfAddBundleTarget(${bundleTargetName} "${runTestTargets}")
set_property(TARGET ${bundleTargetName} PROPERTY FOLDER ${PROJECT_NAME})
set_property(TARGET ${PROJECT_NAME} PROPERTY INTERFACE_CPF_RUN_TESTS_SUBTARGET ${bundleTargetName})

