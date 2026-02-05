from datetime import date
import difflib
import uuid
import json
import os

BASE_DIR = os.path.dirname(__file__)
SAVE_TO = os.path.join(BASE_DIR, 'taskfile.json')

class TaskManager:
    def __init__(self, save_to):
        self.save_to = save_to
        self._manager = []

    @property
    def save_to(self):
        return self._save_to
    
    @save_to.setter
    def save_to(self, file_path):
        if not isinstance(file_path, str):
            raise TypeError('file path has to be a string')
        self._save_to = file_path

    def add(self, task):
        if not isinstance(task, Task):
            raise TypeError(f'task has to be a instance of Task')
        
        for t in self._manager:
            if task.text.lower() == t.text.lower():
                return {'status': 'duplicate', 'task': task}
            
        self._manager.append(task)
        return {'status': 'added', 'task': task}


    def save(self):
        data = [task.to_dict() for task in self._manager]
        with open(self.save_to, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=2)

    def load(self):
        # Se o arquivo não existe ou está vázio, cria um e preenche com []
        self._manager = []

        if not os.path.exists(self.save_to):
            with open(self.save_to, 'w', encoding='utf-8') as file:
                json.dump([], file)
                return
            
        with open(self.save_to, 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

            for datatask in data:
                self._manager.append(Task.from_dict(datatask))

    def _get_suggestions(self, task_name):
        if not self._manager:
            return []
        
        task_texts = [task.text.lower() for task in self._manager]
        return difflib.get_close_matches(
            task_name.lower(), task_texts, n=1, cutoff=0.6
            )

    def delete(self, task_name):
        # Achou com certeza
        for task in self._manager:
            if task_name.lower() == task.text.lower():
                self._manager.remove(task)
                return {'status': 'find', 'task': task}
        
        # Achou parecido
        suggestion = self._get_suggestions(task_name)

        if suggestion:
            return {'status': 'suggestion', 'task': suggestion[0]}

        # Não achou
        return {'status': 'not_found'}

    def search(self, task_name):
        # Achou com certeza
        for task in self._manager:
            if task_name.lower() == task.text.lower():
                return {'status': 'find', 'task': task}
        
        # Achou parecido
        suggestion = self._get_suggestions(task_name)
        
        if suggestion:
            return {'status': 'suggestion', 'task': suggestion[0]}

        # Não achou
        return {'status': 'not_found'}
    
    def delall(self):
        self._manager = []

    def see(self):
        tasks = []
        for task in self._manager:
            tasks.append(
                {
                    'text': task.text,
                    'date': task.date,
                    'done': True if task.done else False
                }
            )
        return tasks
    
    def mark_done(self, task_name):
        # Marca uma task como concluida.
        for task in self._manager:
            if task_name.lower() == task.text.lower():
                task.done = True
                return {'status': 'find', 'task': task}
            
        suggestion = self._get_suggestions(task_name)

        if suggestion:
            return {'status': 'suggestion', 'task': suggestion[0]}

        return {'status': 'not_found'}
            

class Task:
    def __init__(self):
        self._id = str(uuid.uuid4())
        self._text = None
        self.date = date.today().isoformat()
        self._done = False

    @property
    def text(self):
        return self._text
    
    @text.setter
    def text(self, text):
        self._text = str(text).strip()

    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, done):
        if not isinstance(done, bool):
            raise TypeError('done has to be a bool')
        self._done = done

    @classmethod
    def from_dict(cls, data):
        task = cls()
        task.text = data['text']
        task._id = data['id']
        task.date = data['date']
        task.done = data['done']
        return task

    def to_dict(self):
        return {
            'id': self._id,
            'text': self._text,
            'date': self.date,
            'done': self.done
        }
