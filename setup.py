from setuptools import setup

setup(name='git-vanity',
    version='0.1',
    description='vanity leaderboard for git',
    url='http://github.com/intuition-app/frontend',
    author='Brian Brunner',
    author_email='brian@intuition.app',
    license='MIT',
    packages=['gitvanity'],
    package_data={'gitvanity': ['gitvanity/*.csv', 'gitvanity/templates/*.html']},
    include_package_data=True,
    install_requires=[
        'Click==7.0',
        'GitPython==2.1.11',
        'Jinja2==2.10'
    ],
    scripts=['bin/git-vanity'],
    zip_safe=False)
