# NOTE
# - I'm installing jquery version, because then I have webserver alias already
#   setup for it
%define		plugin	photoswipe
Summary:	PhotoSwipe - The web image gallery for your mobile device
Name:		jquery-%{plugin}
Version:	3.0.4
Release:	1
License:	MIT
Group:		Applications/WWW
Source0:	https://github.com/downloads/codecomputerlove/PhotoSwipe/code.photoswipe-%{version}.zip
# Source0-md5:	c690d4d8d44c52a695ee04c813b619e7
URL:		http://www.photoswipe.com/
BuildRequires:	rpmbuild(macros) >= 1.553
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
Inspired by the iOS photo viewer and Google images for mobile,
PhotoSwipe is a HTML/CSS/JavaScript based image gallery specifically
targeting mobile devices.

The current version supports mobile handsets running WebKit based
browsers, i.e. iOS, Android and Blackberry 6.

PhotoSwipe also runs on the desktop and has been tested on Chrome,
Firefox, Safari and Internet Explorer 8 and above and in a limited
capacity on Windows Phone 7 (Mango).

%prep
%setup -qc
mv %{version}/* .

%undos -f txt,js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p code.photoswipe.jquery-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.min.js
cp -p code.photoswipe.jquery-%{version}.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}-%{version}.js
ln -s %{plugin}-%{version}.min.js $RPM_BUILD_ROOT%{_appdir}/%{plugin}.js

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MIT-license.txt README.md change.log
%{_appdir}
