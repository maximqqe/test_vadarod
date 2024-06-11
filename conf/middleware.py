import zlib
from django.utils.encoding import force_bytes


class AddCRC32HeaderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if response and response.content:
            crc32= zlib.crc32(force_bytes(response.content))
            response["CRC32"] = str(crc32)

        return response
