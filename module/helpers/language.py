import i18n
from ..common.common_config import get_language_base_path


def load_language():
    i18n.load_path.append(get_language_base_path())
    return i18n
