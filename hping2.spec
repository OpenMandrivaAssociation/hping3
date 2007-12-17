%define name		hping2
%define version		2.0.0
%define beta		rc3
%define rel %mkrel 3
%define release		0.%{beta}.%rel
%define summary		TCP/IP packet assembler/analyzer

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{summary}
License:	GPL
Group:		Monitoring
Source:		http://www.kyuzz.org/antirez/hping-src/%{name}.0.0-%{beta}.tar.bz2
Patch0: hping2.endianamd64.patch
Patch1:	hping2.0.0-rc3-hz-250.patch
URL:		http://www.kyuzz.org/antirez/hping.html

%description
hping is a command-line oriented TCP/IP packet assembler/analyzer. The 
interface is very similar to the ping(8) unix command, with many
extensions. It supports TCP, UDP, ICMP and RAW-IP protocols. A scripting
language is under developing.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q -n %{name}-%{beta}
%patch0 -p0 -b .endianamd64
%patch1 -p1 -b .hz250

%build
%configure
%make

%install
install -d 755 $RPM_BUILD_ROOT%{_sbindir}
install -d 755 $RPM_BUILD_ROOT%{_mandir}/man8
install -m 755 hping2 $RPM_BUILD_ROOT%{_sbindir}
install -m 644 docs/hping2.8 $RPM_BUILD_ROOT%{_mandir}/man8
cd $RPM_BUILD_ROOT%{_sbindir} && ln -s hping2 hping

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc BUGS CHANGES COPYING INSTALL KNOWN-BUGS TODO
%{_sbindir}/*
%{_mandir}/man8/hping2.8.*


