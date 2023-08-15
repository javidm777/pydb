import shutil
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import WordpressDownloadForm
from . import counter
from django.http import FileResponse

@login_required(login_url='/admin/login/')
def download_wordpress(request):
    if request.method == 'POST':
        form = WordpressDownloadForm(request.POST)
        if form.is_valid():
            website = form.cleaned_data['website']
            wp_username = form.cleaned_data['wp_username']
            wp_password = form.cleaned_data['wp_password']

            # اجرای اسکریپت و ذخیره خروجی در فایل اکسل
            counter.main_download(website, wp_username, wp_password)
            directory_path = f'output_counter/{website}'
            result_df = counter.count_words_in_directory(directory_path)
            output_excel_path = f'output_counter/{website}.xlsx'
            result_df.to_excel(output_excel_path, index=False)
            shutil.rmtree(directory_path)

            # ایجاد FileResponse برای دانلود فایل
            file_response = FileResponse(open(output_excel_path, 'rb'),
                                         as_attachment=True)
            file_response[
                'Content-Disposition'] = f'attachment; filename="{output_excel_path}" '
            return file_response
    else:
        form = WordpressDownloadForm()
    return render(request, 'counter/download_form.html',
                  {'form': form})



def counter_page(request):
    return render(request, 'counter/counter_page.html')
