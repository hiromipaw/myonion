#!/bin/bash

ROOT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd .. && pwd )"
cd $ROOT

# deleting dist
echo Deleting dist folder
rm -rf $ROOT/dist &>/dev/null 2>&1

# build the .app
echo Building MyOnion.app
pyinstaller $ROOT/install/pyinstaller.spec
python3 $ROOT/install/get-tor-osx.py

# create a symlink of myonion-gui called myonion, for the CLI version
cd $ROOT/dist/MyOnion.app/Contents/MacOS
ln -s myonion-gui myonion
cd $ROOT

if [ "$1" = "--release" ]; then
  mkdir -p dist
  APP_PATH="$ROOT/dist/MyOnion.app"
  PKG_PATH="$ROOT/dist/MyOnion.pkg"
  IDENTITY_NAME_APPLICATION="Developer ID Application: Hiro"
  IDENTITY_NAME_INSTALLER="Developer ID Installer: Hiro"

  echo "Codesigning the app bundle"
  codesign --deep -s "$IDENTITY_NAME_APPLICATION" "$APP_PATH"

  echo "Creating an installer"
  productbuild --sign "$IDENTITY_NAME_INSTALLER" --component "$APP_PATH" /Applications "$PKG_PATH"

  echo "Cleaning up"
  rm -rf "$APP_PATH"

  echo "All done, your installer is in: $PKG_PATH"
fi
