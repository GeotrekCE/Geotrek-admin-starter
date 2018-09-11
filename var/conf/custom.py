from geotrek.settings.base import *
import os

#
# BASIC SETTINGS
# ..............
# SRID = 2154  # LAMBERT EXTENDED FOR FRANCE, used for geometric columns.
# Must be a projection in meters Fixed at install, don't change it after
#
# DEFAULT_STRUCTURE_NAME = 'GEOTEAM' # -> Name for your default structure. Can be changed in geotrek admin interface

# SPATIAL_EXTENT = (446412.4257, 6151098.7987, 695956.5365, 6343234.0658)
# spatial bbox in your own projection (example here with 2154)
# this spatial_extent will limit map exploration, and will cut your raster imports
#
# LANGUAGE_CODE = 'fr' # for web interface. default to fr (French)

# MODELTRANSLATION_LANGUAGES = ('fr', 'en', )
# Change with your own wanted translations
# ex: MODELTRANSLATION_LANGUAGES = ('en', 'fr', 'de', 'ne')

ADMINS = (
    ('GEOTREK', 'support-geotrek@lists.makina-corpus.com'),  # change with tuple ('your name', 'your@address.mail')
)
# used to send error mails

MANAGERS = (
)

# or MANAGERS = ADMIN
# used to send report mail

# TIME_ZONE="Europe/Paris"
# set your timezone for date format. For France, uncomment line beside
# For other zones : find your timezone in https://en.wikipedia.org/wiki/List_of_tz_database_time_zones

#
# MAIL SETTINGS
# ..........................
DEFAULT_FROM_EMAIL = "noreply@%s" % os.getenv('DOMAIN_NAME', '')
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

# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True

SPLIT_TREKS_CATEGORIES_BY_PRACTICE = True

SYNC_RANDO_ROOT = '/app/src/var/data'

SYNC_RANDO_OPTIONS = {
    'skip_tiles': True,
}
