# from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from address_book.models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'street_address']

@login_required
def contact_list(request, template_name='address_book/contact_list.html'):
    if request.user.is_superuser:
        contact = Contact.objects.all()
    else:
        contact = Contact.objects.filter(user=request.user)
    data = {}
    data['object_list'] = contact
    return render(request, template_name, data)

@login_required
def contact_create(request, template_name='address_book/contact_form.html'):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save(commit=False)
        contact.user = request.user
        contact.save()
        return redirect('address_book:contact_list')
    return render(request, template_name, {'form':form})

@login_required
def contact_view(request, pk, template_name='address_book/contact_form.html'):
    if request.user.is_superuser:
        contact= get_object_or_404(Contact, pk=pk)
    else:
        contact= get_object_or_404(Contact, pk=pk, user=request.user)
    data = {}
    data['object'] = contact
    data['object_read_only']=True
    return render(request, template_name, data)

@login_required
def contact_update(request, pk, template_name='address_book/contact_form.html'):
    if request.user.is_superuser:
        contact= get_object_or_404(Contact, pk=pk)
    else:
        contact= get_object_or_404(Contact, pk=pk, user=request.user)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        return redirect('address_book:contact_list')
    return render(request, template_name, {'form':form})

@login_required
def contact_delete(request, pk, template_name='address_book/contact_confirm_delete.html'):
    if request.user.is_superuser:
        contact= get_object_or_404(Contact, pk=pk)
    else:
        contact= get_object_or_404(Contact, pk=pk, user=request.user)
    if request.method=='POST':
        contact.delete()
        return redirect('address_book:contact_list')
    return render(request, template_name, {'object':contact})
