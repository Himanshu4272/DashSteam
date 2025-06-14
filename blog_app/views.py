from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from .models import Post, Rating, Contact, Comment
from django.contrib.auth.models import User
from .forms import PostForm, ContactForm, CommentForm
from django.core.paginator import Paginator

def blog_list(request):
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 6)  # 6 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    return render(request, 'blog_app/blog_list.html', {'posts': posts})

def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    user_rating = None
    if request.user.is_authenticated:
        user_rating = Rating.objects.filter(user=request.user, post=post).first()
    comments = post.comments.select_related('user').order_by('-created_at')
    if request.method == 'POST' and request.user.is_authenticated:
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            messages.success(request, 'Comment added!')
            return redirect('blog_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blog_app/blog_detail.html', {
        'post': post,
        'user_rating': user_rating,
        'comments': comments,
        'comment_form': comment_form
    })

@login_required
def blog_create(request):
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog_app/blog_form.html', {'form': form})

@login_required
def blog_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('blog_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog_app/blog_form.html', {'form': form, 'edit': True})

@login_required
def blog_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if not request.user.is_staff:
        return HttpResponseForbidden()
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('blog_list')
    return render(request, 'blog_app/blog_confirm_delete.html', {'post': post})

@login_required
def rate_post(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        rating_value = int(request.POST.get('rating', 0))
        if 1 <= rating_value <= 5:
            rating, created = Rating.objects.update_or_create(
                user=request.user, post=post,
                defaults={'rating': rating_value}
            )
            return JsonResponse({'success': True, 'average': post.average_rating()})
    return JsonResponse({'success': False})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'blog_app/contact.html', {'form': form})

@login_required
def profile(request):
    user = request.user
    posts = Post.objects.filter(author=user)
    ratings = Rating.objects.filter(user=user)
    return render(request, 'blog_app/profile.html', {'user': user, 'posts': posts, 'ratings': ratings})
