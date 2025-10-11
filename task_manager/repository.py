def save(self, task):
    task.id = self._next_id
    self._next_id += 1
    self.storage.add(task.id, task)
    return task