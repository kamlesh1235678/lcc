from django.views import View
from django.http import  JsonResponse
from django.shortcuts import  render
from django.db.models import Q
from contact.models import *
from api.v1.module.forms.contact_forms import *


class ContactListView(View):
    def get(self, request):
        search_term = request.GET.get('search', '')
        if search_term:
            contact_list = Contact.objects.filter(name__icontains=search_term).order_by('-id')
        else:
            contact_list = Contact.objects.all().order_by('-id')
        
        context ={"contact_list" :contact_list  }
        return render( request , 'contact_list.html' , context)

class ContactView(View):
    def get(self, request):
        return render( request , 'contact_add.html')
    def post(self,request):
        form = ContactForm(request.POST, request.FILES)
        # import pdb; pdb.set_trace()
        if form.is_valid():
            form.save()
            response_data = {
            "status": "success",
            "message": "Contact data submitted successfully!",
            "redirect_url": "/contact-list/"
            }
            return JsonResponse(response_data)
        else:
            errors = []
            for field, error_list in form.errors.items():
                for error in error_list:
                    errors.append(f"{field}: {error}")
            response_data = {
            "message": errors[0],
            "redirect_url": "/contact-add/"
            }

            return JsonResponse(response_data)


class ContactUpdateView(View):
    def get(self, request, pk):
        try:
            contact_list = Contact.objects.get(pk=pk)
            form = ContactForm(instance=contact_list)
            context = {"form": form, "contact_list": contact_list}
            return render(request, 'contact-update.html', context)
        except Contact.DoesNotExist:
            return render(request, '404.html')

    
    def post(self, request, pk):
        contact_list = Contact.objects.get(pk=pk)
        form = ContactForm(request.POST, request.FILES, instance=contact_list)
        if form.is_valid():
            form.save()
            response_data = {
                "status": "success",
                "message": "contact data updated successfully!",
                "redirect_url": "/contact-list/"
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
            "redirect_url": f"/contact-update/{pk}/"  
            }
            return JsonResponse(response_data)


class ContactDeleteView(View):
    def post(self, request, pk):
        try:
            contact_list = Contact.objects.get(pk=pk)
            contact_list.delete()
            response_data = {
                "status": "success",
                "message": "contact data deleted successfully!",
                "redirect_url": "/contact-list/" 
            }
            return JsonResponse(response_data)
        except Contact.DoesNotExist:
            response_data = {
                "status": "error",
                "message": "contact account does not exist!",
                "redirect_url": "/contact-list/" 
            }
            return JsonResponse(response_data)

