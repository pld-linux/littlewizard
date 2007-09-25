Summary:	Development environment for children
Summary(pl.UTF-8):	Środowiko programistyczne dla dzieci
Name:		littlewizard
Version:	1.1.5
Release:	1
License:	GPL v2+
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/littlewizard/%{name}-%{version}.tar.gz
# Source0-md5:	37993a3046142e604a3141bc68c51987
Patch0:		%{name}-Makefile.patch
Patch1:		%{name}-pixmapsdir.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-separatelibs.patch
URL:		http://littlewizard.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Development environment for children. Program little wizard without
using keybord, just use the drag and drop system.

%description -l pl.UTF-8
Little wizard ("mały czarodziej") to środowisko programistyczne dla
dzieci. Programuje się je bez klawiatury, korzystając z systemu "złap
i upuść".

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
%patch3 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install littlewizard.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/littlewizard

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
