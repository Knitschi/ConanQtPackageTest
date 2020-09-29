# ConanQtPackageTest
This project is used for testing the Qt package that is provided by the conan package manager.

before building this you need to manually download and install Conan, CMake and the required build tools.


# Tests

All test cases contain commands for getting the qt package. Building the test project and running the built
executable.

## Test Case Windows 10 and Visual Studio 2019

* Visual Studio 16.6.0
* Conan 1.25.2
* python 3.6.6
* CMake 3.16.5

```
>conan install -pr VS2019-profile -if VS2019 . --build=missing conanfile_1.txt
>cmake -H. -BVS2019 -G"Visual Studio 16 2019"
>cmake --build VS2019
>VS2019\bin\test.exe
```

### Result
-> Works!

## Test Case Ubuntu 20.04 and Gcc 9

* Gcc 9.3
* make 4.2.1
* Conan 1.25.2
* python 3.8.2
* CMake 3.16.3

```
$conan install -pr LinuxGcc9-profile -if LinuxGcc9 . --build=missing
$cmake -H. -BLinuxGcc9 -G"Unix Makefiles"
$cmake --build LinuxGcc9
$LinuxGcc9\bin\test.exe
```

### Result
-> Fails in conan step!

Some of the errors:

After Qt configure
```
...
t Sql Drivers:
  DB2 (IBM) .............................. no
  InterBase .............................. no
  MySql .................................. no
  OCI (Oracle) ........................... no
  ODBC ................................... yes
  PostgreSQL ............................. yes
  SQLite2 ................................ no
  SQLite ................................. yes
    Using system provided SQLite ......... yes
  TDS (Sybase) ........................... no
Qt Testlib:
  Tester for item models ................. yes

Note: Disabling X11 Accessibility Bridge: D-Bus or AT-SPI is missing.

ERROR: Feature 'openssl-linked' was enabled, but the pre-condition '!features.securetransport && libs.openssl' failed.

ERROR: Feature 'system-harfbuzz' was enabled, but the pre-condition 'features.harfbuzz && libs.harfbuzz' failed.

ERROR: Feature 'sql-mysql' was enabled, but the pre-condition 'libs.mysql' failed.
...
```

