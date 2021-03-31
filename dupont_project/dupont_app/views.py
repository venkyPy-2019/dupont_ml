import urllib
import json

from django.shortcuts import render, redirect
from .models import researchUpdate, MachineLearningModelReference, Contact, ImagePred
from .forms import ContactForm, ImageForm
from django_countries import countries
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
	return render(request, 'index.html')

@login_required
def model_prediction(request):
	image = ImageForm()
	return render(request, 'model-prediction.html', {'upload_form': image})

@login_required
def ml_model_refrence(request):
	references = MachineLearningModelReference.objects.all()
	return render(request, 'machine-learning-model-reference.html', {'references':references})

@login_required
def research_update(request):
	blogs = researchUpdate.objects.all()
	return render(request, 'research-update.html',{'blogs':blogs})

def contact_us(request):
	form = ContactForm()
	context = {
		'form': form
	}
	return render(request, 'contact.html', context)	

def save_contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)		
		if form.is_valid():
			''' Begin reCAPTCHA validation '''
			recaptcha_response = request.POST.get('g-recaptcha-response')
			url= 'https://www.google.com/recaptcha/api/siteverify'
			values = {
				'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
				'response': recaptcha_response
			}
			data = urllib.parse.urlencode(values).encode()
			req = urllib.request.Request(url, data=data)
			response = urllib.request.urlopen(req)
			result = json.loads(response.read().decode())
			''' End reCAPTCHA validation '''
			if result['success']:
				post = form.save(commit=False)
				form.save()
				subject = 'DUPONT - Contact Us'
				email_d = {
					'first_name': request.POST.get('first_name'),
					'last_name': request.POST.get('last_name'),
					'company_name': request.POST.get('company_name'),
					'country': request.POST.get('country'),
					'phone_no': request.POST.get('phone_no'),
					'contact_prefer': request.POST.get('contact_prefer'),
					'question': request.POST.get('question'),
					'receive_alerts': request.POST.get('receive_alerts'),
				}
				html_message = render_to_string('contact_mail_template.html', {'context': email_d})
				plain_message = strip_tags(html_message)
				# message = f'Hi {request.POST.get('first_name')} {request.POST.get('last_name')}, thank you for contacting us. we will get back to you soon.'
				email_from = settings.EMAIL_HOST_USER
				reciepient_list = [request.POST.get('email_address')]
				send_mail(subject, plain_message, email_from, reciepient_list, html_message=html_message)	
				messages.success(request, 'Query Sent Successfully!')				
			else:
				messages.error(request, 'Invalid reCAPTCHA. Please try again.')
		return redirect('contact_us')												
	else:
		form = ContactForm()
		context = {
			'form': form
		}
		return render(request, 'contact.html', context)

@csrf_exempt
def image_pred(request):
	print(request.POST)
	exit()
	image = ImageForm()
	if request.method == 'POST':
		image = ImageForm(request.POST, request.FILES)
		if image.is_valid():
			image.save(commit=False)
			image.created_by = request.user
			image.save()
			messages.error(request, 'Upload is Successfully!')
			return HttpResponse(messages)
		else:
			messages.error(request, 'Upload is failed, try again!')
			return HttpResponse(messages)
	else:
		messages.error(request, 'Something went wrong!')
		return HttpResponse(messages)


