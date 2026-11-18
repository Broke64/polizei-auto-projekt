# polizei-auto-projekt
Gewinner TEAM TIKT!
Alaaf!


/usr/bin/python /home/szapf/Documents/final_code_auto/main.py
/usr/lib/python3/dist-packages/gpiozero/input_devices.py:852: PWMSoftwareFallback: For more accurate readings, use the pigpio pin factory.See https://gpiozero.readthedocs.io/en/stable/api_input.html#distancesensor-hc-sr04 for more info
  warnings.warn(PWMSoftwareFallback(
/home/szapf/.local/lib/python3.13/site-packages/pirc522/rfid.py:97: RuntimeWarning: This channel is already in use, continuing anyway.  Use GPIO.setwarnings(False) to disable warnings.
  GPIO.setup(pin_rst, GPIO.OUT)
 * Serving Flask app 'main'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://10.10.0.173:5000
Press CTRL+C to quit
[2026-11-18 10:34:53,166] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/szapf/Documents/final_code_auto/main.py", line 43, in index
    return render_template("index.html", state = state)     #landingpage
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 150, in render_template
    return _render(app, template, context)
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 131, in _render
    rv = template.render(context)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1295, in render
    self.environment.handle_exception()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 942, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "/home/szapf/Documents/final_code_auto/templates/index.html", line 1, in top-level template code
    {% extends "base.html" %}
  File "/home/szapf/Documents/final_code_auto/templates/base.html", line 11, in top-level template code
    {% block content %}{% endblock %}
    ^^^^^^^^^^^^^^^^^
  File "/home/szapf/Documents/final_code_auto/templates/index.html", line 4, in block 'content'
    {% include "partials/verriegelung.html" %}
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/szapf/Documents/final_code_auto/templates/partials/verriegelung.html", line 12, in top-level template code
    const antwort = await fetch("{{ url_for('status')}}");
    ^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1121, in url_for
    return self.handle_url_build_error(error, endpoint, values)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1110, in url_for
    rv = url_adapter.build(  # type: ignore[union-attr]
        endpoint,
    ...<3 lines>...
        force_external=_external,
    )
  File "/usr/lib/python3/dist-packages/werkzeug/routing/map.py", line 924, in build
    raise BuildError(endpoint, values, method, self)
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'status'. Did you mean 'static' instead?
10.10.0.205 - - [18/Nov/2026 10:34:53] "GET / HTTP/1.1" 500 -
10.10.0.205 - - [18/Nov/2026 10:34:53] "GET /favicon.ico HTTP/1.1" 404 -
[2026-11-18 10:35:02,965] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1511, in wsgi_app
    response = self.full_dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 919, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "/usr/lib/python3/dist-packages/flask/app.py", line 917, in full_dispatch_request
    rv = self.dispatch_request()
  File "/usr/lib/python3/dist-packages/flask/app.py", line 902, in dispatch_request
    return self.ensure_sync(self.view_functions[rule.endpoint])(**view_args)  # type: ignore[no-any-return]
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^
  File "/home/szapf/Documents/final_code_auto/main.py", line 43, in index
    return render_template("index.html", state = state)     #landingpage
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 150, in render_template
    return _render(app, template, context)
  File "/usr/lib/python3/dist-packages/flask/templating.py", line 131, in _render
    rv = template.render(context)
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 1295, in render
    self.environment.handle_exception()
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^^
  File "/usr/lib/python3/dist-packages/jinja2/environment.py", line 942, in handle_exception
    raise rewrite_traceback_stack(source=source)
  File "/home/szapf/Documents/final_code_auto/templates/index.html", line 1, in top-level template code
    {% extends "base.html" %}
  File "/home/szapf/Documents/final_code_auto/templates/base.html", line 11, in top-level template code
    {% block content %}{% endblock %}
    ^^^^^^^^^^^^^^^^^
  File "/home/szapf/Documents/final_code_auto/templates/index.html", line 4, in block 'content'
    {% include "partials/verriegelung.html" %}
    ^^^^^^^^^^^^^^^^^^^^^
  File "/home/szapf/Documents/final_code_auto/templates/partials/verriegelung.html", line 12, in top-level template code
    const antwort = await fetch("{{ url_for('status')}}");
    ^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1121, in url_for
    return self.handle_url_build_error(error, endpoint, values)
           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/flask/app.py", line 1110, in url_for
    rv = url_adapter.build(  # type: ignore[union-attr]
        endpoint,
    ...<3 lines>...
        force_external=_external,
    )
  File "/usr/lib/python3/dist-packages/werkzeug/routing/map.py", line 924, in build
    raise BuildError(endpoint, values, method, self)
werkzeug.routing.exceptions.BuildError: Could not build url for endpoint 'status'. Did you mean 'static' instead?
10.10.0.205 - - [18/Nov/2026 10:35:02] "GET / HTTP/1.1" 500 -
^CException in thread Thread-4 (alarm_loop):
