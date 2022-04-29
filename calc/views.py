from pyexpat.errors import messages
from tkinter import N
from django.http import HttpResponse
# from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from calc.forms import OldTracktorForm

from .models import Stoke, Index, OldTractor, NewUserForm, ContactEnquiry, \
    Gallery_image


@login_required(login_url=reverse_lazy('calc:login'))
def stoke(request):
    return render(request, 'stoke.html')


def WishList(request):
    return render(request, 'Wishlist.html')


def Gallery(request):
    return render(request, 'gallery.html')


def Profile(request):
    return render(request, 'profile.html')


def Happy_customer(request):
    return render(request, "Customer.html")


def Contact_us(request):
    return render(request, 'Contactus.html')


def SaveCustomer(request):
    # import pdb;
    # pdb.set_trace()

    if request.method == "POST":
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        village = request.POST.get('village')
        description = request.POST.get('name')
        cd = ContactEnquiry(name=name, Phone_number=contact,
                            Village_name=village,
                            Description=description, )
        cd.save()
        messages.success(request, "Form Submit successful.")
        return redirect("index")
    return render(request, 'Contactus.html')


def Our_Team(request):
    return render(request, 'OurTeam.html')


def Sold(request):
    return render(request, 'Sold.html')

def Add_Tractor(request):
    return render(request, 'addtractor.html')

# 
@login_required(login_url = '/admin_login')
def Add_Tractor(request):
    # import pdb; pdb.set_trace()

    Add_Tractor = OldTracktorForm()
    if request.method == 'POST':
        Add_Tractor = OldTracktorForm(request.POST, request.FILES)
        if Add_Tractor.is_valid():
            Add_Tractor.save()
            messages.success(request, "Add Tractor Success.")
            
            return redirect('index')
        messages.error(request,
                       "Not Completed Form")
        return render(request, 'index.html')
        
    else:
        return render(request, 'addtractor.html', {'form': Add_Tractor})

        


@login_required(login_url=reverse_lazy('calc:login'))
def inspection(request, pk):
    data = OldTractor.objects.get(id=pk)
    return render(request, 'inspection.html', {"inspection": data})


@login_required(login_url=reverse_lazy('calc:login'))
def oldtractor(request):
    dest1 = OldTractor.objects.all()
    return render(request, "oldtractor.html", {"oldtractor": dest1})


@login_required(login_url=reverse_lazy('calc:login'))
def stoke(request):
    dest1 = Stoke.objects.all()
    return render(request, "stoke.html", {"stokes": dest1})


def Gallery(request):
    dest1 = Gallery_image.objects.all()
    return render(request, "gallery.html", {"gallery": dest1})


def index(request):
    dest1 = Index.objects.all()
    return render(request, "index.html", {"index": dest1})


@login_required(login_url=reverse_lazy('calc:login'))
def about(request):
    dest1 = Index.objects.all()
    return render(request, "about.html", {"about": dest1})


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("index")
        messages.error(request,
                       "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="register.html",
                  context={"register_form": form})


def login_request(request):
    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # request.session['user'] = user.username
        if user is not None:
            login(request, user)
            messages.success(request,
                             f"you are successfully logging {username}.")
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password.")

    return render(request=request, template_name="login.html")

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            if request.user.is_superuser:
                return redirect("addtractor")
            else:
                return HttpResponse(" You are not an admin")
        else:
            alert = True
            return render(request, "admin_login.html", {'alert':alert})
    return render(request, "admin_login.html")






def logout_user(request):
    logout(request)
    messages.success(request, f" Logout Successfully !!")
    return redirect('index')


def biditem(request):
    # import pdb;
    # pdb.set_trace()
    id = request.GET['id']
    item = OldTractor.objects.get(id=id)
    lstatus = "live"

    if item.status == lstatus:
        return render(request, "biditem.html", {'item': item})
    else:
        return redirect("home")

# def validate(request):
#     value = request.GET.get('bidrs')
#
#     iid = request.GET.get('iid')
#     # print (iid)
#         bidder = request.user
#     bidderEmail = bidder.email
#     # print (bidder.id)
#     item_obj = OldTractor.objects.get(id=iid)
#     itemownerEmail = item_obj.ownermail
#
#     if bidderEmail == itemownerEmail:
#         return render(request, "notification.html")
#     else:
#         mail = item_obj.ownermail
#         subject = "Online Bidding"
#         msg = "Congratulations your item is bidded by " + bidder.email + "
#         , By INR rs = " + value + ". Contact your buyer by email Thank You for
#         using our app."
#         to = mail
#         # res     = send_mail(subject, msg, "bidmafia007@gmail.com", [to])
#
#         OldTractor.objects.filter(id=iid).update(currentPrice=value)
#         OldTractor.objects.filter(id=iid).update(highest_bidder=bidder.id)
#         return redirect("home")
