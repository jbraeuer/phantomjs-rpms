This repository holds files and scripts to build a PhantomJS RPM
package. This package will also include xvfb-run, so you are good to
run your headless tests.

# Ingredients
- Qt 4.7: from http://dl.atrpms.net/el5-x86_64/atrpms/testing/
- xfvb-run(.sh): from xorg-x11-server-1.5.3-5.fc10.src.rpm
- xvfb init script
- PhantomJS: from http://code.google.com/p/phantomjs/

# Licenses
- Qt 4.7: LGPL
- PhantomJS: BSD
- Xorg-X11-Server: MIT

# How to prepare build environment
- build Qt 4.7 RPMS from included src.rpm OR use ./fetch-qt-rpms to download them
- yum/rpm install qt47-devel qt47-webkit qt47-webkit-devel sqlite-devel

# How to build
- source code is included for PhantomJS 1.1, 1.2 and 1.3
- for PhantomJS 1.4.x and 1.5 use `fetch-phantomjs $version`
- `./rpm SPECS/phantomjs-$version.spec`

# Build branches
- use `fetch-phantomjs` script to fetch sources from branches
- modify .spec to suit your needs

Have fun!
Jens Braeuer
