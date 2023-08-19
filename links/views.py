from django.shortcuts import render
from .main import get_wordpress_posts


def form_view(request):
    if request.method == 'POST':
        website = request.POST.get('website')
        wordpress_username = request.POST.get('wordpress_username')
        wordpress_password = request.POST.get('wordpress_password')

        batch_size = 100
        output_directory = f'links/output/{website}'

        start_post = 1
        count = 0

        while True:
            success = get_wordpress_posts(website, wordpress_username,
                                          wordpress_password, start_post,
                                          batch_size, output_directory)
            if not success:
                break
            start_post += batch_size
            count += batch_size

        return render(request, 'links/result.html', {'count': count})

    return render(request, 'links/form.html')
