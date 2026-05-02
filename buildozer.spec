[app]
title = MyPythonAPK
package.name = myapk
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Faster build settings
android.api = 33
android.minapi = 21