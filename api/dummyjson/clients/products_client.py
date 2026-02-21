from api.dummyjson.clients.base_client import BaseClient


class ProductsClient(BaseClient):

    def get_products(self):
        return self.get("/products")

    def get_product_by_id(self, product_id: int):
        return self.get(f"/products/{product_id}")

    def create_product(self, body: dict):
        return self.post("/products/add", json=body)

    def update_product(self, product_id: int, body: dict):
        return self.put(f"/products/{product_id}", json=body)

    def delete_product(self, product_id: int):
        return self.delete(f"/products/{product_id}")
