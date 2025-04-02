from django.views import View
from django.http import  JsonResponse
from django.shortcuts import  render
from django.db.models import Q
from material.models import *
from labour.models import *
from contact.models import *
from api.v1.module.forms.matrial_forms import *
from django.shortcuts import get_object_or_404


class IndexView(View):
    def get(self, request):
        labour_count = Labour.objects.all().count()
        matrial_count = Matrial.objects.all().count()
        review_count = LabourReview.objects.all().count() +  MatrialReview.objects.all().count()
        matrial_list = Matrial.objects.all().order_by('-id')
        labour_list = Labour.objects.all().order_by('-id')
        context ={
            'labour_count':labour_count,
            "matrial_count":matrial_count,
            "review_count":review_count,
            "matrial_list":matrial_list,
            "labour_list":labour_list
        }
        return render( request , 'index.html' , context)

class AboutView(View):
    def get(self, request):
        return render( request , 'about-us.html')

class ConatctView(View):
    def get(self, request):
        return render( request , 'contact-us.html')
    
class FavoriteMatrialAdd(View):
    def post(self, request, matrial_id):
        matrial = get_object_or_404(Matrial, id=matrial_id)
        matrial_list = request.session.get("matrialList", [])
        if matrial_id not in matrial_list:
            matrial_list.append(matrial_id)
            request.session["matrialList"] = matrial_list
            request.session.modified = True
        return JsonResponse({"message": "matrial added to favorites", "matrialList": matrial_list, "status": "success"})

    def delete(self, request, matrial_id):
        matrial_list = request.session.get("matrialList", [])
        if matrial_id in matrial_list:
            matrial_list.remove(matrial_id)
            request.session["matrialList"] = matrial_list
            request.session.modified = True
        return JsonResponse({"message": "matrial removed from favorites", "matrialList": matrial_list, "status": "success"})


class FavoriteLabourAdd(View):
    def post(self, request, labour_id):
        labour = get_object_or_404(Labour, id=labour_id)
        labour_list = request.session.get("labourList", [])
        if labour_id not in labour_list:
            labour_list.append(labour_id)
            request.session["labourList"] = labour_list
            request.session.modified = True
        return JsonResponse({"message": "Labour added to favorites", "labourList": labour_list, "status": "success"})

    def delete(self, request, labour_id):
        labour_list = request.session.get("labourList", [])
        if labour_id in labour_list:
            labour_list.remove(labour_id)
            request.session["labourList"] = labour_list
            request.session.modified = True
        return JsonResponse({"message": "Labour removed from favorites", "labourList": labour_list, "status": "success"})


class CompressionMatrialAdd(View):
    def post(self, request, matrial_id):
        matrial = get_object_or_404(Matrial, id=matrial_id)
        matrial_list = request.session.get("matrialCompressionList", [])
        if matrial_id not in matrial_list:
            matrial_list.append(matrial_id)
            request.session["matrialCompressionList"] = matrial_list
            request.session.modified = True
        return JsonResponse({"message": "matrial added to Compression", "matrialCompressionList": matrial_list, "status": "success"})

    def delete(self, request, matrial_id):
        matrial_list = request.session.get("matrialCompressionList", [])
        if matrial_id in matrial_list:
            matrial_list.remove(matrial_id)
            request.session["matrialCompressionList"] = matrial_list
            request.session.modified = True
        return JsonResponse({"message": "matrial removed from Compression", "matrialCompressionList": matrial_list, "status": "success"})


class CompressionLabourAdd(View):
    def post(self, request, labour_id):
        labour = get_object_or_404(Labour, id=labour_id)
        labour_list = request.session.get("labourCompressionList", [])
        if labour_id not in labour_list:
            labour_list.append(labour_id)
            request.session["labourCompressionList"] = labour_list
            request.session.modified = True
        return JsonResponse({"message": "Labour added to Compression", "labourCompressionList": labour_list, "status": "success"})

    def delete(self, request, labour_id):
        labour_list = request.session.get("labourCompressionList", [])
        if labour_id in labour_list:
            labour_list.remove(labour_id)
            request.session["labourCompressionList"] = labour_list
            request.session.modified = True
        return JsonResponse({"message": "Labour removed from Compression", "labourCompressionList": labour_list, "status": "success"})


class FavList(View):
    def get(self, request):
        matrial_ids = request.session.get("matrialList", [])
        labour_ids = request.session.get("labourList", [])

        matrials = list(Matrial.objects.filter(id__in=matrial_ids))
        labours = list(Labour.objects.filter(id__in=labour_ids))

        context = {
            "matrial_list": matrials,
            "labour_list": labours,
            "message": "Fav List fetched successfully",
            "status": "success"
        }
        return render(request, 'favorite.html', context) 
    
    


class ComList(View):
    def get(self, request):
        matrial_ids = request.session.get("matrialCompressionList", [])
        labour_ids = request.session.get("labourCompressionList", [])

        matrials = list(Matrial.objects.filter(id__in=matrial_ids))
        labours = list(Labour.objects.filter(id__in=labour_ids))

        context = {
            "matrial_list": matrials,
            "labour_list": labours,
            "message": "Compression List fetched successfully",
            "status": "success"
        }
        return render(request, 'compression.html', context) 