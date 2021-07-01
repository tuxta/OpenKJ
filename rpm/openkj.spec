Name:           openkj
Version:		2.1.6
Release:        5%{?dist}
Summary:        Karaoke show hosting software

License:        GPL
URL:            https://openkj.org
Source0:	https://github.com/OpenKJ/OpenKJ/releases/download/2.1.6-unstable/openkj-2.1.6-unstable.tar.gz

BuildRequires:  cmake qt5-qtbase-devel qt5-qtsvg-devel qt5-qtmultimedia-devel gstreamer1-devel gstreamer1-plugins-base-devel taglib-devel taglib-extras-devel git
Requires:       qt5-qtbase qt5-qtsvg qt5-qtmultimedia gstreamer1 gstreamer1-plugins-good gstreamer1-plugins-bad-free gstreamer1-plugins-ugly-free unzip gstreamer1-libav taglib taglib-extras google-roboto-fonts google-roboto-mono-fonts

%description
Karaoke hosting software targeted at professional KJ's.  Includes rotation management, break music player,
key changer, and all of the various bits and pieces required to host karaoke.

%undefine _hardened_build

%prep
%setup

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files
/usr/bin/openkj
/usr/share/applications/openkj.desktop
/usr/share/pixmaps/okjicon.svg

%changelog
* Tue Aug 15 2017 T. Isaac Lightburn <isaac@hozed.net>
- 
