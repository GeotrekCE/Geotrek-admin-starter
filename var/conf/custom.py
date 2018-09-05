from geotrek.settings.base import LEAFLET_CONFIG
# import os

#
# BASIC SETTINGS
# ..............
SRID = 2154  # LAMBERT EXTENDED FOR FRANCE, used for geometric columns.
# Must be a projection in meters Fixed at install, don't change it after
#
DEFAULT_STRUCTURE_NAME = 'ARCHE-AGGLO' # -> Name for your default structure. Can be changed in geotrek admin interface

SPATIAL_EXTENT = (805912, 6426630, 882869, 6470947)
# spatial bbox in your own projection (example here with 2154)
# this spatial_extent will limit map exploration, and will cut your raster imports
#
LANGUAGE_CODE = 'fr' # for web interface. default to fr (French)

MODELTRANSLATION_LANGUAGES = ('fr', 'en', 'de',)
# Change with your own wanted translations
# ex: MODELTRANSLATION_LANGUAGES = ('en', 'fr', 'de', 'ne')

ADMINS = (
    ('GEOTREK', 'support-geotrek@lists.makina-corpus.com'), # change with tuple ('your name', 'your@address.mail')
)
# used to send error mails

MANAGERS = (
    ('manager1', 'damien@tourisme-saintfelicien.fr'),
    ('manager2', 'd.mathieu@ah-tourisme.com'), # change with tuple ('your name', 'your@address.mail')
)

# or MANAGERS = ADMIN
# used to send report mail

# TIME_ZONE="Europe/Paris"
# set your timezone for date format. For France, uncomment line beside
# For other zones : find your timezone in https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

#
# MAIL SETTINGS
# ..........................
# DEFAULT_FROM_EMAIL =
# address will be set for sended emails (ex: noreply@yourdomain.net)
# SERVER_EMAIL = DEFAULT_FROM_EMAIL
# EMAIL_HOST =
# EMAIL_HOST_USER =
# EMAIL_HOST_PASSWORD =
# EMAIL_HOST_PORT =
# EMAIL_USE_TLS = FALSE
# EMAIL_USE_SSL = FALSE

#
# External authent if required
# ..........................

# AUTHENT_DATABASE = 'your_authent_dbname'
# AUTHENT_TABLENAME = 'your_authent_table_name'
# if AUTHENT_TABLENAME:
#     AUTHENTICATION_BACKENDS = ('geotrek.authent.backend.DatabaseBackend',)

# IF YOU USE SSL

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

LEAFLET_CONFIG['TILES'] = [
    ('Scan Express', 
'http://gpp3-wxs.ign.fr/ep7lci7sy61ti943uzugq6wp/geoportail/wmts?LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN-EXPRESS.STANDARD&EXCEPTIONS=image/jpeg&FORMAT=image/jpeg&SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}', 
'&copy; IGN - GeoPortail'),
    ('Scan', 
'http://gpp3-wxs.ign.fr/ep7lci7sy61ti943uzugq6wp/geoportail/wmts?LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS&EXCEPTIONS=image/jpeg&FORMAT=image/jpeg&SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}', 
'&copy; IGN - GeoPortail'),
    ('Ortho', 
'http://gpp3-wxs.ign.fr/ep7lci7sy61ti943uzugq6wp/geoportail/wmts?LAYER=ORTHOIMAGERY.ORTHOPHOTOS&EXCEPTIONS=image/jpeg&FORMAT=image/jpeg&SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}', 
'&copy; IGN - GeoPortail'),
    ('OSM', 'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', '(c) OpenStreetMap Contributors'),
]

SPLIT_TREKS_CATEGORIES_BY_PRACTICE = True

SYNC_RANDO_ROOT = '/app/src/var/data'
SYNC_RANDO_OPTIONS = {
    #'url': 'http://geotrek-ardeche-hermitage.fr',
    'rando_url': 'http://rando-ardeche-hermitage.fr',
}
