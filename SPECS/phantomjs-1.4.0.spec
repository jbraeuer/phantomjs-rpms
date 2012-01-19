Summary: PhantomJS is a headless WebKit with JavaScript API
Name: phantomjs
Version: 1.4.0
Release: 1%{?dist}
License: BSD
Group: unknown
URL: http://code.google.com/p/phantomjs/
Source0: %{name}-%{version}-source.tar.gz
Source1: xvfb-run.sh
BuildRequires: qt47-devel
BuildRequires: qt47-webkit-devel
BuildRequires: sqlite-devel
Requires: qt47
Requires: qt47-webkit
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
%if 0%{?el5}
Requires: xorg-x11-fonts-syriac
Requires: xorg-x11-fonts-truetype
%endif
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
%if 0%{?el5}
cp %SOURCE1 "$RPM_BUILD_ROOT/usr/bin/xvfb-run"
%endif
find "$RPM_BUILD_ROOT/usr/bin" -type f -exec chmod 755 '{}' ';'

mkdir -p "$RPM_BUILD_ROOT/usr/share/doc/%{name}"
cp -r examples "$RPM_BUILD_ROOT/usr/share/doc/%{name}/"

find $RPM_BUILD_ROOT -type f -name Info.plist | xargs rm -f 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
/usr/bin/phantomjs
/usr/share/doc/%{name}/examples
%if 0%{?el5}
/usr/bin/xvfb-run
%endif

%changelog
* Thu Jan 19 2012 Kai Inkinen <kai.inkinen@gmail.com> - 1.4.1-1
- Package PhantomJS 1.4.1. Tested on el5 only. 

* Thu Jan 19 2012 Kai Inkinen <kai.inkinen@gmail.com> - 1.4.0-1
- Package PhantomJS 1.4.0. Tested on el5 only. 

* Tue Sep 27 2011 Jens Braeuer <jens@numberfour.eu> - 1.3.0-6
- Package 1.3.0/Water Lily for SL6.1. Tested on el5 and el6 only.

* Thu Sep 22 2011 Jens Braeuer <jens@numberfour.eu> - 
- Initial build.

