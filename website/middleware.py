from django.conf import settings
from whitenoise.middleware import WhiteNoiseMiddleware


class MediaWhiteNoiseMiddleware(WhiteNoiseMiddleware):
    """Serve version-controlled starter media under Django's MEDIA_URL."""

    def __init__(self, get_response=None, settings=settings):
        super().__init__(get_response, settings)
        self.add_files(settings.MEDIA_ROOT, prefix=settings.MEDIA_URL)
