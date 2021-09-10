#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import subprocess
from script.addpth import main as addpth

if 'darwin' in sys.platform:
    WIN = False
else:
    WIN = True


def main(shell=True):
    """主函数"""
    addpth()
    if WIN:
        subprocess.run("venv\Scripts\activate.bat", shell=True)
    else:
        subprocess.run("source venv/bin/activate", shell=shell)
    subprocess.run(
        "pytest --html=report.html --self-contained-html --alluredir allure-results --clean-alluredir", shell=True)
    if WIN:
        subprocess.run(
            "call COPY config\environment.properties allure-results", shell=True)
    else:
        subprocess.run(
            "cp config/environment.properties allure-results", shell=True)
    subprocess.run(
        "allure generate allure-results -c -o allure-report", shell=True)
    subprocess.run("allure open allure-report", shell=True)


if __name__ == "__main__":
    main()
