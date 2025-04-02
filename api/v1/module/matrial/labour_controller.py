from django.views import View
from django.http import  JsonResponse
from django.shortcuts import  render
from django.db.models import Q
from labour.models import *
from api.v1.module.forms.labour_forms import *


class LabourListView(View):
    def get(self, request):
        search_term = request.GET.get('search', '')
        if search_term:
            labour_list = Labour.objects.filter(name__icontains=search_term).order_by('-id')
        else:
            labour_list = Labour.objects.all().order_by('-id')
        
        context ={"labour_list" :labour_list  }
        return render( request , 'labour_list.html' , context)

class LabourView(View):
    def get(self, request):
        return render( request , 'labour_add.html')
    def post(self,request):
        form = LabourForm(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            response_data = {
            "status": "success",
            "message": "Labour data submitted successfully!",
            "redirect_url": "/labour-list/"
            }
            return JsonResponse(response_data)
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(f"{field}: {error}")
            response_data = {
            "message": errors[0],
            "redirect_url": "/labour-add/"
            }

            return JsonResponse(response_data)


class LabourUpdateView(View):
    def get(self, request, pk):
        try:
            labour_list = Labour.objects.get(pk=pk)
            labours =  Labour.objects.all().exclude(pk = pk)
            labour_review = LabourReview.objects.filter(labour=pk)
            form = LabourForm(instance=labour_list)
            context = {"form": form, "labour_list": labour_list ,"labour_review":labour_review ,"labours":labours}
            return render(request, 'labour-details.html', context)
        except Labour.DoesNotExist:
            return render(request, '404.html')

    
    def post(self, request, pk):
        labour_list = Labour.objects.get(pk=pk)
        form = LabourForm(request.POST, request.FILES, instance=labour_list)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "success",
                "message": "Labour data updated successfully!",
                "redirect_url": "/labour-list/"
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
            "redirect_url": f"/labour-update/{pk}/"  
            }
            return JsonResponse(response_data)


class LabourDeleteView(View):
    def post(self, request, pk):
        try:
            labour_list = Labour.objects.get(pk=pk)
            labour_list.delete()
            response_data = {
                "status": "success",
                "message": "Labour data deleted successfully!",
                "redirect_url": "/labour-list/" 
            }
            return JsonResponse(response_data)
        except Labour.DoesNotExist:
            response_data = {
                "status": "error",
                "message": "Labour account does not exist!",
                "redirect_url": "/labour-list/" 
            }
            return JsonResponse(response_data)

class FilterLabour(View):
    def get(self, request):
        address = request.GET.get('address', '')
        name = request.GET.get('name', '')
        mobile = request.GET.get('mobile', '')
        expertise_title = request.GET.get('expertise_title', '')
        
        filters = Q()
        if address:
            filters &= Q(address__icontains=address)
        if name:
            filters &= Q(name__icontains=name)
        if mobile:
            filters &= Q(mobile__icontains=mobile)
        if expertise_title:
            filters &= Q(expertise_title__icontains=expertise_title)
        
        labour_list = Labour.objects.filter(filters)
        context = {
            "labour_list":labour_list
        }
        
        return render(request , 'labour_list.html' , context)
    



class LabourReviewView(View):
    def get(self, request ,pk):
        return render( request , 'labour-review-add.html' , {'pk':pk})
    def post(self,request , pk):
        form = LabourReviewForm(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            response_data = {
            "status": "success",
            "message": "Labour Review submitted successfully!",
            "redirect_url": f"/labour-update/{pk}/"
            }
            return JsonResponse(response_data)
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(f"{field}: {error}")
            response_data = {
            "message": errors[0],
            "redirect_url": f"/labour-review-add/{pk}/"
            }

            return JsonResponse(response_data)