from django.urls import path,include
from .import views
from django.utils.translation import gettext as _
from django.conf.urls.i18n import i18n_patterns
# from django.conf.urls import handler404

app_name = 'main'

urlpatterns = [
	path('',views.HomePageView.as_view(), name='home'),
	# path('about/',views.AboutPageView.as_view(), name='about'),
    path("university/<slug>", views.UniversityDetailView.as_view(), name="university_detail"),
    path("post/<slug>", views.PostDetailView.as_view(), name="post_detail"),
    path("load_more/", views.load_more, name="load_more"),
    path("load_less/", views.load_less, name="load_less"),
    path("country_filter/", views.country_filter, name="country_filter"),
    path("get_message/", views.get_message, name="get_message")
	# path('product/<pk>', views.ProductDetailView.as_view(), name='product_detail'),
	# path('category_delete/<pk>', views.category_delete, name='category_delete'),
	# path('product_delete/<pk>', views.product_delete, name='product_delete'),
	# path('error/', views.ErrorPageView.as_view(), name='error'),
]
# https://programtalk.com/vs2/?source=python%2F3319%2Fdjango-parler%2Fexample%2Farticle%2Fviews.py#

# handler404 = '.views.error_404_view'