# -*- mode: python -*-

import platform
p = platform.system()

version = open('share/version.txt').read().strip()

a = Analysis(
    ['scripts/myonion-pyinstaller'],
    pathex=['.'],
    binaries=None,
    datas=[
        ('../share/version.txt', 'share'),
        ('../share/wordlist.txt', 'share'),
        ('../share/images/*', 'share/images'),
        ('../share/locale/*', 'share/locale'),
        ('../share/static/*', 'share/static'),
        ('../share/containers/*', 'share/containers'),
        ('../share/static/css/*', 'share/static/css'),
        ('../share/static/img/*', 'share/static/img'),
        ('../share/static/js/*', 'share/static/js'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None)

pyz = PYZ(
    a.pure, a.zipped_data,
    cipher=None)

if p == 'Darwin':
    app = BUNDLE(
        coll,
        name='MyOnion.app',
        icon='install/myonion.icns',
        bundle_identifier='com.micahflee.myonion',
        info_plist={
            'CFBundleShortVersionString': version,
            'NSHighResolutionCapable': 'True'
        }
    )
