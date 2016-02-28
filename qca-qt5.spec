Summary:	Qt Cryptographic Architecture (QCA)
Name:		qca-qt5
Version:	2.1.0.3
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	http://download.kde.org/stable/qca-qt5/%{version}/src/%{name}-%{version}.tar.xz
# Source0-md5:	e29cc1d8f0292eb28e20b216f52d60fc
Patch0:		qiodevice.patch
URL:		http://download.kde.org/stable/qca-qt5/
BuildRequires:	Qt5Core-devel
BuildRequires:	cmake
BuildRequires:	nss-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Cryptographic Architecture (QCA).

%package devel
Summary:	qca-qt5
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel

%description devel
Qt Cryptographic Architecture (QCA) Library - development files.

%description devel -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla
programistów.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/mozcerts-qt5
%attr(755,root,root) %{_bindir}/qcatool-qt5
#%{_prefix}/certs/rootcerts.pem
%attr(755,root,root) %ghost %{_libdir}/libqca-qt5.so.2
%attr(755,root,root) %{_libdir}/libqca-qt5.so.*.*
%attr(755,root,root) %{_libdir}/qca-qt5/crypto/libqca-cyrus-sasl.so
%attr(755,root,root) %{_libdir}/qca-qt5/crypto/libqca-gcrypt.so
%attr(755,root,root) %{_libdir}/qca-qt5/crypto/libqca-gnupg.so
%attr(755,root,root) %{_libdir}/qca-qt5/crypto/libqca-logger.so
%attr(755,root,root) %{_libdir}/qca-qt5/crypto/libqca-nss.so
%attr(755,root,root) %{_libdir}/qca-qt5/crypto/libqca-ossl.so
%attr(755,root,root) %{_libdir}/qca-qt5/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool-qt5.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/Qca-qt5
%{_libdir}/cmake/Qca-qt5
%attr(755,root,root) %{_libdir}/libqca-qt5.so
%{_pkgconfigdir}/qca2-qt5.pc
%{_prefix}/mkspecs/features/crypto.prf
