django-angular-auth
=========

This is based on [HTTP Auth Interceptor Module Demo] and uses [Tastypie] to provide the JSON API for the [AngularJS] front-end.

Django is used only to provide the API and also for it's admin.

Setup
-----------

It's assumed you have Python and Postgres already installed.

* Clone [django-angular-auth] locally.
* Create a VirtualEnv and install the requirements via ```pip install -r requirements.txt```
* Run ```python manage.py syncdb --migrate```
* Go into static directory and run ```python -m SimpleHTTPServer```. I created a serve.bat file for this. This is the Angular app.
* Start Django. ```python runserver 0.0.0.0:8001``` I created a batch file for this called r.bat. This is your API and admin.
* Go to [http://localhost:8000/]. This is the Angular app. It's being served directly via SimpleHTTPServer. It can be served from anywhere, even Amazon. There might be cross domain

Use it
----------
So now we have the Admin and front-end client both running. Let's test

* With your browser pointed to [http://localhost:8000/], enter some data in the field and click "submit". You will get a login prompt.
* Login.

You will get a "missing key" error message. This is because your user does not have API access. To add access, go to [http://localhost:8001/admin/tastypie/apikey/add/] and add a key. Any key will do.

Go back and try to login again. This time, your login worked! Find your just added data at [http://localhost:8001/admin/myproperty/paymenttype/].

What's Happening
--------------
If you take a look at js/controllers.js, you'll find the ```ContentController```. When you submit the form, it's trying to post to [http://localhost:8001/api/myproperty/paymenttype/]. However, it gets a 401 status code back because you're not logged in.

Tastypie is requiring authentication for this resource in ch/api.py by using the [ApiKeyAuthentication] class in PaymentTypeResource.

This TastyPie class looks for the API key in the GET/POST or header. We are using headers. On login, we set the header within Angular.js. See js/controllers.js ~ line 27

```$http.defaults.headers.common['Authorization'] = 'ApiKey ' + data.username + ':' + data.key;```

Because Django returns a status code 401, Angular intercepts this (lib/http-auth-interceptor.js ~line 61) and instead displays the login screen. Once you have a valid API key, it replays your API call and continues where it left off.

License
-------
MIT

  [ed menendez]: http://menendez.com/about/
  [@edmenendez]: http://twitter.com/edmenendez
  [Tastypie]: http://tastypieapi.org/
  [HTTP Auth Interceptor Module Demo]: http://witoldsz.github.com/angular-http-auth/
  [AngularJS]: http://angularjs.org/
  [django-angular-auth]: https://github.com/edmenendez/django-angular-auth
  [ApiKeyAuthentication]: http://django-tastypie.readthedocs.org/en/latest/authentication_authorization.html#apikeyauthentication

Version
-

0.1
