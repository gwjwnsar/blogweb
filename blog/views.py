from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.
@login_required
def post_list_view(request):
    list_objects = Post.published.all()
    paginator = Paginator(list_objects, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html', {'posts':posts})

@login_required
def post_detail_view(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='published', publish__year=year, publish__month=month, publish__day=day)
    return render(request, 'blog/post/detail.html', {'post':post})

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            slug = form.cleaned_data['slug']
            content = form.cleaned_data['content']
            publish = form.cleaned_data['publish']
            status = form.cleaned_data['status']
            p = Post(title=title, slug=slug, author=request.user, content=content, publish=publish, status=status)
            p.save()
            return HttpResponseRedirect('/')

    else:
        form = PostForm()
    return render(request, 'blog/post/create.html', {'form':form})
