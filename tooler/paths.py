from pathlib import Path


def str_to_path(path: Path | str) -> Path:
    """Конверт str -> Path"""
    if isinstance(path, str):
        path = Path(path)
    return path
