import requests

from django.conf import settings

v = 5.131


def post_photo_to_vk_group(file_path):
    response = requests.post(
        'https://api.vk.com/method/photos.getUploadServer',
        data={
            'group_id': settings.VK_GROUP_ID,
            'album_id': settings.VK_GROUP_ALBUM_ID,
            'access_token': settings.VK_TOKEN,
            'v': v
        }
    )
    upload_url = response.json()['response']['upload_url']

    response_send_file = requests.post(upload_url, files=dict(file=open(file_path, 'rb')))
    if len(response_send_file.json()['photos_list'])==0:
        return False

    response_photos_save = requests.post(
        'https://api.vk.com/method/photos.save',
        data={
            'group_id': settings.VK_GROUP_ID,
            'album_id': settings.VK_GROUP_ALBUM_ID,
            'access_token': settings.VK_TOKEN,
            'photos_list': response_send_file.json()['photos_list'],
            'server': response_send_file.json()['server'],
            'hash': response_send_file.json()['hash'],
            'v': v
        }
    )

    photo_id = response_photos_save.json()['response'][0]['id']
    owner_id = response_photos_save.json()['response'][0]['owner_id']
    response = requests.post(
        'https://api.vk.com/method/wall.post', data={
            'access_token': settings.VK_TOKEN,
            'owner_id': -int(settings.VK_GROUP_ID),
            'attachments': f'photo{owner_id}_{photo_id}',
            'from_group': 1,
            # 'message': 'test',
            'signed': 0,
            'v': v
        }
    ).json()

    return response
