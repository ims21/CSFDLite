from distutils.core import setup

pkg = 'Extensions.CSFDLite'
setup (name = 'enigma2-plugin-extensions-csfdlite',
	version = '1.6.06',
	description = 'display event info from csfd server',
	packages = [pkg],
	package_dir = {pkg: 'plugin'},
	package_data = {pkg: ['*.png', '*.xml']},
	)
