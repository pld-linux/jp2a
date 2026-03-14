Summary:	jp2a - convert JPEG/PNG/WebP images to ASCII
Summary(pl.UTF-8):	jp2a - konwersja obrazków JPEG/PNG/WebP do ASCII
Name:		jp2a
Version:	1.3.3
Release:	1
License:	GPL v2
Group:		Applications
Source0:	https://github.com/Talinx/jp2a/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	577a9176984bb5830a2ff5fa693d031b
URL:		https://github.com/Talinx/jp2a
BuildRequires:	curl-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libwebp-devel
BuildRequires:	ncurses-devel
BuildRequires:	rpmbuild(macros) >= 1.228
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jp2a is a small utility that converts JPEG, PNG and WebP images to
ASCII. It's written in C.

%description -l pl.UTF-8
jp2a jest małym narzędziem, które konwertuje pliki JPEG, PNG i WebP do
ASCII. Napisany został w C.

%package -n bash-completion-jp2a
Summary:	Bash completion for jp2a
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów dla jp2a
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-jp2a
Bash completion for jp2a.

%description -n bash-completion-jp2a -l pl.UTF-8
Bashowe dopełnianie parametrów dla jp2a.

%package -n zsh-completion-jp2a
Summary:	Zsh completion for jp2a
Summary(pl.UTF-8):	Dopełnianie parametrów dla jp2a w zsh
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh
BuildArch:	noarch

%description -n zsh-completion-jp2a
Zsh completion for jp2a.

%description -n zsh-completion-jp2a -l pl.UTF-8
Dopełnianie parametrów dla jp2a w zsh.

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

%files -n bash-completion-jp2a
%defattr(644,root,root,755)
%{bash_compdir}/jp2a

%files -n zsh-completion-jp2a
%defattr(644,root,root,755)
%{zsh_compdir}/_jp2a
