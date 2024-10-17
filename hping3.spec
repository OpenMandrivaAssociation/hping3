%define alpha 1

Summary:	TCP/IP packet assembler/analyzer
Name:		hping3
Version:	3.0.0
Release:	0.%{alpha}.1
License:	GPLv2
Group:		Monitoring
Url:		https://www.hping.org/
Source0:	http://www.hping.org/%{name}-%{version}-alpha-%{alpha}.tar.xz
Source1:	hping3.desktop
Patch0:		fix-include-paths-and-linking.patch
Patch1:		configure-fix-tcl-detection.patch
BuildRequires:	pkgconfig(libpcap)
BuildRequires:	pkgconfig(tcl)
BuildRequires:	imagemagick
BuildRequires:	tcl


%description
hping is a command-line oriented TCP/IP packet assembler/analyzer. The
interface is very similar to the ping(8) unix command, with many extensions.
It supports TCP, UDP, ICMP and RAW-IP protocols. A scripting language is under
development.

%prep
%setup -qn %{name}-%{version}-alpha-%{alpha}
%autopatch -p1

%build
%configure
%make_build CCOPT="%{optflags}" LDFLAGS="%{ldflags}"
cd docs/french
make
cd ../../
cd img
mogrify -format png *.jpg
cd ../
%install
install -d 755 %{buildroot}%{_sbindir}
install -d 755 %{buildroot}%{_mandir}/man8
install -m 755 %{name} %{buildroot}%{_sbindir}
install -m 644 docs/hping3.8 %{buildroot}%{_mandir}/man8
install -d 755 %{buildroot}%{_docdir}/hping3/french
install -m 644 docs/french/* %{buildroot}%{_docdir}/hping3/french 
install -m 644 docs/*.txt docs/HPING2-IS-OPEN docs/MORE-FUN-WITH-IPID  docs/AS-BACKDOOR docs/*.example %{buildroot}%{_docdir}/hping3/ 
install -d 755 %{buildroot}/%{_iconsdir}/favicons
install -m 644 img/favicon.ico	 %{buildroot}/%{_iconsdir}/favicons/hping3.ico
install -d 755 %{buildroot}/%{_iconsdir}/hicolor/384x212/apps
install -m 644 img/hping_big.png %{buildroot}/%{_iconsdir}/hicolor/384x212/apps/hping3_big.png
install -d 755 %{buildroot}/%{_iconsdir}/hicolor/16x16/apps
install -m 644 img/hping_icon.png %{buildroot}/%{_iconsdir}/hicolor/16x16/apps/hping3_icon.png
install -d 755 %{buildroot}/%{_datadir}/applications
install -m 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/
install -d 755 %{buildroot}/usr/lib/hping3/regtest
install -m 644 lib/*.htcl %{buildroot}/usr/lib/hping3
install -m 644 lib/regtest/*.htcl %{buildroot}/usr/lib/hping3/regtest
cd %{buildroot}%{_sbindir} && ln -s %{name} hping

%files
%doc BUGS CHANGES COPYING INSTALL KNOWN-BUGS TODO 
%{_docdir}/hping3/*
%{_docdir}/hping3/french/*
%{_sbindir}/*
%{_datadir}/applications/hping3.desktop
%{_mandir}/man8/hping3.8.*
%{_iconsdir}/favicons/*.ico
%{_iconsdir}/hicolor/16x16/apps/hping3_icon.png
%{_iconsdir}/hicolor/384x212/apps/hping3_big.png
/usr/lib/hping3/*.htcl
/usr/lib/hping3/regtest/*.htcl