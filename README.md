# bookshelves_management

This is the set of tools to manage [my bookshelf](https://books.google.co.uk/books?hl=ja&as_coll=1001&num=10&uid=103766385898501065384&source=gbs_slider_cls_metadata_1001_mylibrary_title)

- Convert the photo of the book into its isbn number
- Add the book to the bookshelf on google books by isbn number

# Requirements
- [zbar](http://zbar.sourceforge.net/)
- Python3

# Typical usage

## Convert the photo to its isbn number
```
takeisbn.sh /PATH/TO/PHOTOS > /PATH/TO/ISBNLIST
```

## Add the books by the isbn number
```
python3 addgbs.py /PATH/TO/ISBNLIST
```
