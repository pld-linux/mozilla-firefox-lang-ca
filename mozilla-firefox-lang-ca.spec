Summary:	Catalan resources for Mozilla-firefox
Summary(ca):	Recursos catalans per Mozilla-firefox
Summary(es):	Recursos catalanes para Mozilla-firefox
Summary(pl):	Kataloñskie pliki jêzykowe dla Mozilli-firefox
Name:		mozilla-firefox-lang-ca
Version:	1.0.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/ca-AD.xpi
# Source0-md5:	82273f41c053dcaa32fbd8d602eced4a
Source1:	%{name}-installed-chrome.txt
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
Kataloñskie pliki jêzykowe dla Mozilli-firefox.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_firefoxdir}/defaults/profile}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_firefoxdir}/defaults/profile

install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_firefoxdir}/chrome/*-installed-chrome.txt >%{_firefoxdir}/chrome/installed-chrome.txt

%postun
umask 022
cat %{_firefoxdir}/chrome/*-installed-chrome.txt >%{_firefoxdir}/chrome/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/ca-AD.jar
%{_chromedir}/%{name}-installed-chrome.txt
# file conflict:
#%{_firefoxdir}/defaults/profile/*.rdf
