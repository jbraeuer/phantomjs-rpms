This repository holds files and scripts to build a PhantomJS RPM
package. This package will also include xvfb-run, so you are good to
run your headless tests.

Ingredients
- Qt 4.7: from http://dl.atrpms.net/el5-x86_64/atrpms/testing/
- xfvb-run(.sh): from xorg-x11-server-1.5.3-5.fc10.src.rpm
- xvfb init script
- PhantomJS 1.2.0: from http://code.google.com/p/phantomjs/

Licenses
- Qt 4.7: LGPL
- PhantomJS: BSD
- Xorg-X11-Server: MIT

How to prepare build environment
- build Qt 4.7 RPMS from included src.rpm OR use ./fetch-qt-rpms to download them
- yum/rpm install qt47-devel qt47-webkit qt47-webkit-devel sqlite-devel

How to build
- run ./rpm -d

Have fun!
