def validate_input(data: str) -> bool:
    """Fungsi sederhana untuk validasi input string."""
    if not data or len(data.strip()) == 0:
        return False
    return True