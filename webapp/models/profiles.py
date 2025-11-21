import json
import os
from ..services.utils import ensure_profiles_dir, safe_username


def _user_profile_path(username: str) -> str:
    dirpath = ensure_profiles_dir()
    fname = f"{safe_username(username)}.json"
    return os.path.join(dirpath, fname)


def save_user_data(username: str, data: dict):
    path = _user_profile_path(username)
    try:
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(data, fh, ensure_ascii=False, indent=2)
    except OSError:
        # En prototipo ignoramos errores de escritura
        pass


def load_user_data(username: str) -> dict:
    path = _user_profile_path(username)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh) or {}
    except (FileNotFoundError, json.JSONDecodeError, OSError):
        return {}
