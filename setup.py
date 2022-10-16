from distutils.core import setup
import setup_translate

pkg = 'Extensions.CSFDLite'
setup(name = 'enigma2-plugin-extensions-csfdlite',
	version = '1.6',
	description = 'display event info from csfd server',
	packages = [pkg],
	package_dir = {pkg: 'plugin'},
	)
