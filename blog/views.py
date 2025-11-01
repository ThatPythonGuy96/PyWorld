from django.shortcuts import render, redirect
from django.views import generic
from .models import Blog
from .forms import BlogForm

class BlogHomeView(generic.View):
    template_name = "home.html"

    def get(self, request):
        news = Blog.objects.all().order_by('-created')[:3]
        popular = Blog.objects.all().order_by('-view')
        context={
            'news': news,
            'popular': popular
        }
        return render(request, self.template_name, context)
    
class BlogDetailView(generic.DetailView):
    template_name = "detail.html"

    def get(self, request, id):
        post = Blog.objects.get(id=id)
        post.view =+ 1
        post.save()
        context={
            'post': post,
        }
        return render(request, self.template_name, context)

class CreateBlogView(generic.View):
    template_name = "create.html"

    def get(self, request):
        form = BlogForm()
        context={
            'form':form,
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            print(instance.title)
            blog = Blog.objects.get(title=instance)
            return redirect(blog.get_absolute_url())
        else:
            print(form.errors)
        context = {'form': form}
        return render(request, self.template_name, context)