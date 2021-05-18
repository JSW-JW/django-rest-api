from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class CSRFExemptMixin:
    @method_decorator(csrf_exempt)
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)