Linker errors like this
```
> g++ -c -pipe -O2 -w -fPIC -DPCRE2_STATIC -DU_STATIC_IMPLEMENTATION -DLIBJPEG_STATIC -I. -I/home/knitschi/.conan/data/zlib/1.2.11/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/include -I/home/knitschi/.conan/data/openssl/1.1.1d/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/include -I/home/knitschi/.conan/data/pcre2/10.33/_/_/package/18903774d26ee0498535ef95198a1c997e4ca9ba/include -I/home/knitschi/.conan/data/glib/2.58.3/bincrafters/stable/package/7f983ae1408fa0002112c9e9ae66401d3cfe699c/include -I/home/knitschi/.conan/data/glib/2.58.3/bincrafters/stable/package/7f983ae1408fa0002112c9e9ae66401d3cfe699c/include/glib-2.0 -I/home/knitschi/.conan/data/glib/2.58.3/bincrafters/stable/package/7f983ae1408fa0002112c9e9ae66401d3cfe699c/lib/glib-2.0/include -I/home/knitschi/.conan/data/double-conversion/3.1.5/_/_/package/b911f48570f9bb2902d9e83b2b9ebf9d376c8c56/include -I/home/knitschi/.conan/data/fontconfig/2.13.91/conan/stable/package/ae28ad6d942ab1a800215a9be1f3c0f4410674e2/include -I/home/knitschi/.conan/data/icu/64.2/_/_/package/1524904dd725e06dec6d8b171834126a56e52d5a/include -I/home/knitschi/.conan/data/harfbuzz/2.6.2/bincrafters/stable/package/a251f636bfa3fe088f33f369abc54d65544b7ff2/include -I/home/knitschi/.conan/data/harfbuzz/2.6.2/bincrafters/stable/package/a251f636bfa3fe088f33f369abc54d65544b7ff2/include/harfbuzz -I/home/knitschi/.conan/data/libjpeg/9c/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/include -I/home/knitschi/.conan/data/libpng/1.6.37/_/_/package/f99afdbf2a1cc98ba2029817b35103455b6a9b77/include -I/home/knitschi/.conan/data/sqlite3/3.29.0/_/_/package/0ea13fbeff7afbe2f19b5c349acf59a585a00e93/include -I/home/knitschi/.conan/data/libmysqlclient/8.0.17/_/_/package/c9ac4e003064ca86d0557b636be39c099c45807d/include -I/home/knitschi/.conan/data/libpq/11.5/_/_/package/8e0939db49a1d312829524beb4d0b6824e47691d/include -I/home/knitschi/.conan/data/odbc/2.3.7/_/_/package/b29d3eb003873b92a248c0df6debab47f53853ea/include -I/home/knitschi/.conan/data/qt/5.12.6/bincrafters/stable/source/qt5/qtbase/mkspecs/linux-g++ -o main.o main.cpp
> g++ -Wl,-O1 -fuse-ld=gold -o libdl main.o   -L/home/knitschi/.conan/data/zlib/1.2.11/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib -L/home/knitschi/.conan/data/openssl/1.1.1d/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib -L/home/knitschi/.conan/data/pcre2/10.33/_/_/package/18903774d26ee0498535ef95198a1c997e4ca9ba/lib -L/home/knitschi/.conan/data/bzip2/1.0.8/_/_/package/da606cf731e334010b0bf6e85a2a6f891b9f36b0/lib -L/home/knitschi/.conan/data/glib/2.58.3/bincrafters/stable/package/7f983ae1408fa0002112c9e9ae66401d3cfe699c/lib -L/home/knitschi/.conan/data/libffi/3.2.1/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib -L/home/knitschi/.conan/data/pcre/8.41/_/_/package/0720f5087c8ede691acc72d5629516e165544eb7/lib -L/home/knitschi/.conan/data/libelf/0.8.13/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib -L/home/knitschi/.conan/data/libmount/2.33.1/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib -L/home/knitschi/.conan/data/libselinux/2.9/bincrafters/stable/package/6b0384e3aaa343ede5d2bd125e37a0198206de42/lib -L/home/knitschi/.conan/data/double-conversion/3.1.5/_/_/package/b911f48570f9bb2902d9e83b2b9ebf9d376c8c56/lib -L/home/knitschi/.conan/data/freetype/2.10.0/_/_/package/387eb5152986b9b3cbc2ebb94607d96d90674d67/lib -L/home/knitschi/.conan/data/libpng/1.6.37/_/_/package/f99afdbf2a1cc98ba2029817b35103455b6a9b77/lib -L/home/knitschi/.conan/data/fontconfig/2.13.91/conan/stable/package/ae28ad6d942ab1a800215a9be1f3c0f4410674e2/lib -L/home/knitschi/.conan/data/expat/2.2.9/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib -L/home/knitschi/.conan/data/libuuid/1.0.3/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib -L/home/knitschi/.conan/data/icu/64.2/_/_/package/1524904dd725e06dec6d8b171834126a56e52d5a/lib -L/home/knitschi/.conan/data/harfbuzz/2.6.2/bincrafters/stable/package/a251f636bfa3fe088f33f369abc54d65544b7ff2/lib -L/home/knitschi/.conan/data/libjpeg/9c/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib -L/home/knitschi/.conan/data/sqlite3/3.29.0/_/_/package/0ea13fbeff7afbe2f19b5c349acf59a585a00e93/lib -L/home/knitschi/.conan/data/libmysqlclient/8.0.17/_/_/package/c9ac4e003064ca86d0557b636be39c099c45807d/lib -L/home/knitschi/.conan/data/libpq/11.5/_/_/package/8e0939db49a1d312829524beb4d0b6824e47691d/lib -L/home/knitschi/.conan/data/odbc/2.3.7/_/_/package/b29d3eb003873b92a248c0df6debab47f53853ea/lib -L/home/knitschi/.conan/data/libiconv/1.16/_/_/package/6af9cc7cb931c5ad942174fd7838eb655717c709/lib   
> main.o:main.cpp:function main: error: undefined reference to 'dlopen'
> main.o:main.cpp:function main: error: undefined reference to 'dlclose'
> main.o:main.cpp:function main: error: undefined reference to 'dlsym'
> main.o:main.cpp:function main: error: undefined reference to 'dlerror'
> collect2: error: ld returned 1 exit status
> make: *** [Makefile:67: libdl] Error 1
 => source failed verification.
```

### Remarks

The package builds when using the following options in the conanfile.

```
qt:with_mysql=False
qt:with_harfbuzz=False
qt:openssl=False
```



