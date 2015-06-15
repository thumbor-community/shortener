Installing Thumbor Community Shortener
======================================

1. Install thumbor (see `Thumbor repository`_)
2. Install `Thumbor Community Core`_
3. Clone this repository.
4. If you've set a virtualenv up for thumbor, activate it.
5. Install the Thumbor Community Shortener:
::
    $ cd thumbor-community/shortener
    $ pip install .

6. Register the extension within Thumbor's configuration file:
::
    COMMUNITY_EXTENSIONS = [
        'shortener',
        ...
    ]

7. Configure the extension within the same file:
::
    SHORTENER_GENERATOR = 'Generator'   # Shortener generator class name, defaults to Generator
    SHORTENER_STORAGE   = 'Storage'     # Shortener storage class name, defaults to Storage

7. Launch thumbor with the Thumbor Community custom application:
::
    $ thumbor --conf=my_configuration_file -a thumbor_community.app.App


.. _`Thumbor repository`: https://github.com/thumbor/thumbor
.. _`Thumbor Community Core`: https://github.com/thumbor-community/core
