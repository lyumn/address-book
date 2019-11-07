# Address Book

## Features

* Basic user authentication
* User is able to create/update/view/delete their contacts


## Requirements

* Django 1.8
* Python 2.7

## Installation

django-todo is a Django app, not a project site. It needs a site to live in. You can either install it into an existing Django project site, or clone the django-todo [demo site (GTD)](https://github.com/shacker/gtd).

If using your own site, be sure you have jQuery and Bootstrap wired up and working.

django-todo views that require it will insert additional CSS/JavaScript into page heads, so your project's base templates must include:

```jinja
{% block extrahead %}{% endblock extrahead %}
{% block extra_js %}{% endblock extra_js %}
```

django-todo comes with its own `todo/base.html`, which extends your master `base.html`. All content lives inside of:

`{% block content %}{% endblock %}`

If you use some other name for your main content area, you'll need to override and alter the provided templates.

All views are login-required. Therefore, you must have a working user authentication system.

For email notifications to work, make sure your site/project is [set up to send email](https://docs.djangoproject.com/en/2.0/topics/email/).

Make sure you've installed the Django "sites" framework and have specified the default site in settings, e.g. `SITE_ID = 1`

Put django-todo/todo somewhere on your Python path, or install via pip:

    pip install django-todo


Add to your settings:

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

`python manage.py migrate todo`

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
