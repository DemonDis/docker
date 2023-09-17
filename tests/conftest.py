from _pytest.config import Config
from _pytest.reports import TestReport


def pytest_report_teststatus(report: TestReport, config: Config):
    if (
        report.when == "call"
        and "unknown" in report.keywords.keys()
        and report.keywords["unknown"]
    ):
        c = config._color_for_special_type = {"type": "unknown", "symbol": "❄", "color": "cyan"}
        return c["type"], c["symbol"], (c["type"].upper(), {c["color"]: True})
    
    # https://github.com/pytest-dev/pytest/issues/9961