
def handle_uploaded_file(f, user):

    with open('', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
