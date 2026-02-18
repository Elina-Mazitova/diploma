import requests


class ProductsClient:
    BASE_URL = "https://dummyjson.com"

    def get_products(self):
        return requests.get(f"{self.BASE_URL}/products")

    def get_product_by_id(self, product_id):
        return requests.get(f"{self.BASE_URL}/products/{product_id}")

    def create_product(self, payload: dict):
        return requests.post(f"{self.BASE_URL}/products/add", json=payload)

    def update_product(self, product_id, payload: dict):
        return requests.put(f"{self.BASE_URL}/products/{product_id}", json=payload)

    def delete_product(self, product_id):
        return requests.delete(f"{self.BASE_URL}/products/{product_id}")
