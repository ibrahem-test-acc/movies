from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from django.urls import reverse_lazy, reverse
from .forms import PostForm, CommentForm
from django.http import HttpResponseRedirect
# import requests
# import json


# movie_response = requests.get(
#     f"https://api.themoviedb.org/3/movie/856?api_key={moviedb_api_key}")

# movie_json = json.loads(movie_response.text)
# for key, value in movie_json.items():

#     print(key, ":", value)
#     movie_response = requests.get(f"{moviedb_base_url}/movie/{movie_id}?api_key={moviedb_api_key}")
# def load_json_for_url(url):
#     response = requests.get(url)
#     return json.loads(response.text)


# moviedb_api_key = "b4067cc44892621e5a29e288523d898b"
# moviedb_base_url = "https://api.themoviedb.org/3/"


# def load_moviedb_info(path):
#     return load_json_for_url(f"{moviedb_base_url}/{path}?api_key={moviedb_api_key}")


# def get_movie_info(movie_id):
#     return load_moviedb_info(f"movie/{movie_id}")


# def get_person_info(person_id):
#     return load_moviedb_info(f"person/{person_id}")


# def MovieDetail(request):
#     response = requests.get(
#         'https://api.themoviedb.org/3/trending/movie/day?api_key=b4067cc44892621e5a29e288523d898b').json()
#     title = get_movie_info(856)['title']
#     print(get_person_info(11614)['name'])
#     print(get_movie_info(856)['title'])

#     return render(request, 'movie_details.html', {'response': response, 'title': title})


def LikeView(request, pk):
    liked = False
    post = get_object_or_404(Post, id=request.POST.get('post_id'))

    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False

    else:
        liked = True
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))


class CommunityView(ListView):
    model = Post
    template_name = 'community.html'
    ordering = ['-Publication_date']


def Home(request):
    return render(request, 'home.html')


def Movies(request):
    return render(request, 'Movies.html')


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        current_post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = current_post.total_likes()
        context['total_likes'] = total_likes
        liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['liked'] = liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('community')


class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'
    success_url = reverse_lazy('community')


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    form_class = PostForm
    success_url = reverse_lazy('community')


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('community')


def CategoryView(request, c):
    category_posts = Post.objects.filter(category=c)
    return render(request, 'categories.html', {'c': c, 'category_posts': category_posts})


# replace('-', ' ')) ==> to replace the ' ' with '-'


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('community')
