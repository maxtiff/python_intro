"""

Download.py


"""
#	Import functions from EIA module
import eia
#	Import settings file
import settings

manifest = eia.download_file(settings.url,settings.manifest,settings.PROXIES, settings.HEADERS)
eia.save_manifest(manifest, settings.manifest)

data = eia.download_file(settings.url,settings.zip_archive,settings.PROXIES,settings.HEADERS)
eia.save_json(settings.raw_data, settings.json_obj, data)

eia.decode_json(settings.json_obj)
