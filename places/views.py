from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Place
from .forms import PlaceForm


def index(request):
    return render(request, 'places/index.html', {'title': 'Домашняя страница'})


class PlaceListView(ListView):
    model = Place
    template_name = 'places/places.html'
    context_object_name = 'my_places'

    def get_queryset(self):
        return Place.objects.filter(user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Мои воспоминания'
        return context


class PlaceCreateView(CreateView):
    form_class = PlaceForm
    template_name = 'places/add_place.html'
    success_url = '/places'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Добавить воспоминание о месте'
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)
