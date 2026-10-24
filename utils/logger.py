"""
ANSI Colorized Terminal Logger
Zero-dependency, clean structured logging.
"""

import sys
from datetime import datetime

class Logger:
    COLORS = {
        "INFO": "\033[94m",
        "SUCCESS": "\033[92m",
        "WARN": "\033[93m",
        "ERROR": "\033[91m",
        "RESET": "\033[0m"
    }

    @classmethod
    def _log(cls, level: str, msg: str):
        ts = datetime.now().strftime("%H:%M:%S")
        color = cls.COLORS.get(level, cls.COLORS["RESET"])
        reset = cls.COLORS["RESET"]
        print(f"\033[90m[{ts}]\033[0m {color}{level:<7}{reset} {msg}")

    @classmethod
    def info(cls, msg: str): cls._log("INFO", msg)
    @classmethod
    def success(cls, msg: str): cls._log("SUCCESS", msg)
    @classmethod
    def warn(cls, msg: str): cls._log("WARN", msg)
    @classmethod
    def error(cls, msg: str): cls._log("ERROR", msg)

if __name__ == "__main__":
    Logger.info("Starting code-lab environment...")
    Logger.success("Database connection established.")
    Logger.warn("High memory consumption detected.")
    Logger.error("Failed to fetch payload from upstream.")
