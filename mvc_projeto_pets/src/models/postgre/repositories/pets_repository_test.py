from unittest import mock

import pytest
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from sqlalchemy.exc import NoResultFound

from .pets_repository import PetsRepository
from ..entities.pets import PetsTable


class MockConnection:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(PetsTable)],
                    [PetsTable(id=1, name="dog", type="dog"), PetsTable(id=2, name="cat", type="cat")]
                )
            ]
        )

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass


class MockConnectionNoResult:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_no_result_found

    def __raise_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self): return self

    def __exit__(self, exc_type, exc_val, exc_tb): pass


def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    # Valida se foi chamado o query e o all, e se foi usado algum filtro
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    # Garante que vieram exatamente 2 itens
    assert len(response) == 2

    # Valida o primeiro pet (dog)
    assert response[0].id == 1
    assert response[0].name == "dog"
    assert response[0].type == "dog"

    # Valida o segundo pet (cat)
    assert response[1].id == 2
    assert response[1].name == "cat"
    assert response[1].type == "cat"


def test_list_pets_no_results():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.list_pets()

    # Valida se foi chamado o query e o all, e se foi usado algum filtro
    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    # Garante que vieram exatamente 2 itens
    assert len(response) == 0


def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    repo.delete_pet(1)

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.filter.assert_called_once_with(PetsTable.id == 1)
    mock_connection.session.delete.assert_called_once()


def test_delete_pet_not_found_pet():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete_pet(1)

    mock_connection.session.query.assert_called_once_with(PetsTable)
    mock_connection.session.rollback.assert_called_once()
