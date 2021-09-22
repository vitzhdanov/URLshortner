from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from shortner.forms import UrlForm
from shortner.models import Url
from shortner.random import random_url, emoji


def main(request):
    urls = Url.objects.all()
    form = UrlForm()
    print(request.POST)
    if request.method == 'POST' and 'http' in str(request.POST.get('long_url')):
        if request.POST.get('letters'):
            try:
                if request.POST.get('long_url') == urls.get(long_url=request.POST.get('long_url')).long_url:
                    url = urls.get(long_url=request.POST.get('long_url'))
                    context = {'url': url, 'form': form}
                    return render(request, 'shortner/main.html', context)
            except ObjectDoesNotExist:
                urls.create(long_url=request.POST.get('long_url'), short_url_sym=f'http://127.0.0.1:8000/{random_url()}', short_url_em=f'http://127.0.0.1:8000/{emoji()}')
                url = urls.get(long_url=request.POST.get('long_url'))
                context = {'url': url, 'form': form}
                return render(request, 'shortner/main.html', context)
    if len(urls) > 100000:
        urls.delete()
    context = {'url': urls, 'form': form}
    return render(request, 'shortner/main.html', context)


def url(request, url):
    try:
        url = Url.objects.get(short_url_sym=f'http://127.0.0.1:8000/{url}').long_url
        return redirect(url)
    except ObjectDoesNotExist:
        url = Url.objects.get(short_url_em=f'http://127.0.0.1:8000/{url}').long_url
        return redirect(url)