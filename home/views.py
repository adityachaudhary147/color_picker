from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.colorpicker import finding_border_color,finding_dominating_color

def homeView(request):
    return render(request, 'index.html')

@api_view(['POST'])
def ColorPickerView(request):
    """
    Send image url like this:
    {
        "imgurl": "_imgurl__"
    }
    {
        "imgurl": "https://storage.googleapis.com/bizupimg/profile_photo/kppl_logo.png"
    }
    {
        "imgurl": "https://storage.googleapis.com/bizupimg/profile_photo/918527129869%20instagram-logo-png-2451.png"
    }
    """
    if request.method == 'POST':
        imgurl = request.data['imgurl']
        dominant_color=finding_dominating_color(imgurl)
        logo_border=finding_border_color(imgurl)
        resp = { 'dominant_color': dominant_color,'logo_border': logo_border}
        return Response([resp], status=200)
    else:
        return HttpResponse([{'Error':"Bad Request"}], status=400)

