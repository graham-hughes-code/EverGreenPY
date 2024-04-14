from evergreenpy.filerouter import get_all_files, get_all_routes
import pytest

TEST_FILE_CONTENT = """
from starlette.responses import JSONResponse


async def page(request):
    return JSONResponse({"hello": "test"})
"""


@pytest.fixture(scope="session")
def test_path(tmp_path_factory):
    d = tmp_path_factory.mktemp("src") / "test_get_all_files"
    d.mkdir()
    f1 = d / "page.py"
    f1.write_text(TEST_FILE_CONTENT)
    f2 = d / "something.py"
    f2.write_text(TEST_FILE_CONTENT)
    f3 = d / "file.yaml"
    f3.write_text("test")
    d2 = d / "some_path"
    d2.mkdir()
    f4 = d2 / "page.py"
    f4.write_text(TEST_FILE_CONTENT)
    return d


def test_get_all_files(test_path):
    assert len(get_all_files(test_path)) == 4


def test_get_all_routes(test_path):
    assert len(get_all_routes(test_path)) == 2
