from rest_framework import viewsets
from . common_api_response import *

# ========= FILE UPLOAD API's CLASS HERE ========
class CbtUserViewSet(viewsets.ModelViewSet):
    
    # FILE DATA UPLOAD FUNCTION HERE
    def UserAdd(self, request):
        return 1