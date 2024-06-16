from setuptools import setup

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='faKy',
    version='2.1.0',
    description='faKy is a Python library for text analysis. It provides functions for readability, complexity, sentiment, and statistical analysis in the scope of fake news detection.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Sandro Barres Hamers',
    author_email='sbarreshamers@gmail.com',
    packages=['faKy'],
    install_requires=[
        'numpy==1.26.0',
        'pandas==2.2.0',
        'spacy-readability==1.4.1',
        'nltk==3.8.1',
        'vaderSentiment==3.3.2',
    ],
    extras_require={
        'vader': ['vaderSentiment'],
    },
    package_data={
    'faKy': ['en_core_web_md-3.7.1/*', 'en_core_web_md-3.7.1/en_core_web_md/*'],
}
)
