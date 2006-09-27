Summary:	Development environment for children
Summary(pl):	¦rodowiko programistyczne dla dzieci
Name:		littlewizard
Version:	1.1.4
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/littlewizard/%{name}-%{version}.tar.gz
# Source0-md5:	b3dad856d0931f4f6846bf8a523792f9
Patch0:		%{name}-Makefile.patch
URL:		http://littlewizard.sourceforge.net/
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libxml2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Development environment for children. Program little wizard without
using keybord, just use the drag and drop system.

%description -l pl
Little wizard ("ma³y czarodziej") to ¶rodowisko programistyczne dla
dzieci. Programuje siê je bez klawiatury, korzystaj±c z systemu "z³ap
i upu¶æ".

%package devel
Summary:	Header files for littlewizard
Summary(pl):	Pliki nag³ówkowe bibliotek littlewizard
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
littlewizard header files.

%description devel -l pl
Pliki nag³ówkowe bibliotek littlewizard.

%package static
Summary:	Static libraries for littlewizard
Summary(pl):	Statyczne biblioteki dla littlewizard
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
littlewizard static libraries.

%description static -l pl
Biblioteki statyczne dla littlewizard.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}/* $RPM_BUILD_ROOT%{_pixmapsdir}

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
%{_datadir}/%{name}

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/littlewizard

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
