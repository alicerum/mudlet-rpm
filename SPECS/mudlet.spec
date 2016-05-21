Name:           mudlet
Version:        3.0.0
Release:        1%{?dist}
Summary:        Crossplatform mud client

License:        GPLv2+
Group:          Amusements/Games
URL:            http://www.mudlet.org/
Source0:        Mudlet-3.0.0-delta.tar.gz
Patch0:         mudlet-3.0.0-cmake.patch
Patch1:         mudlet-3.0.0-ctelnet.patch
Patch2:         mudlet-3.0.0-lua-path.patch
Patch3:         mudlet-3.0.0-lua-global.patch
Patch4:         mudlet-3.0.0-hunspell.patch

BuildRequires:  cmake,compat-lua-devel,libzip-devel,zlib-devel,pcre-devel,yajl-devel,hunspell-devel
BuildRequires:  qt5-qtbase-devel,qt5-qtmultimedia-devel,qt5-qttools-static,boost-devel
BuildRequires:  mesa-libGLU-devel

Requires:       compat-lua,libzip,zlib,pcre,yajl,hunspell
Requires:       qt5-qtbase,qt5-qtmultimedia,qt5-qttools-static,boost
Requires:       mesa-libGLU

%description
Mudlet is a quality MUD client, designed to take mudding to a new level.

It’s a new breed of a client on the MUD scene – with an intuitive user interface, a specially designed scripting framework, and a very fast text display. Add to that cross-platform capability, an open-source development model, and you have a very likable MUD client.

%prep
%setup -n Mudlet-Mudlet-3.0.0-delta
%patch0
%patch1
%patch2
%patch3
%patch4

%build
%cmake .
make %{?_smp_mflags}

%install
%make_install
mkdir -pv %{buildroot}/usr/share/pixmaps/
cp src/icons/mudlet.png %{buildroot}/usr/share/pixmaps/
mkdir -pv %{buildroot}/usr/share/applications/
cp mudlet.desktop %{buildroot}/usr/share/applications/

%files
/usr/bin/*
/usr/share/mudlet
/usr/share/pixmaps/*
/usr/share/applications/*

%changelog
* Thu May 19 2016 wyvie <irum@redhat.com>
- Made mudlet look for mudlet-lua on absolute path.

* Tue May 17 2016 wyvie <irum@redhat.com>
- Fixed dependencies of rpm package.
