Summary: Interpreter for Scott Adams format text adventure games
Name: scottfree
Version: 1.14
Release: 2%{?dist}
License: GPL
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
* Mon Oct 09 2006 Andrea Musuruane <musuruan@gmail.com> 1.14-2%{?dist}
- changed patch name to lowercase to match RPM name
- changed group to "Amusements/Games"
- added %%{?_smp_mflags} to make invocation to speed up SMP builds

* Sat Oct 07 2006 Andrea Musuruane <musuruan@gmail.com> 1.14-1%{?dist}
- initial package based on the old RH 5.2 package and a patch from Debian

