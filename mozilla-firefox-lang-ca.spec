Summary:	Catalan resources for Mozilla-firefox
Summary(ca):	Recursos catalans per Mozilla-firefox
Summary(es):	Recursos catalanes para Mozilla-firefox
Summary(pl):	Katalo�skie pliki j�zykowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-ca
Version:	1.5.0.8
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca.xpi
# Source0-md5:	5570e6e51a06e2a6c9d14aaa11a92ee1
URL:		http://www.softcatala.org/projectes/mozilla/
BuildRequires:	unzip
Requires(post,postun):	mozilla-firefox >= %{version}
Requires(post,postun):	textutils
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_libdir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
Catalan resources for Mozilla-firefox.

%description -l ca
Recursos catalans per Mozilla-firefox.

%description -l es
Recursos catalanes para Mozilla-firefox.

%description -l pl
Katalo�skie pliki j�zykowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_firefoxdir}/defaults/profile}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/ca.jar $RPM_BUILD_ROOT%{_chromedir}/ca-ES.jar
sed -e 's@chrome/ca@ca-ES@' $RPM_BUILD_ROOT%{_libdir}/chrome.manifest \
	> $RPM_BUILD_ROOT%{_chromedir}/ca-ES.manifest
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_firefoxdir}/defaults/profile

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/ca-ES.jar
%{_chromedir}/ca-ES.manifest
# file conflict:
#%{_firefoxdir}/defaults/profile/*.rdf
