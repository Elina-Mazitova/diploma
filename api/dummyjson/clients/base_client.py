import logging
import time

import allure
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseClient:

    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def _log_request(self, method: str, url: str, **kwargs):
        with allure.step(f"REQUEST → {method} {url}"):
            if "json" in kwargs and kwargs["json"] is not None:
                allure.attach(
                    str(kwargs["json"]),
                    name="Request JSON",
                    attachment_type=allure.attachment_type.JSON
                )

            if "headers" in kwargs and kwargs["headers"] is not None:
                allure.attach(
                    str(kwargs["headers"]),
                    name="Request Headers",
                    attachment_type=allure.attachment_type.TEXT
                )

    def _log_response(self, response: requests.Response, elapsed: float):
        with allure.step(f"RESPONSE ← {response.status_code}"):
            allure.attach(
                str(response.status_code),
                name="Status Code",
                attachment_type=allure.attachment_type.TEXT
            )

            try:
                allure.attach(
                    response.text,
                    name="Response Body",
                    attachment_type=allure.attachment_type.JSON
                )
            except ValueError:
                allure.attach(
                    response.text,
                    name="Response Body (raw)",
                    attachment_type=allure.attachment_type.TEXT
                )

        logger.info(
            f"{response.request.method} {response.url} "
            f"→ {response.status_code} ({elapsed:.3f}s)"
        )

    def _request(self, method: str, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"

        self._log_request(method, url, **kwargs)

        start = time.time()
        try:
            response = requests.request(method, url, **kwargs)
        except Exception as exc:
            logger.error(f"Request failed: {exc}")
            raise
        elapsed = time.time() - start

        self._log_response(response, elapsed)

        return response

    def get(self, endpoint: str, **kwargs):
        return self._request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self._request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self._request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self._request("DELETE", endpoint, **kwargs)
