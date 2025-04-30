import pytest
from main import BooksCollector

# Фикстура для создания экземпляра BooksCollector перед каждым тестом
@pytest.fixture
def collector():
    return BooksCollector()
