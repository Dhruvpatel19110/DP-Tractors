from pyexpat.errors import messages
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

# def Add_Tractor(request):
#     if request.method == 'POST':
#          form = OldTracktorForm(request.POST)
#         # form = OldTracktorForm(data=request.POST, files=request.FILES)
   
#     if form.is_valid():
#         user = form.save()
#         form.save()
        
#         return redirect("index")
#     else:
#         form = OldTracktorForm()
#         return render(request, 'addtractor.html', {'form': form})
        # return render(request, 'addtractor.html')

        # mimg = request.FILES.get('Main_image')
        # Tname = request.POST.get('TAname')
        # HP = request.POST.get('HAP')
        # MF = request.POST.get('MAF')
        # RN = request.POST.get('RAN')
        # RC = request.POST.get('RAC')
        # EXPRI = request.POST.get('EAXPRI')
        # Hour = request.POST.get('HAour')
        # RY = request.POST.get('RAY')
        # DET = request.POST.get('DAET')
        # RTON = request.POST.get('RATON')
        # ONA = request.POST.get('OANA')
        # VEM = request.POST.get('VAEM')
        # CN = request.POST.get('CAOL')
        # EN = request.POST.get('EAN')
        # RCS = request.POST.get('RACS')
        # CAP = request.POST.get('CAAP')
        # TH = request.POST.get('TAH')
        # RSP = request.FILES.get('RAP')
        # LP = request.FILES.get('LAP')
        # MP = request.FILES.get('MAP')
        # BP = request.FILES.get('BAP')
        # TP1 = request.FILES.get('TAP1')
        # TL1 = request.POST.get('TAL1')
        # TY2 = request.POST.get('TAY2')
        # TL2 = request.POST.get('TAL2')
        # TY3 = request.POST.get('TAY3')
        # TL3 = request.POST.get('TAL3')
        # TL4 = request.FILES.get('TAL4')
        # EP = request.POST.get('EAP')
        # EP1 = request.POST.get('EAP1')
        # Video = request.POST.get('VAideo')
        # MPri = request.POST.get('MAPri')
      
        # item = OldTractor(upload=mimg,name=Tname, HP=HP, Manufacturingyear=MF,
        #                   Regno=RN, RC=RC, price=EXPRI,
        #                   Hours=Hour, Registeryear=RY, Detail=DET, RTOName=RTON,
        #                   OwnerNumber=ONA, VehicalMake=VEM,
        #                    ChassisNo=CN, EngineNo=EN, RCStatus=RCS,Tyare4_Photo=TL4,
        #                   Capacity=CAP, Trollyhook=TH, Rightside_Photo=RSP,
        #                   Leftside_Photo=LP, Meter_Photo=MP,
        #                   Back_Photo=BP, Tyare1_Photo=TP1, TyareLife1=TL1,
        #                   Tyare2_Photo=TY2, TyareLife2=TL2,
        #                   Tyare3_Photo=TY3, TyareLife3=TL3,
        #                   Engine_Photo=EP, Engine1_Photo=EP1,
        #                   Video=Video, Min_Prize=MPri)
        # item.save()
     


#
# def Add_Tractor(request):
#     if request.method == 'POST':
#         # import pdb; pdb.set_trace()
#
#         mimg = request.FILES['Mainimage']
#         Tname = request.POST['TAname']
#         HP = request.POST['HAP']
#         MF = request.POST['MAF']
#         RN = request.POST['RAN']
#         RC = request.POST['RAC']
#         EXPRI = request.POST['EAXPRI']
#         Hour = request.POST['HAour']
#         RY = request.POST['RAY']
#         DET = request.POST['DAET']
#         RTON = request.POST['RATON']
#         ONA = request.POST['OANA']
#         VEM = request.POST['VAEM']
#         COL = request.POST['CAOL']
#         CN = request.POST['CAN']
#         EN = request.POST['EAN']
#         RCS = request.POST['RACS']
#         CAP = request.POST['CAAP']
#         TH = request.POST['TAH']
#         # import pdb; pdb.set_trace()
#         Rightside_Photo = request.POST['RAP']
#         LP = request.POST['LAP']
#         MP = request.POST['MAP']
#         BP = request.POST['BAP']
#         TP1 = request.POST['TAP1']
#         TL1 = request.POST['TAL1']
#         TY2 = request.POST['TAY2']
#         TL2 = request.POST['TAL2']
#         TY3 = request.POST['TAY3']
#         TL3 = request.POST['TAL3']
#         TL4 = request.POST['TAL4']
#         EP = request.POST['EAP']
#         EP1 = request.POST['EAP1']
#         Video = request.POST['VAideo']
#         MPri = request.POST['MAPri']
#
#         item = OldTractor(upload=mimg, name=Tname, HP=HP, Manufacturingyear=MF, Regno=RN, RC=RC, price=EXPRI,
#                           Hours=Hour, Registeryear=RY, Detail=DET, RTOName=RTON, OwnerNumber=ONA, VehicalMake=VEM,
#                           Color=COL, ChassisNo=CN, EngineNo=EN, RCStatus=RCS,
#                           Capacity=CAP, Trollyhook=TH, Rightside_Photo=RP, Leftside_Photo=LP, Meter_Photo=MP,
#                           Back_Photo=BP, Tyare1_Photo=TP1, TyareLife1=TL1, Tyare2_Photo=TY2, TyareLife2=TL2,
#                           Tyare3_Photo=TY3, TyareLife3=TL3, Tyare4_Photo=TL4,
#                           TyareLife4=TL4, Engine_Photo=EP, Engine1_Photo=EP1, Video=Video, Min_Prize=MPri)
#         item.save()
#         return redirect("index")
#     else:
#         return render(request, 'addtractor.html')


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
