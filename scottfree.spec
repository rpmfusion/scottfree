Name:    scottfree
Version: 1.14
Release: 13%{?dist}
Summary: Interpreter for Scott Adams format text adventure games

License: GPLv2+
URL:     http://ifarchive.org/if-archive/scott-adams/interpreters/scottfree/
Source0: http://ifarchive.org/if-archive/scott-adams/interpreters/scottfree/ScottFree.tar.gz
# Man page taken from Debian
Source1: %{name}.6
Patch0:  %{name}-1.14-Makefile.patch
Patch1:  %{name}-1.14-includes.patch

BuildRequires: ncurses-devel 


%description
ScottFree is an interpreter for Scott-Adams-format text adventure games
(remember those?). It reads and executes TRS-80 format data files.

Most Adventure International Games are distributed as shareware and are 
available from http://ifarchive.org/if-archive/scott-adams/


%prep
%autosetup -c -p1

# Fix file permissions
chmod 644 *


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
%make_install

# Install man page
install -d %{buildroot}%{_mandir}/man6
install -p -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man6/


%files
%{_bindir}/%{name}
%{_mandir}/man6/%{name}.6*
%doc README Definition


%changelog
* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.14-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 02 2017 Andrea Musuruane <musuruan@gmail.com> - 1.14-12
- Fixed missing debuginfo
- Added URL tag
- Updated Source0 tags
- Updated description
- Added man page from Debian
- Dropped Group tag

* Fri Sep 01 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.14-11
- Disable debuginfo

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.14-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.14-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.14-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.14-7
- Mass rebuilt for Fedora 19 Features

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 1.14-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

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

