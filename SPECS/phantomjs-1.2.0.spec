Summary: PhantomJS is a headless WebKit with JavaScript API
Name: phantomjs
Version: 1.2.0
Release: 8
License: BSD
Group: unknown
URL: http://code.google.com/p/phantomjs/
Source0: %{name}-%{version}-source.zip
Source1: xvfb-run.sh
Source2: xvfb.init
BuildRequires: qt47-devel
BuildRequires: qt47-webkit-devel
BuildRequires: sqlite-devel
Requires: dpkg
Requires: xorg-x11-xauth
Requires: xorg-x11-server-Xvfb
Requires: xorg-x11-server-Xorg
Requires: xorg-x11-fonts-100dpi
Requires: xorg-x11-fonts-75dpi
Requires: xorg-x11-fonts-ISO8859-1-100dpi
Requires: xorg-x11-fonts-ISO8859-1-75dpi
Requires: xorg-x11-fonts-ISO8859-14-100dpi
Requires: xorg-x11-fonts-ISO8859-14-75dpi
Requires: xorg-x11-fonts-ISO8859-15-100dpi
Requires: xorg-x11-fonts-ISO8859-15-75dpi
Requires: xorg-x11-fonts-ISO8859-2-100dpi
Requires: xorg-x11-fonts-ISO8859-2-75dpi
Requires: xorg-x11-fonts-ISO8859-9-100dpi
Requires: xorg-x11-fonts-ISO8859-9-75dpi
Requires: xorg-x11-fonts-Type1
Requires: xorg-x11-fonts-base
Requires: xorg-x11-fonts-cyrillic
Requires: xorg-x11-fonts-ethiopic
Requires: xorg-x11-fonts-misc
Requires: xorg-x11-fonts-syriac
Requires: xorg-x11-fonts-truetype
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description

%prep
%setup -q

%build
qmake-qt47
make

%install
rm -rf "$RPM_BUILD_ROOT"

mkdir -p "$RPM_BUILD_ROOT/usr/bin"
cp bin/* "$RPM_BUILD_ROOT/usr/bin"
cp %SOURCE1 "$RPM_BUILD_ROOT/usr/bin/xvfb-run"
find "$RPM_BUILD_ROOT/usr/bin" -type f -exec chmod 755 '{}' ';'

mkdir -p "$RPM_BUILD_ROOT/usr/share/doc/%{name}"
cp -r examples "$RPM_BUILD_ROOT/usr/share/doc/%{name}/"

mkdir -p "$RPM_BUILD_ROOT/etc/rc.d/init.d"
cp %SOURCE2 "$RPM_BUILD_ROOT/etc/rc.d/init.d/xvfb"
chmod 755 "$RPM_BUILD_ROOT/etc/rc.d/init.d/xvfb"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/etc/rc.d/init.d/xvfb
/usr/bin/phantomjs
/usr/bin/xvfb-run
/usr/share/doc/%{name}/examples

%changelog
* Thu Sep 22 2011 Jens Braeuer <jens@numberfour.eu> - 
- Initial build.

