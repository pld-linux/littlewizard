%define		rc		rc2
Summary:	Development environment for children
Summary(pl):	¦rodowiko programistyczne dla dzieci
Name:		littlewizard
Version:	1.0.0rc2
Release:	0.1
License:	GPL v2
Group:		Development
Source0:	http://dl.sourceforge.net/littlewizard/%{name}-%{version}.tar.gz
# Source0-md5:	a68d33d34bd01f28070358809642f7c8
URL:		http://littlewizard.sourceforge.net/
#BuildRequires: 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Development environment for children. Program little wizard without
using keybord, just use the drag and drop system.

%description -l pl
¦rodowisko programistyczne dla dzieci. Program ma³y czarodziej u¿ywa
siê bez klawiatury, korzystaj±c z systemu "z³ap i upu¶æ".

%prep
%setup -q

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
%{_includedir}/littlewizard/*
%{_datadir}/*
%{_libdir}/*
#%{_mandir}/man8/%{name}.*
