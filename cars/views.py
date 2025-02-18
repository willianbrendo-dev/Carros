from django.shortcuts import render, redirect
from cars.models import Car
from django.urls import reverse_lazy
from cars.forms import CarModelForm
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DeleteView


#function base view
def cars_view(request):
    cars = Car.objects.all().order_by('model')
    search = request.GET.get('search')
    if search:
        cars = cars.filter(model__icontains=search).order_by('model')

    return render(
        request,
        'cars.html', 
        {'cars': cars}
    )

#class basic view
class CarsView(View):

    def get(self, request):
        cars = Car.objects.all().order_by('model')
        search = request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search).order_by('model')

        return render(
            request,
            'cars.html', 
            {'cars': cars}
    )


#class basic view genérica
class CarListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'

    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__icontains=search).order_by('model')
        return cars


#func basic view
def new_car_view(request):
    if request.method == 'POST':
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
    else:
        new_car_form = CarModelForm()
    return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )

#class basic view
class NewCarView(View):

    def get(self, request):
        new_car_form = CarModelForm()
        return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )

    def post(self, request):
        new_car_form = CarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        
        return render(
        request,
        'new_car.html',
        {'new_car_form': new_car_form}
    )


#class basic CreatView generica
@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreatView(CreateView):
    model = Car
    form_class = CarModelForm
    template_name = 'new_car.html'
    success_url = '/cars/'


class CarDatailView(DeleteView):
    model = Car
    template_name = 'car_detail.html'



class CarUpdateView(UpdateView):
    model = Car
    form_class = CarModelForm
    template_name = 'car_update.html'


    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = '/cars/'