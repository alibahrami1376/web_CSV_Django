import logging
import time
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware(MiddlewareMixin):
    """Middleware برای لاگ کردن تمام درخواست‌ها"""

    def process_request(self, request):
        """قبل از پردازش درخواست"""
        request._start_time = time.time()
        logger.info(f"Request started: {request.method} {request.path}")
        logger.info(
            f'User: {request.user.username if request.user.is_authenticated else "Anonymous"}'
        )
        logger.info(f"IP: {self.get_client_ip(request)}")
        logger.info("Everything is OK!")
        return None

    def process_response(self, request, response):
        """بعد از پردازش درخواست"""
        if hasattr(request, "_start_time"):
            duration = time.time() - request._start_time
            logger.info(
                f"Request completed: {request.method} {request.path} - Status: {response.status_code} - Duration: {duration:.3f}s"
            )
            if response.status_code >= 400:
                logger.warning(f"Request returned error status: {response.status_code}")
            else:
                logger.info("Everything is OK!")
        return response

    def process_exception(self, request, exception):
        """هنگام بروز خطا"""
        logger.error(
            f"Exception in request {request.method} {request.path}: {exception}"
        )
        logger.error(f"Exception type: {type(exception).__name__}")
        return None

    def get_client_ip(self, request):
        """دریافت IP کاربر"""
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0]
        else:
            ip = request.META.get("REMOTE_ADDR")
        return ip
