%define		rc		rc2
Summary:	Development environment for children
Name:		littlewizard
Version:	1.0.0
Release:	0.rc2.1
License:	GPL v2
Group:		Development
Source0:	http://dl.sourceforge.net/littlewizard/%{name}-%{version}.tar.gz
# Source0-md5:	a68d33d34bd01f28070358809642f7c8
URL:		http://littlewizard.sourceforge.net/
#uildRequires:	
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Development environment for children. Program little wizard without using keybord, just use the drag and drop system

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
%doc AUTHORS ChangeLog README TODO NEWS
%attr(755,root,root) %{_bindir}/*
%{_includedir}/littlewizard/*
%{_datadir}/*
%{_libdir}/*
#%{_mandir}/man8/%{name}.*
