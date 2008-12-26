%define		_lang		ca
Summary:	Catalan resources for Firefox
Summary(ca.UTF-8):	Recursos catalans per Firefox
Summary(es.UTF-8):	Recursos catalanes para Firefox
Summary(pl.UTF-8):	Katalońskie pliki językowe dla Firefoksa
Name:		mozilla-firefox-lang-%{_lang}
Version:	3.0.5
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://releases.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/%{_lang}.xpi
# Source0-md5:	2f07344aa1c82ef333b4c2e8f85e4bb5
URL:		http://www.softcatala.org/projectes/mozilla/
BuildRequires:	unzip
Requires:	mozilla-firefox >= %{version}
Provides:	mozilla-firefox-lang-resources = %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_firefoxdir	%{_datadir}/mozilla-firefox
%define		_chromedir	%{_firefoxdir}/chrome

%description
Catalan resources for Firefox.

%description -l ca.UTF-8
Recursos catalans per Firefox.

%description -l es.UTF-8
Recursos catalanes para Firefox.

%description -l pl.UTF-8
Katalońskie pliki językowe dla Firefoksa.

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
