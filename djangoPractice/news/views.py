from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from .utils import MyMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import login, logout

from .forms import NewsForm, UserRegisterForm, UserLoginForm
from .models import News, Category


# to register func
# mail=send_mail('Confirm mail', 'You register at Yiknok site please confirm your email','for_smtptest@ukr.net',[form.cleaned_data['email']], fail_silently=False)
#             if mail:
#                 messages.success(request, 'Register success, confirm your email')
#                 return redirect('home')
#             else:
#                 messages.error(request,'error sending message to email')
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Register success')
            return redirect('home')
        else:
            messages.error(request, 'Register failed')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


class HomeNews(MyMixin, ListView):
    model = News
    template_name = 'news/class_index.html'
    context_object_name = 'news'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper('Home page')
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True).select_related('category')


class CategoryNews(MyMixin, ListView):
    model = News
    template_name = 'news/class_category.html'
    context_object_name = 'news'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_upper(Category.objects.get(pk=self.kwargs['category_id']))
        return context

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')


class ViewNews(DeleteView):
    model = News
    context_object_name = 'news_item'
    # template_name = 'news/news_confirm_delete.html'
    # pk_url_kwarg = 'news_id'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    # success_url = reverse_lazy('home')
    # login_url = '/admin/'

# def index(request):
#     news = News.objects.all()
#     context = {
#         'news': news,
#         'title': 'News list',
#     }
#     return render(request, 'news/index.html', context)


# def get_category(request, category_id):
#     news = News.objects.filter(category_id=category_id)
#     category = Category.objects.get(pk=category_id)
#     return render(request, 'news/category.html', {'news': news, 'category': category})


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     return render(request, 'news/view_news.html', {'news_item': news_item})


# def add_news(request):
#     if request.method == 'POST':
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()
#     return render(request, 'news/add_news.html', {'form': form})
