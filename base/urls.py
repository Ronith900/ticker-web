from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from snippets import views as snip_views
from task import views as task_view


router = DefaultRouter()
router.register(r'snippets', snip_views.SnippetViewSet,basename="snippet")
router.register(r'users', snip_views.UserViewSet,basename="user")
router.register(r'tasklabels', task_view.TaskLabelViewSet,basename="tasklabel")
router.register(r'tasks', task_view.TaskViewSet,basename="task")

urlpatterns = [
    path('', include(router.urls)),
]