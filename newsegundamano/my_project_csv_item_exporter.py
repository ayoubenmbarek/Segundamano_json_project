from scrapy.conf import settings
from scrapy.contrib.exporter import CsvItemExporter

class MyProjectCsvItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        delimiter = settings.get('CSV_DELIMITER', ',')
        kwargs['delimiter'] = delimiter

        fields_to_export = settings.get('FEED_EXPORT_FIELDS', [])#FEED_EXPORT_FIELDS #FEED_EXPORT_FIELDS
        if fields_to_export :
        	kwargs['fields_to_export'] = fields_to_export

        super(MyProjectCsvItemExporter, self).__init__(*args, **kwargs)
