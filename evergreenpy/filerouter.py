import logging
from typing import Optional
from pathlib import Path
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
import importlib


def get_all_routes(file_path: Path) -> list[Route]:
    all_files = get_all_files(file_path)
    auto_file_routes = []
    for file in all_files:
        if "page.py" != file.name:
            continue
        try:
            spec = importlib.util.spec_from_file_location("page", str(file))
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            route_path = (
                str(file.as_posix())
                .removeprefix(str(file_path.as_posix()))
                .removesuffix("page.py")
            )
            auto_file_routes.append(Route(route_path, module.Green._get_last_page()))
            logging.debug(f"added route {route_path} successfully")
        except Exception as e:
            logging.error(f"error adding route - {e}")
    return auto_file_routes


def get_static_dir(file_path: Path) -> Optional[Mount]:
    if file_path.exists():
        return Mount("/static", StaticFiles(directory=file_path))


def get_all_files(file_path: Path) -> list[Path]:
    files = []
    for f in file_path.iterdir():
        if f.is_file():
            files.append(f)
        if f.is_dir():
            files.extend(get_all_files(f))
    return files
