from . import views 
from django.urls import path

app_name='web'

urlpatterns=[
    path("",views.index,name="index"),
    path("blog_detail",views.blog_detail,name="blog_detail"),
    path("blog",views.blog,name="blog"),
    path("browse_category",views.browse_category,name="browse_category"),

    path("browse_employers_list",views.browse_employers_list,name="browse_employers_list"),
    path("browse_employers",views.browse_employers,name="browse_employers"),
    path("browse_jobs",views.browse_jobs,name="browse_jobs"),
    path("browse_resumes_list",views.browse_resumes_list,name="browse_resumes_list"),
     path("browse_resumes",views.browse_resumes,name="browse_resumes"),
     path("candidate_dashboard",views.candidate_dashboard,name="candidate_dashboard"),
     path("candidate_detail",views.candidate_detail,name="candidate_detail"),
    #  path("contact",views. contact,name=" contact"),
     path('contact/', views.contact, name='contact'),
     path('login', views.login_1, name='login'),
     path('employer_login', views.employer_login, name='employer_login'),
    path("job_search_v1",views.job_search_v1,name="job_search_v1"),
    path('register', views.register_1, name='register'),

    path('employer_register', views.employer_register, name='employer_register'),

    path('post_job', views.post_job, name='post_job'),

       path('logout',views.logout_1,name='logout'),
]