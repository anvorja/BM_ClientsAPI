from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Client
from .forms import ClientForm
from .serializers import ClienteSerializer
from rest_framework.decorators import api_view, action
from rest_framework import generics, viewsets, status


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {"form": UserCreationForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('clients')
            except IntegrityError:
                return render(request, 'signup.html', {"form": UserCreationForm, "error": "Username already exists."})

        return render(request, 'signup.html', {"form": UserCreationForm, "error": "Passwords did not match."})


@login_required
def clients(request):
    clients = Client.objects.filter(user=request.user)
    return render(request, 'clients.html', {"clients": clients})


@login_required
def create_client(request):
    if request.method == "GET":
        return render(request, 'create_client.html', {"form": ClientForm})
    else:
        try:
            form = ClientForm(request.POST)
            new_client = form.save(commit=False)
            new_client.user = request.user
            new_client.save()
            return redirect('clients')
        except ValueError:
            return render(request, 'create_client.html', {"form": ClientForm, "error": "Error al crear cliente."})


def home(request):
    return render(request, 'home.html')


@login_required
def signout(request):
    logout(request)
    return redirect('home')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {"form": AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html',
                          {"form": AuthenticationForm,
                           "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('clients')


@login_required
def client_detail(request, client_id):
    if request.method == 'GET':
        client = get_object_or_404(Client, pk=client_id, user=request.user)
        form = ClientForm(instance=client)
        return render(request, 'client_detail.html', {'client': client, 'form': form})
    else:
        try:
            client = get_object_or_404(Client, pk=client_id, user=request.user)
            form = ClientForm(request.POST, instance=client)
            form.save()
            return redirect('clients')
        except ValueError:
            return render(request, 'client_detail.html',
                          {'client': client, 'form': form, 'error': 'Error actualizando cliente.'})


@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id, user=request.user)
    if request.method == 'POST':
        client.delete()
        return redirect('clients')


@login_required
def prioritary_clients(request):
    clientePrioritario = Client.objects.filter(user=request.user, prioritario=True)
    return render(request, 'clients_prioritary.html', {"clients": clientePrioritario})


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClienteSerializer


# class ClientList(generics.ListCreateAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClienteSerializer


def get_clients_as_json(request):
    clients = Client.objects.all()
    serializer = ClienteSerializer(clients, many=True)
    return JsonResponse(serializer.data, safe=False)
