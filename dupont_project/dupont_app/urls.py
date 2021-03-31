from django.urls import path
from . import views
from dupont_project.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
	path('', views.index, name='index'),
	path('index', views.index, name='index'),
	path('model_prediction', views.model_prediction, name='model_prediction'),
	path('ml_model_refrence', views.ml_model_refrence, name='ml_model_refrence'),
	path('research_update', views.research_update, name='research_update'),
	path('contact_us', views.contact_us, name='contact_us'),
	path('save_contact', views.save_contact, name='save_contact'),
	path('image_pred', views.image_pred, name='image_pred'),
]

if DEBUG:
	urlpatterns += [
		*static(STATIC_URL, document_root = STATIC_ROOT),
		*static(MEDIA_URL, document_root = MEDIA_ROOT)
	]