import sunau
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse,Http404,JsonResponse



class ApiSession(APIView):
    def get(self,request):
        session=request.session['card']
        if session:
            count=len(session)
        else:
            count=''    
        dichvu={'rodo':'okoment','session':session,'count':count}
        return Response(dichvu)


def ApiSession1(request):
    if request.method == 'GET':
        try:
            session=request.session['card']
            if session:
                count=len(session)
            else:
                count=''    
            dichvu={'count':count,'session':session}
            todo=count
            return JsonResponse(dichvu)
        except:
            return JsonResponse({'card':'Không có'})