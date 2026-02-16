from django.core.paginator import Paginator
from ..models import Task


def paginationList(request):
  qs = Task.objects.all()
  
  paginator = Paginator(qs,5)
  
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  return page_obj