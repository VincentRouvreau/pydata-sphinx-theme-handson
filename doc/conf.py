project = 'Lumache'
copyright = '2023, Me'
author = 'Me'
release = '0.0.0'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'pydata_sphinx_theme'

html_static_path = ['_static']

html_css_files = [
    'custom.css',
]

html_theme_options = {
   "logo": {
      "image_light": "logo-light.png",
      "image_dark": "logo-dark.png",
   }
}