Summary:	Development environment for children
Summary(pl.UTF-8):	Środowiko programistyczne dla dzieci
Name:		littlewizard
Version:	1.2.2
Release:	3
License:	GPL v2+
Group:		Development/Tools
Source0:	http://downloads.sourceforge.net/littlewizard/%{name}-%{version}.tar.gz
# Source0-md5:	1a6f4405418c8b55b29de0ce5934d73f
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-pixmapsdir.patch
Patch2:		%{name}-desktop.patch
URL:		http://littlewizard.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.4
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Development environment for children. Program little wizard without
using keybord, just use the drag and drop system.

%description -l pl.UTF-8
Little wizard ("mały czarodziej") to środowisko programistyczne dla
dzieci. Programuje się w nim bez użycia klawiatury, korzystając z
systemu "złap i upuść".

%package devel
Summary:	Header files for littlewizard
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek littlewizard
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
littlewizard header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek littlewizard.

%package static
Summary:	Static libraries for littlewizard
Summary(pl.UTF-8):	Statyczne biblioteki dla littlewizard
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
littlewizard static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne dla littlewizard.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%update_icon_cache hicolor
%update_mime_database

%postun
/sbin/ldconfig
%update_icon_cache hicolor
%update_mime_database

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COMPATIBILITY ChangeLog README TODO
%attr(755,root,root) %{_bindir}/littlewizard
%attr(755,root,root) %{_bindir}/littlewizardtest
%attr(755,root,root) %{_libdir}/liblanguage.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblanguage.so.0
%attr(755,root,root) %{_libdir}/liblw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/liblw.so.0
%{_pixmapsdir}/*
%{_desktopdir}/littlewizard.desktop
%{_datadir}/%{name}
%{_datadir}/mime/packages/littlewizard.xml
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/liblanguage.so
%attr(755,root,root) %{_libdir}/liblw.so
%{_libdir}/liblanguage.la
%{_libdir}/liblw.la
%{_includedir}/littlewizard

%files static
%defattr(644,root,root,755)
%{_libdir}/liblanguage.a
%{_libdir}/liblw.a
