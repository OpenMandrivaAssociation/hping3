%define beta rc3

Summary:	TCP/IP packet assembler/analyzer
Name:		hping2
Version:	2.0.0
Release:	0.%{beta}.14
License:	GPLv2
Group:		Monitoring
Url:		http://www.hping.org/
Source0:	http://www.hping.org/hping%{version}-%{beta}.tar.gz
Patch0:		30_bytesex.diff
Patch1:		hping2.0.0-rc3-hz-250.patch
Patch2:		hping2-LDFLAGS.diff

%description
hping is a command-line oriented TCP/IP packet assembler/analyzer. The
interface is very similar to the ping(8) unix command, with many extensions.
It supports TCP, UDP, ICMP and RAW-IP protocols. A scripting language is under
developing.

%prep
%setup -qn %{name}-%{beta}
%autopatch -p1

%build
%configure2_5x
%make CCOPT="%{optflags}" LDFLAGS="%{ldflags}"

%install
install -d 755 %{buildroot}%{_sbindir}
install -d 755 %{buildroot}%{_mandir}/man8
install -m 755 hping2 %{buildroot}%{_sbindir}
install -m 644 docs/hping2.8 %{buildroot}%{_mandir}/man8
cd %{buildroot}%{_sbindir} && ln -s hping2 hping

%files
%doc BUGS CHANGES COPYING INSTALL KNOWN-BUGS TODO
%{_sbindir}/*
%{_mandir}/man8/hping2.8.*

