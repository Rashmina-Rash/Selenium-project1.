from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='ie':
        driver=webdriver.Ie()
    elif browser=='firefox':
        driver=webdriver.Firefox()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):   #this will get the value from CLI/hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):   #this will return the browser value to setup method
    return request.config.getoption("--browser")

#### pytest HTML reports

def pytest_configure(config):
    config._metadata = {
            "Tester": "Rashmina",
            "Project Name": "Hybrid Framework Practice",
        }

 #hook for delete/modify enviroment info to HTML report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("plugins",None)
