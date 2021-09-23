"""
异常类
"""

class YamlException(Exception):
    """Custom exception for error reporting."""

    def __init__(self, basename, value) -> None:
        self.basename = basename
        self.value = value

    def __str__(self) -> str:
        return repr("".join(("testcase execution failed", 
            "spec failed: {} non testcase detail.".format(self.value),
            "please check `{}.yaml`".format(self.basename))))
