# This script creates the github workflow files for a matrix of qt versions and build configurations.
# This is done in order to get a build-badge for the README.md for each individual configuration.
#
#

cmake_minimum_required(VERSION 3.17)


set(qtVersions 5.12.6 #[[ 5.12.9 5.13.2 5.14.2 5.15.1 ]])
set(linuxConfigs Gcc-shared-debug #[[ Clang-shared-debug Clang-static-release ]])
set(windowsConfigs VS2019-shared-debug #[[VS2019-static-release ]])

foreach(qtVersion ${qtVersions})

    foreach(config ${linuxConfigs})

        set(configName Qt${qtVersion}-${config})
        set(conanProfile ConanProfile-${config})
        set(conanFile conanfile_Qt${qtVersion}.txt)

        set(actionsTemplateFile "${CMAKE_CURRENT_LIST_DIR}/buildActionsLinux.yml.in")
        set(actionsTargetFile "${CMAKE_CURRENT_LIST_DIR}/../.github/workflows/build-Qt${qtVersion}-${config}.yml")
        configure_file(${actionsTemplateFile} ${actionsTargetFile} @ONLY)

    endforeach()

    foreach(config ${windowsConfigs})

        set(configName Qt${qtVersion}-${config})
        set(conanProfile ConanProfile-${config})
        set(conanFile conanfile_Qt${qtVersion}.txt)

        set(actionsTemplateFile "${CMAKE_CURRENT_LIST_DIR}/buildActionsWindows.yml.in")
        set(actionsTargetFile "${CMAKE_CURRENT_LIST_DIR}/../.github/workflows/build-Qt${qtVersion}-${config}.yml")
        configure_file(${actionsTemplateFile} ${actionsTargetFile} @ONLY)

    endforeach()

endforeach()



