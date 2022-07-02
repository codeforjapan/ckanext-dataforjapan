ckanext-dataforjapan
====================
| ⚠️ This repository will be archived in the future, this config will no longer be maintained. Thanks for all the stars, help and brainstorms! |

CKAN extension for Data for Japan

# Install

```
$ pip install -e git+https://github.com/codeforjapan/ckanext-dataforjapan.git#egg=ckanext-dataforjapan
```
Add dataforjapan_theme into ckan.plugins in your configuration file.

```
ckan.plugins = stats text_preview recline_preview pdf_preview dataforjapan_theme
```

Then restart your web server.
