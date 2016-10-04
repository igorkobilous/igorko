SECRET_KEY = 'xwr3&0e0rgs!8viv9w&-1k4r^=&1(869kamt5+=gfn6^^b@+j+'

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['students.ihorkobilous.com', 'demo-students.vitaliypodoba.co']

PORTAL_URL = 'http://students.vitaliypodoba.com'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'USER': 'test',
        'PASSWORD': 'x8wer3',
        'NAME': 'students_db',
        'TEST': {
            'CHARSET': 'utf8',
            'COLLATION': 'utf8_general_ci',
        }
    }
}

ADMIN_EMAIL = 'admin@studentsdb.com'
EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'ihorkobilous@gmail.com'
EMAIL_HOST_PASSWORD = 'ROti-8rYRJTbSSfsEoqCQg'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL  = 'webmaster@my-host.com'

ADMINS = (('Ihor', 'ihorkobilous@gmail.com'), ('Ihor', 'ihorbilous@yandex.ru'))
MANAGERS = (('Manager', 'manager@gmail.com'),)

STATIC_URL = '/static/'
STATIC_ROOT = '/path/to/folder/with/static/files/'

MEDIA_URL = '/media/'
MEDIA_ROOT = '/path/to/folder/with/media/files/'

SOCIAL_AUTH_FACEBOOK_KEY = '1052578368137861'
SOCIAL_AUTH_FACEBOOK_SECRET = '09f6de7ca423dcd6b3bcd3ec08feee7b'

#key for google login
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '538712673303-326m7bhnan728uj2q0295fuur8dfm7lk.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'Vd1YWM01zCGTX1NgSI2eGdmZ'

SOCIAL_AUTH_GOOGLE_OAUTH2_IGNORE_DEFAULT_SCOPE =  True
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE =  [
    'https://www.googleapis.com/auth/userinfo.email' ,
    'https://www.googleapis.com/auth/userinfo.profile'
]
SOCIAL_AUTH_GOOGLE_OAUTH2_USE_DEPRECATED_API = True

SOCIAL_AUTH_TWITTER_KEY = 'uzV78La1F7AIbhNFnYyolUfp9'
SOCIAL_AUTH_TWITTER_SECRET = 'I5LDgupesWGx5XHZdbiHBKEFTyqjue585R91ni6SPlXvO2H31x'