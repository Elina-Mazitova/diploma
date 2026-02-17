import requests
import allure


class BaseClient:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")

    def _headers(self):
        return {"Content-Type": "application/json"}

    def _log_request(self, method: str, url: str, json: dict | None):
        allure.attach(
            body=f"METHOD: {method}\nURL: {url}\nBODY: {json}",
            name="Request",
            attachment_type=allure.attachment_type.TEXT
        )

    def _log_response(self, response: requests.Response):
        allure.attach(
            body=f"STATUS: {response.status_code}\nBODY: {response.text}",
            name="Response",
            attachment_type=allure.attachment_type.TEXT
        )

    def _request(self, method: str, path: str, json=None, **kwargs):
        url = f"{self.base_url}/{path.lstrip('/')}"

        self._log_request(method, url, json)

        response = requests.request(
            method=method,
            url=url,
            headers=self._headers(),
            json=json,
            **kwargs
        )

        self._log_response(response)
        return response

    def get(self, path: str, **kwargs):
        return self._request("GET", path, **kwargs)

    def post(self, path: str, json=None, **kwargs):
        return self._request("POST", path, json=json, **kwargs)

    def put(self, path: str, json=None, **kwargs):
        return self._request("PUT", path, json=json, **kwargs)

    def delete(self, path: str, **kwargs):
        return self._request("DELETE", path, **kwargs)
