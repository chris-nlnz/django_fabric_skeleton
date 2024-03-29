__author__ = 'chris'

base_html = """
<!DOCTYPE html>
{% load i18n %}
<!--[if lt IE 7]>      <html class="no-js lt-ie9 lt-ie8 lt-ie7"> <![endif]-->
<!--[if IE 7]>         <html class="no-js lt-ie9 lt-ie8"> <![endif]-->
<!--[if IE 8]>         <html class="no-js lt-ie9"> <![endif]-->
<!--[if gt IE 8]><!--> <html class="no-js"> <!--<![endif]-->
    <head>
        <meta charset="utf-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1"/>
        <title>{% block page_title %}[name]{% endblock %}</title>

        <meta name="description" content="{% block meta_description %}{% endblock %}" />
        <meta name="author" content="{% block meta_author %}{% endblock %}" />
        <meta name="viewport" content="width=device-width" />
        <link rel="stylesheet" href="{{ STATIC_URL }}css/normalize.css" />
        <link rel="stylesheet" href="{{ STATIC_URL }}css/main.css" />
        {% block css %}{% endblock %}

        <script src="{{ STATIC_URL }}js/vendor/modernizr-2.6.2.min.js"></script>
    </head>

    <body class="{% block body_class %}{% endblock %}">
    {% block body %}
        <!--[if lt IE 7]>
            <p class="chromeframe">You are using an outdated browser. <a href="http://browsehappy.com/">Upgrade your browser today</a> or <a href="http://www.google.com/chromeframe/?redirect=true">install Google Chrome Frame</a> to better experience this site.</p>
        <![endif]-->

        {% block content %}
        {% endblock content %}

        {% block javascript_library %}
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
        <script>window.jQuery || document.write('<script src="{{ STATIC_URL }}js/vendor/jquery-1.9.1.min.js"><\/script>')</script>
        <script src="{{ STATIC_URL }}js/plugins.js"></script>
        <script src="{{ STATIC_URL }}js/main.js"></script>
        {% endblock javascript_library %}
        {% block javascript %}
        {% endblock javascript %}

        <!-- Google Analytics: change UA-XXXXX-X to be your site's ID. -->
        <script>
            var _gaq=[['_setAccount','UA-XXXXX-X'],['_trackPageview']];
            (function(d,t){var g=d.createElement(t),s=d.getElementsByTagName(t)[0];
            g.src=('https:'==location.protocol?'//ssl':'//www')+'.google-analytics.com/ga.js';
            s.parentNode.insertBefore(g,s)}(document,'script'));
        </script>
    {% endblock body %}
    </body>
</html>
"""

home_html = """
{% extends "base.html" %}
{% load i18n %}
{% block body_class %}{{ block.super }} home{% endblock %}

{% block content %}
    <!-- Add your site or application content here -->
    <p>{% trans "Hello world!" %}</p>
    <p>{% trans "Edit 'templates/home.html' to modify this content." %}</p>
{% endblock %}
"""