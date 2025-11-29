import os
import base64
import logging
import pytest

logger = logging.getLogger(__name__)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            try:
                if hasattr(item.instance, "screenshots"):
                    for shot in item.instance.screenshots:
                        screenshot_path = os.path.join("screenshots", shot)
                        if os.path.exists(screenshot_path):
                            with open(screenshot_path, "rb") as image_file:
                                encoded = base64.b64encode(image_file.read()).decode("utf-8")
                                extras.append(pytest_html.extras.image(
                                    f"data:image/png;base64,{encoded}",
                                    mime_type="image/png",
                                    extension="png"
                                ))
            except Exception as e:
                logger.error(f"Exception adding screenshot to report: {e}")
        report.extras = extras
