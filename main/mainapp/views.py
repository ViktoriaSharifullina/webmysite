from django.shortcuts import render, redirect
from django.views import View
from .forms import ContactForm, PostForm, CommentForm
from .models import *
from .telegram import send_message


def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            forms = Account.objects.last()
            message = "*СООБЩЕНИЕ С САЙТА*:" + "\n" + str({forms})
            send_message(message)
            return redirect('index')
        else:
            """return HttpResponse("Your account is disabled")"""

    form = ContactForm()
    data = {
        'form': form,
    }

    return render(request, "index.html", data)


def mammals(request):
    return render(request, "mammals.html")


def ecoproblems(request):
    return render(request, "ecoproblems.html")


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post.html', context={'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'post_detail.html', context={'post': post})


class PostCreate(View):
    @staticmethod
    def get(request):
        form = PostForm()
        return render(request, 'post_create_form.html', context={'form': form})

    @staticmethod
    def post(request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'post_create_form.html', context={'form': bound_form})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def post__detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    comments = post.comments.filter(active=True)

    if request.method == 'POST' and is_ajax(request):
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

            result = {
                "name": new_comment.name,
                "email": new_comment.email,
                "body": new_comment.body,
                "created": new_comment.created

            }
            return JsonResponse({"result": result}, status=200)
        else:
            errors = comment_form.errors.as_json()
            return JsonResponse({"errors": errors}, status=400)
    else:
        comment_form = CommentForm()
    return render(request,
                  'post_detail.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})
