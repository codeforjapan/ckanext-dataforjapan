''' plugin.py
'''
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

class DataForJapanThemePlugin(plugins.SingletonPlugin):
  '''
      CKAN theme plugin for Data for Japan
  '''
  plugins.implements(plugins.IConfigurer)

  def update_config(self, config):
    toolkit.add_template_directory(config, 'templates')
    toolkit.add_public_directory(config, 'public')
