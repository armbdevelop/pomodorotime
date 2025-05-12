from .ping import router as ping_route
from .tasks import router as task_route

routers = [ping_route, task_route]