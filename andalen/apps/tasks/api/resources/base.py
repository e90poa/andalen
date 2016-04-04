from restless.modelviews import ListEndpoint, DetailEndpoint

from ...models import Task

class TaskList(ListEndpoint):
    model = Task

class TaskDetail(DetailEndpoint):
    model = Task