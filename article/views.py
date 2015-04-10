from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response, redirect
from article.models import Article,Comments
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import Http404
from article.forms import CommentForm
from django.core.context_processors import csrf
from django.core.paginator import Paginator
from django.contrib import auth

# Create your views here.

def articles(request, page_number=1):
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 3)


    return render_to_response('articles.html', {'articles': current_page.page(page_number), 'username': auth.get_user(request).username })

def article(request, article_id = 1):
    comment_from = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id = article_id)
    args['comments'] = Comments.objects.filter(comments_acticle_id  = article_id)
    args['form']= comment_from
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html',args)

def addlike(request, article_id = 1):
    try:
        if article_id in request.COOKIES:
            redirect("/")
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes +=1
            article.save()
            response = redirect("/")
            response.set_cookie(article_id,"test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')

def addcomment(request, article_id):
    if request.POST and ("pause") not in request.session:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_acticle = Article.objects.get(id = article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True

    return redirect("/get/%s" % article_id)




