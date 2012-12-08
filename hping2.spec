%define beta rc3

Summary:	TCP/IP packet assembler/analyzer
Name:		hping2
Version:	2.0.0
Release:	%mkrel 0.%{beta}.14
License:	GPL
Group:		Monitoring
URL:		http://www.hping.org/
Source0:	http://www.hping.org/hping%{version}-%{beta}.tar.gz
Patch0:		30_bytesex.diff
Patch1:		hping2.0.0-rc3-hz-250.patch
Patch2:		hping2-LDFLAGS.diff
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
hping is a command-line oriented TCP/IP packet assembler/analyzer. The
interface is very similar to the ping(8) unix command, with many extensions.
It supports TCP, UDP, ICMP and RAW-IP protocols. A scripting language is under
developing.

%prep

%setup -q -n %{name}-%{beta}
%patch0 -p1 -b .endian
%patch1 -p1 -b .hz250
%patch2 -p0 -b .LDFLAGS

%build
%configure2_5x
%make CCOPT="%{optflags}" LDFLAGS="%{ldflags}"

%install
rm -rf %{buildroot}

install -d 755 %{buildroot}%{_sbindir}
install -d 755 %{buildroot}%{_mandir}/man8
install -m 755 hping2 %{buildroot}%{_sbindir}
install -m 644 docs/hping2.8 %{buildroot}%{_mandir}/man8
cd %{buildroot}%{_sbindir} && ln -s hping2 hping

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc BUGS CHANGES COPYING INSTALL KNOWN-BUGS TODO
%{_sbindir}/*
%{_mandir}/man8/hping2.8.*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.rc3.12mdv2011.0
+ Revision: 665439
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.rc3.11mdv2011.0
+ Revision: 605878
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.rc3.10mdv2010.1
+ Revision: 519009
- rebuild

* Fri Sep 25 2009 Olivier Blin <oblin@mandriva.com> 2.0.0-0.rc3.9mdv2010.0
+ Revision: 449057
- fix endian test by using endian.h, better than checking for every
  arch in the world (from Arnaud Patard, patch from Debian)

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.0-0.rc3.8mdv2010.0
+ Revision: 425151
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.rc3.7mdv2009.1
+ Revision: 316761
- use %%ldflags

* Tue Jul 29 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.rc3.6mdv2009.0
+ Revision: 253201
- upstream source is gzipped
- new url
- spec file clean

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-0.rc3.5mdv2009.0
+ Revision: 221344
- rebuild

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.0.0-0.rc3.4mdv2008.1
+ Revision: 150276
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed Mar 07 2007 Oden Eriksson <oeriksson@mandriva.com> 2.0.0-0.rc3.3mdv2007.0
+ Revision: 134428
- Import hping2

* Sun Dec 11 2005 Olivier Thauvin <nanardon@mandriva.org> 2.0.0-0.rc3.3mdk
- from Anssi Hannula <anssi.hannula@gmail.com>
  - Patch1: add 250Hz to the kernel HZ array (default since 2.6.13) (#17537)

* Sat Apr 09 2005 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.0.0-0.rc3.2mdk
- Patch0: add x86_64 as little endian

* Tue May 04 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.0.0-0.rc3.1mdk
- 2.0.0-rc3

