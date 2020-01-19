from setuptools import setup

setup(name='python_workflow',
      version='1.0',
      description='Python workflow for data science projects',
      url='https://github.com/pradasub/test_workflows',
      author='Dr Prada',
      author_email='prachandasubedi@gmail.com',
      license='MIT',
      packages=['workflow'],
      install_requires = ['pandas',
          'numpy',
          'seaborn',
          'sklearn',
          'collections',
          'imblearn',
          'keras',
          'matplotlib',
          'lime',
          'lime.lime_tabular',
          'treeinterpreter']
      zip_safe=False)
