%define	name	id3ed
%define	version	1.10.4
%define release	 9

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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10.4-8mdv2011.0
+ Revision: 619598
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.10.4-7mdv2010.0
+ Revision: 429493
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.10.4-6mdv2009.0
+ Revision: 247192
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.10.4-4mdv2008.1
+ Revision: 126975
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import id3ed


* Sun Jan 23 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.10.4-4mdk
- rebuild for new readline
- fix summary-ended-with-dot
- cosmetics

* Fri Jun 11 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.10.4-3mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.10.4-2mdk
- rebuild

* Fri Jan 10 2003 Götz Waschk <waschk@linux-mandrake.com> 1.10.4-1mdk
- drop patch
- new version

* Mon Jul 29 2002 Götz Waschk <waschk@linux-mandrake.com> 1.10.3-3mdk
- gcc 3.2 build

* Thu Jul 25 2002 Götz Waschk <waschk@linux-mandrake.com> 1.10.3-2mdk
- fix description for rpmlint
- gcc 3.1.1 patch

* Tue Oct 02 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.10.3-1mdk
- 1.10.3

* Fri Jan 12 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.10.2-1mdk
- updated to 1.10.2

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.3-3mdk
- BM

* Fri Apr 28 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.3-2mdk
- fix group
- fix files section

* Thu Feb 24 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build

* Fri Mar 26 1999 Ryan Weaver <ryanw@infohwy.com>
  [id3ed-1.3-1]
- Initial RPM Build.
- 03/23/1999 - 1.3
- Removed a debug printf that sneaked into the release.
- Added -l to show known genres.
- Added support to set genre by name as well as number.

- 03/22/1999 - 1.2
- Added -SNAYCG selection of which tags you want to edit.
- Added optional use of readline library for input.
  (Tested with Readline 4.0)  Comment the appropriate
  lines in the Makefile if you don't want it.

- 12/03/1998 - 1.1
- Added command line default value patch from Peter Karlsson <pk@abc.se>
- Added -q(uiet) command line param.

- 02/24/1998 - 1.0 - initial release

