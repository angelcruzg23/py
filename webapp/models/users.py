import os
from ..services.utils import project_root


def _users_file_path():
    base = project_root()
    return os.path.normpath(os.path.join(base, "data", "users.txt"))


def load_users():
    path = _users_file_path()
    users = {}
    try:
        with open(path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" in line:
                    user, pwd = line.split(":", 1)
                    users[user.strip()] = pwd.strip()
    except FileNotFoundError:
        # No users file yet
        pass
    return users


def validate_user(username: str, password: str) -> bool:
    users = load_users()
    return username in users and users[username] == password
