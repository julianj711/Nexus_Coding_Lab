from abc import ABC, abstractmethod

from .models import Customer, CustomerSnapshot

import json

class CustomerRepository(ABC):
    @abstractmethod
    def save(self, customer: Customer) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, customer_id: str) -> Customer | None:
        raise NotImplementedError

    @abstractmethod
    def all(self) -> list[Customer]:
        raise NotImplementedError


class InMemoryCustomerRepository(CustomerRepository):
    """Simple repository with a reasonably narrow responsibility."""

    def __init__(self) -> None:
        self._customers: dict[str, Customer] = {}
        self._audit: list[dict] = []
        self.audit_load()

    def save(self, customer: Customer) -> None:
        self._customers[customer.customer_id] = customer

    def audit_log(self, audit: dict):
        self._audit.append(audit)

    def audit_load(self):
        with open("audit.json", "r", encoding="utf-8") as f:
            json_text = f.read()

            try:
                self._audit = json.loads(json_text)
            except Exception as e:
                pass

    def audit_save(self):
        with open("audit.json", "w") as f:
            # Convert each dict to a sorted JSON string to make it hashable
            unique_strings = {json.dumps(item, sort_keys=True) for item in self._audit}
            # Convert the unique strings back into dictionaries
            unique_data = [json.loads(item) for item in unique_strings]


            f.write(json.dumps(unique_data))


    def get(self, customer_id: str) -> Customer | None:
        return self._customers.get(customer_id)

    def all(self) -> list[Customer]:
        return list(self._customers.values())

    def snapshot(self, customer_id: str) -> CustomerSnapshot | None:
        customer = self.get(customer_id)
        return CustomerSnapshot.from_customer(customer) if customer else None
