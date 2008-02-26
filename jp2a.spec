Summary:	jp2a - convert JPEG images to ASCII
Summary(pl.UTF-8):	jp2a - konwersja obrazków JPEG do ASCII
Name:		jp2a
Version:	1.0.6
Release:	2
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/jp2a/%{name}-%{version}.tar.bz2
# Source0-md5:	3febc9c404a9e45ffcb36924861ddd33
URL:		http://jp2a.sourceforge.net/
BuildRequires:	curl-devel
BuildRequires:	libjpeg-devel
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jp2a is a small utility that converts JPEG images to ASCII. It's
written in C.

%description -l pl.UTF-8
jp2a jest małym narzędziem, które konwertuje pliki JPEG do ASCII.
Napisany został w C.

%prep
%setup -q

%build
%configure
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/jp2a
%{_mandir}/man1/%{name}.1*
