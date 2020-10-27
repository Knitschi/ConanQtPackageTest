from conans import ConanFile, CMake, tools

class ConanQtPackageTests(ConanFile):
    name = "ConanQtPackageTest"
    version = "1.0"
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

# GUI: [True, False]
# commercial: [True, False]
# opengl: ['no', 'es2', 'desktop', 'dynamic']
# openssl: [True, False]
# qt3d: [True, False]
# qtactiveqt: [True, False]
# qtandroidextras: [True, False]
# qtbase: [True, False]
# qtcanvas3d: [True, False]
# qtcharts: [True, False]
# qtconnectivity: [True, False]
# qtdatavis3d: [True, False]
# qtdeclarative: [True, False]
# qtdoc: [True, False]
# qtgamepad: [True, False]
# qtgraphicaleffects: [True, False]
# qtimageformats: [True, False]
# qtlocation: [True, False]
# qtmacextras: [True, False]
# qtmultimedia: [True, False]
# qtnetworkauth: [True, False]
# qtpurchasing: [True, False]
# qtqa: [True, False]
# qtquickcontrols: [True, False]
# qtquickcontrols2: [True, False]
# qtremoteobjects: [True, False]
# qtrepotools: [True, False]
# qtscript: [True, False]
# qtscxml: [True, False]
# qtsensors: [True, False]
# qtserialbus: [True, False]
# qtserialport: [True, False]
# qtspeech: [True, False]
# qtsvg: [True, False]
# qttools: [True, False]
# qttranslations: [True, False]
# qtvirtualkeyboard: [True, False]
# qtwayland: [True, False]
# qtwebchannel: [True, False]
# qtwebengine: [True, False]
# qtwebglplugin: [True, False]
# qtwebsockets: [True, False]
# qtwebview: [True, False]
# qtwinextras: [True, False]
# qtx11extras: [True, False]
# qtxmlpatterns: [True, False]
# shared: [True, False]
# widgets: [True, False]
# with_doubleconversion: [True, False]
# with_freetype: [True, False]
# with_harfbuzz: [True, False]
# with_libjpeg: [True, False]
# with_libpng: [True, False]
# with_odbc: [True, False]
# with_pcre2: [True, False]
# with_pq: [True, False]
# with_sqlite3: [True, False]


    def source(self):
        self.run("git clone https://github.com/Knitschi/ConanQtPackageTest.git")

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure()
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()
        cmake.test()

    def package(self):
        cmake = self.configure_cmake()
        cmake.install()
