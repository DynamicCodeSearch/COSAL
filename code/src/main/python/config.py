import sys
import os

sys.path.append(os.path.abspath("."))
sys.dont_write_bytecode = True

__author__ = "COSAL"


class BaseConfig:
    HOME = os.getenv("HOME")
    ROOT_HOME = os.path.join(HOME, "Raise", "ProgramRepair")
    CODESEER_HOME = os.path.join(ROOT_HOME, "CodeSeer")
    CODE_HOME = os.path.join(CODESEER_HOME, "code")

    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_project_name(self):
        raise NotImplementedError("Must be implemented in subclasses")

    def get_dataset(self):
        raise NotImplementedError("Must be implemented in subclasses")

    def get_projects_home(self):
        raise NotImplementedError("Must be implemented in subclasses")

    def get_python_projects_home(self):
        raise NotImplementedError("Must be implemented in subclasses")

    def get_java_projects_home(self):
        raise NotImplementedError("Must be implemented in subclasses")

    def get_default_values(self):
        return None


class ApacheConfig(BaseConfig):
    def get_project_name(self):
        return "commons-lang"

    def get_dataset(self):
        return "OpenSource"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "subjects", "commons-lang")

    def get_python_projects_home(self):
        return None


class CodeJamConfig(BaseConfig):
    def get_project_name(self):
        return "CodeJam"

    def get_dataset(self):
        return "CodeJam"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "projects")

    def get_python_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "python", "CodeJam")


class DummyConfig(BaseConfig):
    def get_project_name(self):
        return "Dummy"

    def get_dataset(self):
        return "Dummy"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "projects")

    def get_python_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "python", "stupid")

    # def get_default_values(self):
    #     return ["Hello", [1,2,3]]


class GuavaConfig(BaseConfig):
    def get_project_name(self):
        return "guava"

    def get_dataset(self):
        return "OpenSource"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "subjects", "guava")

    def get_python_projects_home(self):
        return None


class IntroClassConfig(BaseConfig):
    def get_project_name(self):
        return "IntroClassJava"

    def get_dataset(self):
        return "IntroClassJava"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "projects")

    def get_python_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "python", "IntroClassJava")


class SystemLibConfig(BaseConfig):
    def get_project_name(self):
        return "SystemLibs"

    def get_dataset(self):
        return "OpenSource"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "projects")

    def get_python_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "python", "SystemLibs")


class StandaloneEngineConfig(BaseConfig):
    def get_project_name(self):
        return "Standalone"

    def get_dataset(self):
        return "Standalone"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "projects")

    def get_python_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "python", "Standalone")

    def get_default_values(self):
        return ["Hello", [1,2,3]]


class AtCoderConfig(BaseConfig):
    def get_project_name(self):
        return "AtCoder"

    def get_dataset(self):
        return "AtCoder"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "subjects", "atcoder")

    def get_python_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "python")

    def get_java_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "java")


class AtCoderMethodConfig(BaseConfig):
    def get_project_name(self):
        return "AtCoder"

    def get_dataset(self):
        return "AtCoderMethods"

    def get_projects_home(self):
        return os.path.join(BaseConfig.CODESEER_HOME, "subjects", "atcoder")

    def get_python_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "python")

    def get_java_projects_home(self):
        return os.path.join(self.get_projects_home(), "src", "main", "java")


class BigCloneBenchConfig(BaseConfig):
    def get_project_name(self):
        return "BigCloneBench"

    def get_dataset(self):
        return "BigCloneBench"

    def get_projects_home(self):
        return os.path.join(BaseConfig.ROOT_HOME, "BigCloneEval", "ijadataset", "bcb_reduced")

    def get_python_projects_home(self):
        # raise RuntimeError("BigCloneBench only supports Java!!!")
        return None

    def get_java_projects_home(self):
        return self.get_projects_home()


if __name__ == "__main__":
    print(DummyConfig.ROOT_HOME)
