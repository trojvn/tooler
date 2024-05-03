from paths import str_to_path
from pathlib import Path
import os


class Process:
    def __init__(self):
        pass

    @staticmethod
    def kill_by_path(path: str | Path):
        path = str_to_path(path)
        if not path.is_file():
            return
        cmd = f"""WMIC Process Where "ExecutablePath='{path}'" """
        cmd += "Call Terminate"
        tmp_file = Path("tmp.bat")
        with tmp_file.open("w", encoding="utf-8") as f:
            f.write(cmd)
        os.system(tmp_file)
        os.remove(tmp_file)
