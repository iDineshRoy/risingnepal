from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from .forms import DocumentForm, PostForm, ImageForm, UpdatePostForm, NewCategoryForm
from .models import Post, FeaturedPost, Images, Category
from taggit.models import Tag
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db.models import Q
from datetime import datetime
from unidecode import unidecode
import functools
import operator
from django.http import HttpResponse

# from pages.views import get_pages

def get_category():
    cat = get_list_or_404(Category)
    print("This is cat:"+cat)
    if cat is None:
        cat = ""
    return cat

def get_recent():
    return get_list_or_404(Post.objects.order_by('-id')[:8])

def get_suggestions(slug):
    post = get_object_or_404(Post, slug=slug)
    tag =  post.tags.all()
    qset = functools.reduce(operator.__and__, [
        Q(tags__name__iexact=q.name) &
        Q(status__iexact='Published') 
        for q in tag])
    suggestions = Post.objects.filter(qset).distinct().exclude(slug=slug).order_by('-id')[:4]
    return suggestions

def paginate(request, posts):
    paginator = Paginator(posts, 3)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        obj = paginator.page(page)
    except(EmptyPage, InvalidPage):
        obj = paginator.page(paginator.num_pages)
    return obj

def posts(request):
    context = {}
    try:
        # qset = functools.reduce(operator.__and__, [
        #     Q(status__iexact='Published')
        #     ])
        posts = Post.objects.all().order_by('-id')
        
        if posts is not None:
            context['posts'] = paginate(request, posts)
        else:
            context['posts'] = paginate(request, {})
        date = datetime.now()
        obj2 = FeaturedPost.objects.filter(
            Q(startdate__lte=date)&
            Q(enddate__gte=date)
        )
        context['featured'] =obj2
        context['recent'] = get_recent()
    except:
        pass
    return render(request, 'post_list.html', context)

def showpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context =  { 'post': post }
    context['suggestions'] = get_suggestions(post.slug)
    return render(request, 'post.html', context)

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DocumentForm()
    return render(request, 'file_upload.html', {
        'form': form
    })

@login_required
def create_post(request):
    posts = Post.objects.all()
    common_tags = Post.tags.most_common()[:4]
    form = PostForm(request.POST, request.FILES)
    form_image = ImageForm(request.POST)
    if form.is_valid() and form_image.is_valid():
        print("Now validated")
        newpost = form.save(commit=False)
        newpost.slug = slugify(unidecode(newpost.title))
        newpost.author = request.user
        print(newpost.slug)
        newpost.save()
        form.save_m2m()
        files = request.FILES.getlist('image')
        for f in files:
            instance = Images(image=f)
            instance.post = newpost
            print("Saving multiple images")
            instance.save()
        return redirect('/')
    
    context = {
        'posts': posts,
        'common_tags':common_tags, 
        'form':form,
        'form_image':form_image
    }
    # context['menu'] = get_category()
    # context['pages'] = get_pages()
    return render(request, 'newpost.html',context)

def create_category(request):
    form = NewCategoryForm(request.POST)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.slug = slugify(unidecode(obj.name))
        obj.save()
        return redirect('/')
    context = { 'form': form }
    context['menu'] = get_category()
    # context['pages'] = get_pages()
    return render(request, 'newcategory.html', context)

def update_category(request, slug):
    obj = Category.objects.get(slug=slug)
    form = NewCategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.slug = slugify(unidecode(obj.name))
        obj.save()
        return redirect('/')
    context = { 'form': form }
    context['menu'] = get_category()
    # context['pages'] = get_pages()
    return render(request, 'newcategory.html', context)

def all_categories(request):
    obj = get_list_or_404(Category)
    context = { 'categories':obj }
    context['menu'] = get_category()
    # context['pages'] = get_pages()
    return render(request, 'categories.html', context)

def show_post_category(request, slug):
    cat = get_object_or_404(Category, slug=slug)
    posts = get_list_or_404(Post, category=cat)
    context = {}
    context['menu'] = get_category()
    # context['pages'] = get_pages()
    context['posts'] = paginate(request, posts)
    return render(request, 'post.html', context)

def tagged(request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    posts = get_list_or_404(Post, tags=tag)
    context = {
        'tag': tag,
    }
    # context['menu'] = get_category()
    context['recent'] = get_recent()
    # context['pages'] = get_pages()
    context['posts'] = paginate(request, posts)
    context['suggestions'] = get_suggestions(posts[0].slug)
    return render(request, 'post_list.html', context)

@login_required
def update_post(request, slug):
    post = Post.objects.get(slug=slug)
    images = Images.objects.filter(post=post)
    form_image = ImageForm(request.POST or None)
    form = UpdatePostForm(request.POST or None, request.FILES or None, instance=post)
    if form.is_valid():
        obj = form.save(commit=False)
        s = request.POST['title']
        obj.slug = slugify(unidecode(s))
        obj.save()
        form.save_m2m()
        return redirect('/blog/post/'+str(obj.slug))
    if(form_image.is_valid()):
        files = request.FILES.getlist('image')
        print(files)
        for f in files:
            instance = Images(image=f)
            instance.post = post
            instance.save()
        return redirect("/")
    context = {"title": "Update Post", "form":form,'images':images, 'form_image':form_image}
    # context['menu'] = get_category()
    # context['pages'] = get_pages()
    return render(request, 'newpost.html', context)

def edit_about(request):
    # try
    # obj = get_object_or_404(OtherDetails, id=1)
    pass