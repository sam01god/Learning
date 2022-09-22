from django.urls import path, include
from . import views
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns = [

# Shared URLs
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('services/', views.services, name='services'),
path('contact/', views.contact, name='contact'),
path('lsign/', views.LearnerSignUpView.as_view(), name='lsign'),
path('tsign/', views.TeacherSignUpView.as_view(), name='tsign'),
path('login_form/', views.login_form, name='login_form'),
path('login/', views.loginView, name='login'),
path('logout/', views.logoutView, name='logout'),


# Admin URLs
path('dashboard/', views.dashboard, name='dashboard'),
path('course/', views.course, name='course'),
path('courselist/', CourcesList.as_view(), name='courcelist'),
path('studentlist/', StudentList.as_view(), name='studentlist'),
path('studentdetail/<int:id>', views.studentdetail, name='studentdetail'),
path('teacherlist/', TeacherList.as_view(), name='teacherlist'),
path('teacherdetail/<int:id>', views.teacherdetail, name='teacherdetail'),
path('isign/', views.InstructorSignUpView.as_view(), name='isign'),
path('addlearner/', views.AdminLearner.as_view(), name='addlearner'),
path('apost/', views.AdminCreatePost.as_view(), name='apost'),
path('alpost/', views.AdminListTise.as_view(), name='alpost'),
path('alistalltise/', views.ListAllTise.as_view(), name='alistalltise'),
path('adpost/<int:pk>', views.ADeletePost.as_view(), name='adpost'),
path('aluser/', views.ListUserView.as_view(), name='aluser'),
path('aduser/<int:pk>', views.ADeleteuser.as_view(), name='aduser'),
path('create_user_form/', views.create_user_form, name='create_user_form'),
path('create_user/', views.create_user, name='create_user'),
path('acreate_profile/', views.acreate_profile, name='acreate_profile'),
path('auser_profile/', views.auser_profile, name='auser_profile'),
path('chat-admin/', views.homepage_admin, name="chat-admin"),


# Instructor URLs
path('instructor/', views.home_instructor, name='instructor'),
path('inscourselist/', InsCourcesList.as_view(), name='inscourcelist'),
path('quiz_add/', views.QuizCreateView.as_view(), name='quiz_add'),
path('question_add/<int:pk>', views.question_add, name='question_add'),
path('quiz/<int:quiz_pk>/<int:question_pk>/', views.question_change, name='question_change'),
path('llist_quiz/', views.QuizListView.as_view(), name='quiz_change_list'),
path('quiz/<int:quiz_pk>/question/<int:question_pk>/delete/', views.QuestionDeleteView.as_view(), name='question_delete'),
path('quiz/<int:pk>/results/', views.QuizResultsView.as_view(), name='quiz_results'),
path('quiz/<int:pk>/delete/', views.QuizDeleteView.as_view(), name='quiz_delete'),
path('quizupdate/<int:pk>/', views.QuizUpdateView.as_view(), name='quiz_change'),
path('ipost/', views.CreatePost.as_view(), name='ipost'),
path('llchat/', views.TiseList.as_view(), name='llchat'),
path('user_profile/', views.user_profile, name='user_profile'),
path('create_profile/', views.create_profile, name='create_profile'),
path('tutorial/', views.tutorial, name='tutorial'),
path('post/',views.publish_tutorial,name='publish_tutorial'),
path('itutorial/',views.itutorial,name='itutorial'),
path('itutorials/<int:pk>/', views.ITutorialDetail.as_view(), name = "itutorial-detail"),
path('listnotes/', views.LNotesList.as_view(), name='lnotes'),
path('iadd_notes/', views.iadd_notes, name='iadd_notes'),
path('publish_notes/', views.publish_notes, name='publish_notes'),
path('update_file/<int:pk>', views.update_file, name='update_file'),
path('chat-instructor/', views.homepage_instructor, name="chat-instructor"),

# Chat App Url
path('<int:pk>/', views.chatroom, name='chatroom'),
path("ajax/<int:pk>/",views.ajax_load_messages,name='chatroom-ajax',),

# Learner URl's
path('learner/',views.home_learner,name='learner'),
path('learncourselist/', LearnCourcesList.as_view(), name='learncourcelist'),
path('ltutorial/',views.ltutorial,name='ltutorial'),
path('llistnotes/', views.LLNotesList.as_view(), name='llnotes'),
path('ilchat/', views.ITiseList.as_view(), name='ilchat'),
path('luser_profile/', views.luser_profile, name='luser_profile'),
path('lcreate_profile/', views.lcreate_profile, name='lcreate_profile'),
path('tutorials/<int:pk>/', views.LTutorialDetail.as_view(), name = "tutorial-detail"),
path('interests/', views.LearnerInterestsView.as_view(), name='interests'),
path('learner_quiz/', views.LQuizListView.as_view(), name='lquiz_list'),
path('taken/', views.TakenQuizListView.as_view(), name='taken_quiz_list'),
path('taken_question/<int:id>', views.quizquestion, name='taken_question'),
path('quiz/<int:pk>/', views.take_quiz, name='take_quiz'),
path('chat-student/', views.homepage_student, name="chat-student"),

#### Blog
path('add_blog/', views.add_blog, name='add_blog'),
path('publish_blog/', views.publish_blog, name='publish_blog'),
path('list_blog/', BlogList.as_view(), name='list_blog'),
path('update_blog/<int:pk>', views.update_blog, name='update_blog'),
path('delete_blog/<int:pk>', views.delete_blog, name='delete_blog'),
path('detail_blog/<int:id>', views.detail_blog, name='detail_blog'),
]

