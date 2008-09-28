%define		_lang		ca
Summary:	Catalan resources for Mozilla-firefox
Summary(ca.UTF-8):	Recursos catalans per Mozilla-firefox
Summary(es.UTF-8):	Recursos catalanes para Mozilla-firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-%{_lang}
Version:	3.0.2
Release:	1
License:	GPL
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/%{_lang}.xpi
# Source0-md5:	d274b22e13c8247e8e7c02f89a3a2e41
URL:		http://www.softcatala.org/projectes/mozilla/
BuildRequires:	unzip
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_datadir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
Catalan resources for Mozilla-firefox.

%description -l ca.UTF-8
Recursos catalans per Mozilla-firefox.

%description -l es.UTF-8
Recursos catalanes para Mozilla-firefox.

%description -l pl.UTF-8
Katalońskie pliki językowe dla Mozilli-firefox.

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
