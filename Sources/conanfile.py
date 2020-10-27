from conans import ConanFile, CMake, tools

class ConanQtPackageTests(ConanFile):
    name = "ConanQtPackageTest"
    version = "1.0.0"
    license = "MIT License"
    url = "https://github.com/Knitschi/ConanQtPackageTest"
    description = "This project is used for testing the Qt package that is provided by the conan package manager."
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False],
                 "qtVersion": ["5.12.6", "5.12.9", "5.13.2", "5.14.2", "5.15.1"], }

    default_options = {"shared": False, "qtVersion": "5.15.1"}
    generators = "cmake"

    def requirements(self):

        qtPackage = "qt/{0}@bincrafters/stable".format(self.options.qtVersion)
        self.output.info(qtPackage)
        self.requires(qtPackage)

    def configure(self):
        self.options["openssl"].no_asm = True
        self.options["qt"].shared = True
        self.options["qt"].with_mysql = False
        self.options["qt"].with_sqlite3 = False
        self.options["qt"].with_pq = False
        self.options["qt"].with_odbc = False
        self.options["qt"].with_harfbuzz = False
        self.options["qt"].openssl = False
        self.options["qt"].with_libjpeg = False

    def source(self):
        self.run("git clone https://github.com/Knitschi/ConanQtPackageTest.git")

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="{0}/Sources".format(self.name), build_folder="build")
        cmake.definitions["CONAN_BUILD_INFO_DIR"] = ".."
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def imports(self):
        self.copy("*.dll", dst="bin", src="bin")

    def test(self):
        os.chdir("bin")
        self.run(".%test" % os.sep)

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
