import logging
from pathlib import Path
from shutil import move, rmtree


def str_to_path(path: Path | str) -> Path:
    """Конверт str -> Path"""
    if isinstance(path, str):
        path = Path(path)
    return path


def remove_item(path: Path):
    """Удаляет path"""
    if path.is_file():
        return path.unlink(True)
    rmtree(path, ignore_errors=True)


def move_item(src: Path, dst: Path, overwrite: bool, debug: bool = False) -> bool:
    """Перемещает src в dst"""
    if overwrite:
        remove_item(dst / src.name)
    try:
        move(src, dst / src.name)
        return True
    except Exception as e:
        if debug:
            logging.exception(e)
        return False
