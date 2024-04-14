from starlette.applications import Starlette
from starlette.routing import Route
from pathlib import Path
import logging

from .filerouter import get_all_routes, get_static_dir

logger = logging.getLogger(__name__)


class Green(Starlette):
    _pages = []

    def __init__(
        self, debug: bool = False, routes: list[Route] = [], *args, **kwargs
    ) -> None:
        curr_path = Path("src")
        routes.extend(get_all_routes(curr_path))
        if static := get_static_dir(curr_path):
            routes.append(static)
        logger.setLevel(logging.DEBUG)
        logging.debug(f"routes{routes}")
        super().__init__(debug, routes, *args, **kwargs)

    @classmethod
    def page(cls, func):
        # print('called')
        cls._pages.append(func)
        # print(cls.pages)
        return func

    @classmethod
    def _get_last_page(cls):
        return cls._pages[-1]
