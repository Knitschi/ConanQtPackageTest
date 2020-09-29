include(cpfAddFilePackage)

cpfInitPackageProject()

set( sources
    conanfile_1.txt
    conanfile_2.txt
    TestProject/CMakeLists.txt
    test.cpp
)

cpfAddFilePackage(
	SOURCES "${files}"
)



