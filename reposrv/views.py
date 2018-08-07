from django.shortcuts import render

# Create your views here.

from .models import Customer, Address, Blockchain, Watchlist, Log, Operations

def index(request):
    '''
    Функция отображения для домашней страницы сайта.
    '''
    # Генерация "количеств" некоторых главных объектов
    num_customers=Customer.objects.all().count()
    num_addresses=Address.objects.all().count()
    num_blockchains=Blockchain.objects.all().count()
    num_watchlists=Watchlist.objects.count()
    num_logs=Log.objects.all().count()
    num_operations=Operations.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1
    
    # Отрисовка HTML-шаблона index.html с данными внутри 
    # переменной контекста context
    return render(
        request,
        'index.html',
        context={'num_customers':num_customers,'num_addresses':num_addresses,'num_blockchains':num_blockchains,'num_watchlists':num_watchlists,'num_logs':num_logs,'num_operations':num_operations,'num_visits':num_visits},
    )

from django.views import generic

class AddressListView(generic.ListView):
    model = Address
    paginate_by = 10

class AddressDetailView(generic.DetailView):
    model = Address

class BlockchainListView(generic.ListView):
    model = Blockchain
    def get_object_count(self):
        return Address.objects.filter(blockchain=self.id).count()
    paginate_by = 10

class BlockchainDetailView(generic.DetailView):
    model = Blockchain

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class AddressCreate(CreateView):
    model = Address
    fields = '__all__'


class AddressUpdate(UpdateView):
    model = Address
    fields = ['key','customer','blockchain','addrstatus']

class AddressDelete(DeleteView):
    model = Address
    success_url = reverse_lazy('addresses')