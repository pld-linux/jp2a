Summary:	jp2a
Summary(pl):	jp2a
Name:		jp2a
Version:	0.9.8
Release:	1
License:	GPL v2
Group:		Applications
Source0:	http://dl.sourceforge.net/jp2a/%{name}-%{version}.tar.bz2
# Source0-md5:	8067ab28dd5ade10be659866908d7b35
URL:		http://jp2a.sourceforge.net/
BuildRequires:	libjpeg-devel
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jp2a is a small utility that converts JPG images to ASCII. It's
written in C.

%description -l pl
jp2a jest ma³ym narzêdziem, które konwertuje pliki JPEG do ASCII.
Napisany zosta³ w C.

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
%{_mandir}/man1/%{name}*
