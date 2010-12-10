%define	name	id3ed
%define	version	1.10.4
%define release	 %mkrel 8

Summary:	Edit id3v1 description tags in mpeg3 files
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://www.azstarnet.com/~donut/programs.html
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
id3ed edits the "id3" tag for mpeg layer3 files. The mpeg3
specification does not provide any method for storing song
information, however the id3 tag has become a standard method
for doing this, and most mp3 players can read the tag. It will
not cause any errors in players that do not support it.
The tag is 128 bytes long and is located at the end of the file.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
install -m755 id3ed -D $RPM_BUILD_ROOT%{_bindir}/id3ed
install -m755 id3ed.1 -D $RPM_BUILD_ROOT%{_mandir}/man1/id3ed

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc COPYING Changelog README
%{_bindir}/*
%{_mandir}/man1/*

