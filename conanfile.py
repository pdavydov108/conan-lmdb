from conans import ConanFile, tools, AutoToolsBuildEnvironment


class LmdbConan(ConanFile):
    name = "lmdb"
    version = "0.9.23"
    license = "OpenLDAP public license"
    author = "Pavel Davydov pdavydov108@gmail.com"
    url = "https://github.com/LMDB/lmdb"
    description = "Conan package for LDAP's lmdb database."
    settings = "os", "compiler", "arch"
    generators = "make"

    @property
    def source_dir(self):
        return '{}-LMDB_{}/libraries/liblmdb'.format(self.name, self.version)


    def source(self):
        package_url = '{}/archive/LMDB_{}.tar.gz'.format(self.url, self.version)
        tools.get(package_url)

    def build(self):
        with tools.chdir(self.source_dir):
            env_build = AutoToolsBuildEnvironment(self)
            env_build.make()

    def package(self):
        self.copy("*.h", dst="include", src=self.source_dir)
        self.copy("*.a", dst="lib", src=self.source_dir, keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["lmdb"]

