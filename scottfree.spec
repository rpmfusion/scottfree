Summary: Interpreter for Scott Adams format text adventure games
Name: scottfree
Version: 1.14
Release: 5%{?dist}
License: GPLv2+
Group: Amusements/Games
Source: ftp://ftp.gmd.de/if-archive/scott-adams/ScottFree.tar.gz
Patch: scottfree-1.14.diff
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: ncurses-devel 

%description
ScottFree is an interpreter for Scott-Adams-format text adventure games
(remember those?). It reads and executes TRS-80 format data files.

Most Adventure International Games are distributed as shareware and are 
available from ftp://ftp.gmd.de/if-archive/scott-adams/

%prep
%setup -q -c
%patch -p1
chmod 644 *

%build
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/scottfree
%doc README Definition

%changelog
* Sun Mar 29 2009 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 1.14-5
- rebuild for new F11 features

* Mon Aug 11 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 1.14-4
- rebuild to fix early trouble on RPM Fusions x86 builders

* Fri Nov 02 2007 Andrea Musuruane <musuruan@gmail.com> 1.14-3
- changed license due to new guidelines
- removed %%{?dist} tag from changelog

* Mon Oct 09 2006 Andrea Musuruane <musuruan@gmail.com> 1.14-2
- changed patch name to lowercase to match RPM name
- changed group to "Amusements/Games"
- added %%{?_smp_mflags} to make invocation to speed up SMP builds

* Sat Oct 07 2006 Andrea Musuruane <musuruan@gmail.com> 1.14-1
- initial package based on the old RH 5.2 package and a patch from Debian

