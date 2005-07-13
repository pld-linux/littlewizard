%define		_rc		rc2
Summary:	Development environment for children
Summary(pl):	¦rodowiko programistyczne dla dzieci
Name:		littlewizard
Version:	1.0.0
Release:	0.%{_rc}.1
License:	GPL v2
Group:		Development
Source0:	http://dl.sourceforge.net/littlewizard/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	a68d33d34bd01f28070358809642f7c8
URL:		http://littlewizard.sourceforge.net/
BuildRequires:	pkgconfig
BuildRequires:	libxml2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Development environment for children. Program little wizard without
using keybord, just use the drag and drop system.

%description -l pl
¦rodowisko programistyczne dla dzieci. Program ma³y czarodziej u¿ywa
siê bez klawiatury, korzystaj±c z systemu "z³ap i upu¶æ".

%package devel
Summary:	Header file and libraries for littlewizard
Summary(pl):	Pliki nag³ówkowe i biblioteki dla littlewizard
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
littlewizard header files and librarie.s

%description devel -l pl
Pliki nag³ówkowe i biblioteki dla littlewizard.

%package static
Summary:	Static libraries for littlewizard
Summary(pl):	Statyczne biblioteki dla littlewizard
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description static
littlewizard static libraries.

%description static -l pl
Biblioteki statyczne dla littlewizard.

%prep
%setup -q -n %{name}-%{version}%{_rc}

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
# TODO: fix it
%{_datadir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/littlewizard
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
