from contextlib import contextmanager
from time import sleep
from playwright.sync_api import Page, expect
import pytest
# from playwright.sync_api import Page, expect

LOCAL_TEST = True 

PORT = "8501" if LOCAL_TEST else "8699"


@pytest.fixture(scope="module", autouse=True)
def before_module():
    # Run the streamlit app before each module
    with run_streamlit():
        yield


@pytest.fixture(scope="function", autouse=True)
def before_test(page: Page):
    page.goto(f"localhost:{PORT}")


@contextmanager
def run_streamlit():
    """Run the streamlit app at examples/streamlit_app.py on port 8599"""
    import subprocess

    if LOCAL_TEST:
        try:
            yield 1
        finally:
            pass
    else:
        p = subprocess.Popen(
            [
                "streamlit",
                "run",
                "examples/streamlit_app.py",
                "--server.port",
                PORT,
                "--server.headless",
                "true",
            ]
        )

        sleep(5)

        try:
            yield 1
        finally:
            p.kill()

def test_wheat_health_dashboard(page: Page):

    # Wait for the app to load
    expect(page).to_have_title("Wheat Health Monitoring Dashboard")
    # columns = page.query_selector_all(".css-1r6slb0")
    # assert len(columns) == 3
    # for column in columns:
    #     metric_text = column.inner_text()
    #     print(metric_text)
    #     # metric_elements = column.query_selector_all(".css-1r6slb0")
