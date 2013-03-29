django-angular-auth
=========

This is based on [HTTP Auth Interceptor Module Demo] and uses [Tastypie] to provide the JSON API for the [AngularJS] front-end.

Django is used to provide the API and for its admin.

Setup
-----------

It's assumed you have Python and Postgres already installed.

* Clone [django-angular-auth] locally.
* Create a VirtualEnv and install the requirements via ```pip install -r requirements.txt```
* Create a database in Postgres. Whatever database settings used needs to be added to apps/ch/settings.py ~ line 12. You could also make a settings_local file using your machine name and put that in settings_local/MACHINE_NAME.py
* Run ```python manage.py syncdb --migrate```
* Go into static directory and run ```python -m SimpleHTTPServer```. You should create a serve.bat file for this. This is the Angular app.
* Start Django. ```python runserver 0.0.0.0:8001``` I created a batch file for this called r.bat. This is your API and admin.
* Go to [http://localhost:8000/]. This is the Angular app. It's being served directly via SimpleHTTPServer. It can be served from anywhere, even Amazon. There might be cross domain issues if you're hosting on a different domain.

Use it
----------
Now we have the admin and front-end client both running. Let's test.

* With your browser pointed to [http://localhost:8000/], enter some data in the field and click "submit". You will get a login prompt.
* Login.

You will get a "missing key" error message. This is because your user does not have API access. To add access, go to http://localhost:8001/admin/tastypie/apikey/add/ and add a key. Any key will do. You can have this key added automatically for new users by uncommenting out the signal at the bottom of myproperty/models.py.

Go back and try to login again. This time, your login worked! Find your just added data at http://localhost:8001/admin/myproperty/paymenttype/.

What's Happening
--------------
If you take a look at js/controllers.js, you'll find the ```ContentController```. When you submit the form, it's trying to post to [http://localhost:8001/api/myproperty/paymenttype/]. However, it gets a 401 status code back because you're not logged in.

Tastypie is requiring authentication for this resource in ch/api.py by using the [ApiKeyAuthentication] class in PaymentTypeResource.

This TastyPie class looks for the API key in the GET/POST or header. We are using headers. On login, we set the header within Angular.js. See js/controllers.js ~ line 27

```$http.defaults.headers.common['Authorization'] = 'ApiKey ' + data.username + ':' + data.key;```

Because Django returns a status code 401, Angular intercepts this (lib/http-auth-interceptor.js ~line 61) and instead displays the login screen. Once you have a valid API key, it replays your API call and continues where it left off.

Future
-------
This is a very basic demo. I hope it helps shortcut getting you started with AngularJS and Django. You might want to add additional checking in your TastyPie authentication so that the API key expires after a certain amount of time, or even if the IP changes.

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
  [http://localhost:8000/]: http://localhost:8000/

Version
-

0.1
