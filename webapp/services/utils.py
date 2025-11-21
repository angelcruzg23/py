import os


def project_root() -> str:
    # Subimos dos niveles para llegar a la raíz del proyecto
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def ensure_profiles_dir() -> str:
    base = project_root()
    dirpath = os.path.join(base, "data", "user_profiles")
    os.makedirs(dirpath, exist_ok=True)
    return dirpath


def safe_username(username: str) -> str:
    if not username:
        return "user"
    safe = "".join(c for c in username if c.isalnum() or c in ('-', '_')).strip()
    return safe or "user"
