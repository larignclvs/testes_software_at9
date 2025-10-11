def test_save_atribui_id(mocker):
    mock_storage = mocker.Mock()
    repo = TaskRepository(mock_storage)
    task = Task(None, "Teste", "Desc",
    Priority.BAIXA, datetime.now())
    resultado = repo.save(task)
    assert resultado.id == 1
    mock_storage.add.assert_called_once()