import logging
import time

import allure
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class BaseClient:
    def __init__(self, base_url: str, token: str | None = None):
        self.base_url = base_url.rstrip("/")
        self.token = token

    def _headers(self) -> dict:
        headers = {"Content-Type": "application/json"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        return headers

    def _log_request(self, method: str, url: str, json: dict | None):
        with allure.step(f"REQUEST → {method} {url}"):
            allure.attach(
                body=f"METHOD: {method}\nURL: {url}\nBODY: {json}",
                name="Request",
                attachment_type=allure.attachment_type.TEXT
            )

    def _log_response(self, response: requests.Response, elapsed: float):
        with allure.step(f"RESPONSE ← {response.status_code}"):
            allure.attach(
                body=f"STATUS: {response.status_code}\nBODY: {response.text}",
                name="Response",
                attachment_type=allure.attachment_type.TEXT
            )

        logger.info(
            f"{response.request.method} {response.url} "
            f"→ {response.status_code} ({elapsed:.3f}s)"
        )

    def _request(self, method: str, path: str, json=None, **kwargs) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"

        self._log_request(method, url, json)

        start = time.time()
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self._headers(),
                json=json,
                **kwargs
            )
        except Exception as exc:
            logger.error(f"Request failed: {exc}")
            raise
        elapsed = time.time() - start

        self._log_response(response, elapsed)
        return response

    def get(self, path: str, **kwargs) -> requests.Response:
        return self._request("GET", path, **kwargs)

    def post(self, path: str, json=None, **kwargs) -> requests.Response:
        return self._request("POST", path, json=json, **kwargs)

    def put(self, path: str, json=None, **kwargs) -> requests.Response:
        return self._request("PUT", path, json=json, **kwargs)

    def delete(self, path: str, **kwargs) -> requests.Response:
        return self._request("DELETE", path, **kwargs)
