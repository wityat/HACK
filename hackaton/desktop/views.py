from django.shortcuts import render, HttpResponse, redirect
from qr_code.qrcode.utils import QRCodeOptions
from decimal import Decimal
from django.conf import settings
from django.urls import resolve, reverse
from .models import SiteUser
from .forms import ImageUpload, CheckTags
from .management.commands import obj_recognise
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def index(request):
    request.session.create()
    return render(request, 'desktop/base.html')


def mobile_qr(request):
    user = SiteUser.objects.filter(session_key=request.session.session_key)
    if user:
        user = user[0]
        if user.image:
            return render(request, 'desktop/mobile_qr.html', {'image_exist': True, 'obj': user})

    context = dict(
        my_options=QRCodeOptions(size='L', border=6, error_correction='L'),
        current_url=f"http://185.139.69.27:8000/desktop/upload?session_key={request.session.session_key}",
        image_exist=False,
    )
    return render(request, 'desktop/mobile_qr.html', context=context)


def create_user(request):
    user = SiteUser.objects.create(session_key=request.session.session_key)
    return user


def upload(request):
    # model = SiteUser.objects.get(session_key=request.POST['session_key'])
    # form_class = ImageUpload
    # template_name = 'desktop/upload.html'
    #
    # return render(request, 'desktop/upload.html', {"form_class": form_class})

    # form = ImageUpload()
    # image_exist = False
    # # user = SiteUser.objects.get(session_key=request.session.session_key)
    #
    # if request.method:
    #     form = ImageUpload(request.POST, request.FILES)
    #     # form.session_key = user.session_key
    #     # form.save()
    #     if form.is_valid():
    #         image_exist = True
    #         form.image = form.cleaned_data['image']
    #         form.save()
    #
    # return render(request, "desktop/upload.html", {"form": form, "image_exist": image_exist})

    session_key_, is_desktop = request.session.session_key if not request.GET.get("session_key") else request.GET.get(
        "session_key"), False
    image_exist = False
    form = ImageUpload(request.POST, request.FILES or None)
    obj = None

    if request.method == "POST" and form.is_valid():
        obj = form.save(commit=True)
        obj.session_key = session_key_
        obj.save()
        image_exist = True
        # return HttpResponse("Картинка загружена!")

    return render(request, 'desktop/upload.html', {'form': form, 'image_exist': image_exist, 'obj': obj})


def neural():
    result = ['Keyboard', 'Mouse', 'Toaster', 'Panda', 'Black cat']
    return result


def result(request):
    user = SiteUser.objects.filter(session_key=request.session.session_key)[0]
    result = obj_recognise.get_most_similar(f"http://185.139.69.27:8000/{user.image.url}")

    return render(request, 'desktop/result.html', {'result': result})
