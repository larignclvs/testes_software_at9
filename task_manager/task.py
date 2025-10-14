# task_manager/task.py
from __future__ import annotations

from enum import IntEnum, Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


class Priority(IntEnum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3


class Status(Enum):
    PENDENTE = "pendente"
    EM_PROGRESSO = "em_progresso"
    CONCLUIDA = "concluida"


@dataclass
class Task:
    id: Optional[int]
    titulo: str
    descricao: str
    prioridade: Priority
    prazo: datetime
    status: Status = Status.PENDENTE

    def validar(self) -> None:
        """Valida regras básicas da tarefa.

        - título com 3+ caracteres (desconsiderando espaços nas pontas)
        - prazo não pode estar no passado
        """
        # título
        if not isinstance(self.titulo, str) or len(self.titulo.strip()) < 3:
            raise ValueError("Título deve ter pelo menos 3 caracteres.")

        # prazo
        if not isinstance(self.prazo, datetime):
            raise ValueError("Prazo deve ser um datetime válido.")

        if self.prazo < datetime.now():
            raise ValueError("Prazo não pode estar no passado.")