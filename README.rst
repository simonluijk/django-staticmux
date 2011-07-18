StaticMux
=========

StaticMux is a small django application to simplifiy development and deployment
of CSS and Javascript for Django projects.


Install
-------

Add `staticmux` to your INSTALLED_APPS setting.

In your base.html template load the template tags with `{% load staticmux %}`.
You will need to add `{% static_css %}` within your head tags and `{% static_js %}`
just before the closing body tag.

By default staticmux will look it css/src and js/src to your media files. This
can me configured with the `STATICMUX_CSS` and `STATICMUX_JS` settings.

When DEBUG == True the indivudual media files will be imported into the webpage
with the respective tags. With DEBUG == False the combined media file will be
imported into the page `js/compressed.js` and `css/compressed.css` by default.
These file can be generated with the command `python manage.py statixmux`
