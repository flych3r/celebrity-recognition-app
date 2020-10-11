import streamlit as st
import os
from image_paginator import paginator
from upload_to_bucket import upload_file
from read_from_dynamo import retrieve_all_items


CELEBS_BUCKET = os.environ.get('CELEBS_BUCKET')
CELEBS_TABLE = os.environ.get('CELEBS_TABLE')


def main():
    file = st.file_uploader("Upload file", type=["jpg"])
    if file:
        upload_file(file, CELEBS_BUCKET, object_ext='jpg')

    celeb_images = retrieve_all_items(CELEBS_TABLE)
    celeb_images = [
        (c['img_path']['S'], c['celebs']['S'])
        for c in celeb_images
    ]
    image_iterator = paginator("Select a sunset page", celeb_images)
    images_on_page, indices_on_page = map(list, zip(*image_iterator))
    st.image(images_on_page, width=300, caption=indices_on_page)

if __name__ == '__main__':
    main()
