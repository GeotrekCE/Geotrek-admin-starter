from geotrek.settings.base import LEAFLET_CONFIG

#
# BASIC SETTINGS
# ..............
# SRID = 2154  # LAMBERT EXTENDED FOR FRANCE, used for geometric columns.
# Must be a projection in meters Fixed at install, don't change it after
#
DEFAULT_STRUCTURE_NAME = 'PNRP'  # -> Name for your default structure. Can be changed in geotrek admin interface
#
SPATIAL_EXTENT = (500413.05, 6773442.40, 577989.04, 6851411.72)

ALTIMETRIC_PROFILE_MIN_YSCALE = 600

# spatial bbox in your own projection (example here with 2154)
# this spatial_extent will limit map exploration, and will cut your raster imports
#
# LANGUAGE_CODE = 'en' # for web interface. default to fr (French)

MODELTRANSLATION_LANGUAGES = ('en', 'fr',)
# Change with your own wanted translations
# ex: MODELTRANSLATION_LANGUAGES = ('en', 'fr', 'de', 'ne')

ADMINS = (
    ('GEOTREK', 'support-geotrek@lists.makina-corpus.com'),
    #    ('admin1', 'jonathan.allain@parc-naturel-perche.fr'),
    #    ('admin2', 'fabienne.debuchy@parc-naturel-perche.fr'),
    #    ('admin2', 'contact@parc-naturel-perche.fr'),
)
# used to send error mails

MANAGERS = (
    ('manager1', 'fabienne.debuchy@parc-naturel-perche.fr'),
)

LEAFLET_CONFIG['TILES'] = [
    ('Scan',
     '//gpp3-wxs.ign.fr/b746xijzy2ihmjn3whljl0l9/geoportail/wmts?LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS&EXCEPTIONS=image/jpeg&FORMAT=image/jpeg&SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}',
     '&copy; IGN - GeoPortail'),
    ('Scan Express',
     '//gpp3-wxs.ign.fr/b746xijzy2ihmjn3whljl0l9/geoportail/wmts?LAYER=GEOGRAPHICALGRIDSYSTEMS.MAPS.SCAN-EXPRESS.STANDARD&EXCEPTIONS=image/jpeg&FORMAT=image/jpeg&SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}',
     '&copy; IGN - GeoPortail'),
    ('Ortho',
     '//gpp3-wxs.ign.fr/b746xijzy2ihmjn3whljl0l9/geoportail/wmts?LAYER=ORTHOIMAGERY.ORTHOPHOTOS&EXCEPTIONS=image/jpeg&FORMAT=image/jpeg&SERVICE=WMTS&VERSION=1.0.0&REQUEST=GetTile&STYLE=normal&TILEMATRIXSET=PM&TILEMATRIX={z}&TILEROW={y}&TILECOL={x}',
     '&copy; IGN - GeoPortail'),
    ('OSM', '//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', '(c) OpenStreetMap Contributors'),
]

SPLIT_TREKS_CATEGORIES_BY_PRACTICE = True

# TIME_ZONE="Europe/Paris"
# set your timezone for date format. For France, uncomment line beside
# For other zones : find your timezone in https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

#
# MAIL SETTINGS
# ..........................
DEFAULT_FROM_EMAIL = "noreply@geotrek-perche.makina-corpus.net"
# address will be set for sended emails (ex: noreply@yourdomain.net)
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_HOST = "172.17.0.1"
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

SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SYNC_RANDO_OPTIONS = {
    'skip-tiles': True,
}
