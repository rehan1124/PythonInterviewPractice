import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(autouse=True)
def setup(browser):
    print(f"\nLaunching portal in {browser.upper()}")
    yield browser
    print(f"\nClosing {browser.upper()} browser.")
