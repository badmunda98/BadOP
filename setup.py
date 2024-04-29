
from setuptools import setup, find_packages
from os import path
base_dir = path.abspath(path.dirname(__file__))
setup(
  name = 'BadOP',        
  packages = ['BadOP'],
  include_package_data=True,
  version = '1.2',    
  license='MIT',     
  description = 'BadOP Logo Generator', 
  author = 'BAD',                  
  author_email = 'sukhwinderwarval50@gmail.com',     
  url = 'https://github.com/badmunda98/BadOP',   
  download_url = 'https://github.com/badmunda98/BadOP/archive/1.2.tar.gz',    
  keywords = ['BadOP', 'logo', 'generator'], 
  install_requires=[           
          'pillow',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',  
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)
