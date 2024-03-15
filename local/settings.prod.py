# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-5d8%)i4vhvs#uvz4y$94zah(=dw2xx8a6ej8ygim#aq3%h$3*('

LOGGING['formatters']['colored'] = {
    '()':'colorlog.ColoredFormatter',
    'format': '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['musicapi']['level']='DEBUG'
LOGGING['handlers']['console']['level']='DEBUG'
LOGGING['handlers']['console']['formatter']='colored'
