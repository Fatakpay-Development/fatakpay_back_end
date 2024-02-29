import pytest

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="DEV", help="Environment to run the tests (DEV or UAT)")

@pytest.fixture(scope="class")
def url_link(request):
    env = request.config.getoption("--env", default="DEV")
    if env == "DEV":
        return "https://devonboardingapi.fatakpay.com"
    elif env == "UAT":
        return "https://uatonboardingapi.fatakpay.com"
    else:
        return None

# pytest --env=UAT
