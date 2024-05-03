from pathlib import Path
from subprocess import run, PIPE
import os


class Process:
    def __init__(self, process_path_or_name: str):
        self.__process_path_or_name = process_path_or_name

    def kill_by_path(self):
        cmd = "WMIC Process Where "
        cmd += f""""ExecutablePath='{self.__process_path_or_name}'" Call Terminate"""
        tmp_file = Path("tmp.bat")
        with tmp_file.open("w", encoding="utf-8") as f:
            f.write(cmd)
        run(cmd, stdout=PIPE, stderr=PIPE)
        os.remove(tmp_file)

    def kill_by_name(self):
        cmd = f"taskkill /f /im {self.__process_path_or_name}"
        run(cmd, stdout=PIPE, stderr=PIPE)
