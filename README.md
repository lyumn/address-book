# Address Book

A web-based address book which allows a user to manage individual contacts.

## Features

* Basic user authentication
* User is able to create/update/view/delete their contacts


## Requirements

* Django 1.8
* Python 2.7

## Installation

Add to your project settings:

```
INSTALLED_APPS = (
    ...
    'address_book',
    ...
)
```

```
TEMPLATES = [
    {
        ...
        'APP_DIRS': True,
        ...
    },
]

LOGIN_REDIRECT_URL = '/'
```

Migrate in database tables:

`python manage.py migrate address_book`

`python manage.py migrate accounts`

Add to your project urls.py:

```
    url(r'^address_book/', include('address_book.urls', namespace="address_book")),
    url(r'^admin/', include(admin.site.urls)),
    url('accounts/', include('accounts.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url('', TemplateView.as_view(template_name='home.html'), name='home'),
```

## Future Improvements

* User should be able filter their contacts
