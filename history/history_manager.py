from collections import deque
from typing import Any, Optional

class HistoryManager:
    """Управление историей действий с использованием стека (undo) и очереди (redo)"""
    
    def __init__(self, max_size: int = 50):
        self._undo_stack = []  # Стек для операций отмены (LIFO)
        self._redo_queue = deque()  # Очередь для повтора (FIFO)
        self._max_size = max_size
    
    def push_action(self, action: dict):
        """Добавление действия в историю"""
        self._undo_stack.append(action)
        
        # Ограничиваем размер стека
        if len(self._undo_stack) > self._max_size:
            self._undo_stack.pop(0)
        
        # Очищаем очередь redo при новом действии
        self._redo_queue.clear()
    
    def undo(self) -> Optional[dict]:
        """Отмена последнего действия (из стека)"""
        if self._undo_stack:
            action = self._undo_stack.pop()
            self._redo_queue.append(action)
            return action
        return None
    
    def redo(self) -> Optional[dict]:
        """Повтор отменённого действия (из очереди)"""
        if self._redo_queue:
            action = self._redo_queue.pop() if self._redo_queue else None
            if action:
                self._undo_stack.append(action)
            return action
        return None
    
    def can_undo(self) -> bool:
        """Можно ли отменить действие"""
        return len(self._undo_stack) > 0
    
    def can_redo(self) -> bool:
        """Можно ли повторить действие"""
        return len(self._redo_queue) > 0


class ActionType:
    """Типы действий для истории"""
    ADD = "ADD"
    EDIT = "EDIT"
    DELETE = "DELETE"