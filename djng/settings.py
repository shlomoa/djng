from contextlib import contextmanager
from typing import Any, Dict

from django.conf import settings
from rest_framework.settings import APISettings, perform_import

DJNG_DEFAULTS: Dict[str, Any] = {
    # General attributes
    'NG_ROOT_DIR': 'ng',
    # Command default attributes
    'NG_BUILD_ATTRIBUTES': {"--output-hashing": "none", "--output-path": 'ng_dist'},
    'NG_GEN_ATTRIBUTES': {'--style': 'scss', '--routing': 'true', '--defaults': 'true'},
    'NG_NEW_ATTRIBUTES': {'--create-application': 'false', '--style': 'scss',
                          '--skip-git': 'true', '--defaults': 'true'}
}

IMPORT_STRINGS = [
    'DEFAULT_GENERATOR_CLASS',
    'SERVE_AUTHENTICATION',
    'SERVE_PERMISSIONS',
    'POSTPROCESSING_HOOKS',
    'PREPROCESSING_HOOKS',
    'GET_LIB_DOC_EXCLUDES',
    'GET_MOCK_REQUEST',
    'SORT_OPERATIONS',
    'SORT_OPERATION_PARAMETERS',
    'AUTHENTICATION_WHITELIST',
    'RENDERER_WHITELIST',
    'PARSER_WHITELIST',
    'WEBHOOKS',
]


class DjngSettings(APISettings):
    _original_settings: Dict[str, Any] = {}

    def apply_patches(self, patches):
        for attr, val in patches.items():
            if attr in self.import_strings:
                val = perform_import(val, attr)
            # load and store original value, then override __dict__ entry
            self._original_settings[attr] = getattr(self, attr)
            setattr(self, attr, val)

    def clear_patches(self):
        for attr, orig_val in self._original_settings.items():
            setattr(self, attr, orig_val)
        self._original_settings = {}


djng_settings = DjngSettings(
    user_settings=getattr(settings, 'DJNG_SETTINGS', {}),  # type: ignore
    defaults=DJNG_DEFAULTS,  # type: ignore
    import_strings=IMPORT_STRINGS,
)


@contextmanager
def patched_settings(patches):
    """ temporarily patch the global spectacular settings (or do nothing) """
    if not patches:
        yield
    else:
        try:
            djng_settings.apply_patches(patches)
            yield
        finally:
            djng_settings.clear_patches()
