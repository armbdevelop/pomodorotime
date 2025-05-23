from .ping import router as ping_route
from .tasks import router as task_route
from .user import router as user_route
from .auth import router as auth_route

routers = [ping_route, task_route, user_route, auth_route]