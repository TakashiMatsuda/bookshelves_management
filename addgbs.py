#!/usr/bin/env python

import sys
from google_auth_oauthlib.flow import InstalledAppFlow

SHELF = 1001


def addbook(isbn: str, secrets_path: str):
    """
    add the book by isbn
    """
    flow = InstalledAppFlow.from_client_secrets_file(
                'client_secrets.json',
                scopes=['https://www.googleapis.com/auth/books'])
    flow.run_local_server()
    session = flow.authorized_session()
    searchquery = {'q': "isbn:{}".format(isbn)}
    searchresp = session.get("https://www.googleapis.com/books/v1/volumes",
                             params=searchquery)
    assert searchresp.ok
    volumeId = searchresp.json()['items'][0]['id']

    # add the book by volumeId
    addresp = session.post("https://www.googleapis.com/books/v1/mylibrary/"
                           + "bookshelves/{}/addVolume?volumeId={}"
                           .format(SHELF, volumeId))
    assert addresp.ok


if __name__ == '__main__':
    isbn = sys.argv[1]
    #secrets_path = sys.argv[2]
    secrets_path = 'client_secrets.json'
    addbook(isbn, secrets_path)
