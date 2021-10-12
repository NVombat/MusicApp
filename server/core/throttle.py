from rest_framework import throttling


class throttle(throttling.AnonRateThrottle):
    scope = "init_throttle"

    def allow_request(self, request, view):
        # If GET Methods need to be unrestricted
        if request.method == "GET":
            return True
        return super().allow_request(request, view)
