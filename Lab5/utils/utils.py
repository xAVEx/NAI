from typing import Any
import joblib


def save_instance(instance: Any, path: str) -> None:
    joblib.dump(instance, path)


def load_instance(path: str) -> Any:
    return joblib.load(path)
