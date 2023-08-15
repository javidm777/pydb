import shutil
import xmlrpc.client
import os
import pandas as pd


def get_wordpress_posts(wp_url, wp_username, wp_password):
    try:
        wp = xmlrpc.client.ServerProxy(wp_url)
        posts = wp.wp.getPosts(0, wp_username, wp_password, {'number': 1000})
        return posts
    except Exception as e:
        print(f"Error while getting posts: {e}")
        return []


def save_to_txt_file(directory, title, content):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(os.path.join(directory, f"{title}.txt"), 'w',
                  encoding='utf-8') as file:
            file.write(content)
        # print(f"محتوای '{title}' با موفقیت در فایل ذخیره شد.")
    except Exception as e:
        print(f"Error while saving {title}: {e}")


def main_download(website, wp_username, wp_password):
    wp_url = f'https://{website}/xmlrpc.php'
    target_directory = f'output_counter/{website}'
    posts = get_wordpress_posts(wp_url, wp_username, wp_password)
    for post in posts:
        title = post['post_title']
        content = post['post_content']
        save_to_txt_file(target_directory, title, content)


def count_words_in_directory(directory_path):
    try:
        files = [file for file in os.listdir(directory_path) if
                 file.endswith('.txt')]
        data = []

        for file in files:
            file_path = os.path.join(directory_path, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                word_count = len(content.split())
                data.append((file, word_count))

        df = pd.DataFrame(data, columns=['عنوان محتوا', 'تعداد کلمات'])
        return df
    except:
        print('ERROR TRY AGIAN')


