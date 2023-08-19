from django.shortcuts import render
from .main import get_wordpress_posts
from .remove import process_text_file


def form_view(request):
    if request.method == 'POST':
        website = request.POST.get('website')
        wordpress_username = request.POST.get('wordpress_username')
        wordpress_password = request.POST.get('wordpress_password')

        batch_size = 50
        output_directory = website

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

        # اجرای دکمه‌ها
        if 'remove_arad_links' in request.POST:
            txt_files = [f for f in os.listdir(output_directory) if
                         f.endswith(".txt")]
            for txt_file in txt_files:
                txt_file_path = os.path.join(output_directory, txt_file)
                process_text_file(txt_file_path)
            message = "Arad links removed successfully."

        elif 'create_links' in request.POST:
            # اجرای اسکریپت مربوط به لینک‌سازی
            message = "Links created successfully."

        return render(request, 'links/result.html',
                      {'count': count, 'message': message, 'website': website})

    return render(request, 'links/form.html')
