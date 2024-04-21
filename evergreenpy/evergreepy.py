from starlette.applications import Starlette
from starlette.routing import Route
from pathlib import Path

from typing import Union
from .filerouter import get_all_routes, get_static_dir


class Green(Starlette):
    _pages = []

    def __init__(
        self,
        root_path: Union[str, Path] = Path("src"),
        static_path: Union[str, Path] = Path("static"),
        debug: bool = False,
        routes: list[Route] = [],
        *args,
        **kwargs,
    ) -> None:
        if isinstance(root_path, str):
            root_path = Path(root_path)
        routes.extend(get_all_routes(root_path))

        if isinstance(static_path, str):
            static_path = Path(static_path)
        if static := get_static_dir(static_path):
            routes.append(static)

        super().__init__(debug, routes, *args, **kwargs)

    @classmethod
    def page(cls, func):
        cls._pages.append(func)
        return func

    @classmethod
    def _get_last_page(cls):
        return cls._pages[-1]
