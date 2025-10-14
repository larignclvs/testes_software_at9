# tests/test_task.py
import pytest
from datetime import datetime, timedelta

from task_manager.task import Task, Priority, Status


def test_task_valida():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "Estudar", "Python", Priority.ALTA, prazo)

    # não deve lançar erro
    task.validar()

    assert task.titulo == "Estudar"
    # opcional, mas útil: status padrão
    assert task.status == Status.PENDENTE


def test_titulo_curto_invalido():
    prazo = datetime.now() + timedelta(days=1)
    task = Task(None, "AB", "Desc", Priority.BAIXA, prazo)

    with pytest.raises(ValueError):
        task.validar()


def test_prazo_no_passado_invalido():
    prazo_passado = datetime.now() - timedelta(minutes=1)
    task = Task(None, "Estudar", "Python", Priority.MEDIA, prazo_passado)

    with pytest.raises(ValueError):
        task.validar()