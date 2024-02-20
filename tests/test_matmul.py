from fastapi.testclient import TestClient
from src.main import app_factory

from http import HTTPStatus


client = TestClient(app_factory())


def test_matmul():
    matrices = {
        "matrix1": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "matrix2": [[5, 1, -3], [-4, 0, 8], [7, 1, -2]],
        }

    response = client.post("/api/v1/matmul", json=matrices)

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "message": "success",
        "data": [[18, 4, 7], [42, 10, 16], [66, 16, 25]]
        }


def test_matmul_invalid_mat_dim():
    matrices = {
        "matrix1": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "matrix2": [[5, 1, -3], [-4, 0, 8]],
        }

    response = client.post("/api/v1/matmul", json=matrices)

    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_matmul_empty_mat():
    matrices = {
        "matrix1": [],
        "matrix2": [[1, 2]],
        }

    response = client.post("/api/v1/matmul", json=matrices)
    assert response.status_code == HTTPStatus.BAD_REQUEST


def test_matmul_invalid_req_fmt():
    # Missing field

    missing_matrices = {
        "matrix1": [[1, 2, 3]],
        }

    response = client.post("/api/v1/matmul", json=missing_matrices)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY

    # Input not a matrix

    not_mat_matrices = {
        "matrix1": [1, 2, 3],
        "matrix2": "hello",
        }

    response = client.post("/api/v1/matmul", json=not_mat_matrices)
    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
