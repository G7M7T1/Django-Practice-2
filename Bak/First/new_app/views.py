from django.shortcuts import render


# Create your views here.
def new_index(req):
    return render(req, 'new_app/index.html')


def variable_view(req):
    my_var = {'first_name': 'Rosalind', 'last_name': 'Jon',
              'some_list': [81, 22, 3, 24, 18, 67, 45, 100],
              'some_dict': {'call_phone': 10080215}, 'user_login': True}

    return render(req, 'new_app/variable.html', context=my_var)


def new_page(req):
    return render(req, 'new_app/newpage.html')