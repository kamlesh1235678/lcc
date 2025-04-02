from django.views import View
from django.http import  JsonResponse
from django.shortcuts import  render
from django.db.models import Q
from material.models import *
from api.v1.module.forms.matrial_forms import *


class MatrialListView(View):
    def get(self, request):
        search_term = request.GET.get('search', '')
        if search_term:
            matrial_list = Matrial.objects.filter(name__icontains=search_term).order_by('-id')
        else:
            matrial_list = Matrial.objects.all().order_by('-id')
        
        context ={"matrial_list" :matrial_list  }
        return render( request , 'matrial_list.html' , context)

class MatrialView(View):
    def get(self, request):
        return render( request , 'matrial_add.html')
    def post(self,request):
        form = MatrialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            response_data = {
            "status": "success",
            "message": "Personal Matrial data submitted successfully!",
            "redirect_url": "/matrial-list/"
            }
            return JsonResponse(response_data)
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(f"{field}: {error}")
            response_data = {
            "message": errors[0],
            "redirect_url": "/matrial-add/"
            }

            return JsonResponse(response_data)


class MatrialUpdateView(View):
    def get(self, request, pk):
        try:
            matrials = Matrial.objects.all().exclude(pk = pk)
            matrial_review = MatrialReview.objects.filter(matrial = pk)
            matrial_list = Matrial.objects.get(pk=pk)
            form = MatrialForm(instance=matrial_list)
            context = {"form": form, "matrial_list": matrial_list , "matrials":matrials , "matrial_review":matrial_review}
            return render(request, 'matrial-details.html', context)
        except Matrial.DoesNotExist:
            return render(request, '404.html')

    
    def post(self, request, pk):
        matrial_list = Matrial.objects.get(pk=pk)
        form = MatrialForm(request.POST, request.FILES, instance=matrial_list)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "success",
                "message": "Matrial data updated successfully!",
                "redirect_url": "/matrial-list/"
            }
            return JsonResponse(response_data)
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(f"{field}: {error}")
            response_data = {
            "status": "error",
            "message": errors[0],
            "redirect_url": f"/matrial-update/{pk}/"  
            }
            return JsonResponse(response_data)


class MatrialDeleteView(View):
    def post(self, request, pk):
        try:
            matrial_list = Matrial.objects.get(pk=pk)
            matrial_list.delete()
            response_data = {
                "status": "success",
                "message": "Matrial data deleted successfully!",
                "redirect_url": "/matrial-list/" 
            }
            return JsonResponse(response_data)
        except Matrial.DoesNotExist:
            response_data = {
                "status": "error",
                "message": "Matrial account does not exist!",
                "redirect_url": "/matrial-list/" 
            }
            return JsonResponse(response_data)

class MatrialReviewView(View):
    def get(self, request ,pk):
        return render( request , 'matrial-review-add.html' , {'pk':pk})
    def post(self,request , pk):
        form = MatrialReviewForm(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            response_data = {
            "status": "success",
            "message": "Matrial review submitted successfully!",
            "redirect_url": f"/matrial-update/{pk}/"
            }
            return JsonResponse(response_data)
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(f"{field}: {error}")
            response_data = {
            "message": errors[0],
            "redirect_url": f"/matrial-review-add/{pk}/"
            }

            return JsonResponse(response_data)