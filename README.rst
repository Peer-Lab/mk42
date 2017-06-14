.. mk42
.. README.rst

A mk42 documentation
====================
    *mk42 is a backend for Peer Lab Kyiv (https://meetup.com/peerlab-kyiv/) cooperative pet project*

.. contents::

Bootstrap
---------
* Install ``git``, ``gcc``, ``mercurial``, ``libjpeg-turbo-devel``, ``freetype-devel``, ``GeoIP-devel``, ``python2-virtualenv``, ``memcached``, ``redis`` and ``rabbitmq-server`` system packages. On Fedora or CentOS ``dnf install git gc mercurial libjpeg-turbo-devel freetype-devel GeoIP-devel python2-virtualenv memcached redis rabbitmq-server``.
* Install ``https://github.com/kennethreitz/autoenv/``. And configure to use ``.autoenv`` files instead of ``.env``.
* Get code: ``git clone https://github.com/Peer-Lab/mk42.git``.
* Copy ``.credentials-example`` to ``.credentials``. Fill ``.credentials`` by your credentials.
* Create virtualenv: ``make create-virtualenv``.
* Install requirements: ``make pip-install``.

Licensing
---------
This work is free. You can redistribute it and/or modify it under the terms of the Do What The Fuck You Want To Public License, Version 2, as published by Sam Hocevar. See the COPYING file for more details.

Contacts
--------
**Project website**: https://github.com/Peer-Lab/mk42/

**Author**: Peer Lab Kyiv

For full authors list see AUTHORS file.
