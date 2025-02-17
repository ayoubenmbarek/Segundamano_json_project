# -*- coding: utf-8 -*-

# Scrapy settings for newsegundamano project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'newsegundamano'

SPIDER_MODULES = ['newsegundamano.spiders']
NEWSPIDER_MODULE = 'newsegundamano.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'newsegundamano (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

FEED_EXPORTERS = {                                                                                                                                                 
        'csv': 'newsegundamano.my_project_csv_item_exporter.MyProjectCsvItemExporter',                                                                                    
        'csv': 'newsegundamano.exporters.QuoteAllCsvItemExporter',                                                                                                        
    }
SPLASH_URL = 'http://127.0.0.1:8050'
FEED_EXPORT_FIELDS = ["ANNONCE_LINK", "FROM_SITE", "ID_CLIENT", "ANNONCE_DATE", "ACHAT_LOC", "MAISON_APT", "CATEGORIE", "NEUF_IND", "NOM", "ADRESSE","CP","VILLE",       "QUARTIER", "DEPARTEMENT", "REGION", "PROVINCE", "ANNONCE_TEXT", "ETAGE", "NB_ETAGE", "LATITUDE", "LONGITUDE", "M2_TOTALE", "SURFACE_TERRAIN", "NB_GARAGE", "PHOTO", "PIECE", "PRIX", "PRIX_M2", "URL_PROMO", "PAYS_AD", "PRO_IND", "SELLER_TYPE", "MINI_SITE_URL", "MINI_SITE_ID", "AGENCE_NOM", "AGENCE_ADRESSE", "AGENCE_VILLE", "AGENCE_DEPARTEMENT", "EMAIL", "WEBSITE", "AGENCE_TEL", "AGENCE_TEL_2", "AGENCE_TEL_3", "AGENCE_TEL_4", "AGENCE_FAX", "AGENCE_CONTACT", "PAYS_DEALER", "FLUX", "SITE_SOCIETE_URL", "SITE_SOCIETE_ID", "SITE_SOCIETE_NAME", "SPIR_ID"] 


CSV_DELIMITER = ";"

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
#    'newsegundamano.middlewares.NewsegundamanoSpiderMiddleware': 543,
     'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'


# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'newsegundamano.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'newsegundamano.pipelines.NewsegundamanoPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 0
HTTPCACHE_DIR = 'httpcache'
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'

