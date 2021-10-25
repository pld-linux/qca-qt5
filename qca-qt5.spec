Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca-qt5
Version:	2.3.4
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	https://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
# Source0-md5:	5a5398e9dc7fef37d1e7f070260f4886
Patch1:		qt5.patch
URL:		https://invent.kde.org/libraries/qca
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	cmake >= 2.8.2
BuildRequires:	libstdc++-devel
BuildRequires:	nss-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	qt5-build
BuildRequires:	which
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt Cryptographic Architecture (QCA) Library.

%description -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA).

%package devel
Summary:	Qt Cryptographic Architecture (QCA) Library - development files
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla programistów
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel

%description devel
Qt Cryptographic Architecture (QCA) Library - development files.

%description devel -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla
programistów.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DQCA_INSTALL_IN_QT_PREFIX=ON \
	-DQCA_MAN_INSTALL_DIR=%{_mandir} \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build5 install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/qcatool
%attr(755,root,root) %{_bindir}/mozcerts
%ghost %attr(755,root,root) %{_libdir}/libqca.so.2
%attr(755,root,root) %{_libdir}/libqca.so.*.*
%dir %{_libdir}/qca
%dir %{_libdir}/qca/crypto
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-cyrus-sasl.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-gcrypt.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-gnupg.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-logger.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-nss.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-ossl.so
%attr(755,root,root) %{_libdir}/qca/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqca.so
%{_includedir}/QtCrypto
%{_pkgconfigdir}/qca2.pc
%{_datadir}/qt4/mkspecs/features/crypto.prf
%{_libdir}/cmake/Qca

%files -n qca-qt5
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/qt5/bin/mozcerts-qt5
%attr(755,root,root) %{_libdir}/qt5/bin/qcatool-qt5
#%{_prefix}/certs/rootcerts.pem
%attr(755,root,root) %ghost %{_libdir}/libqca-qt5.so.2
%attr(755,root,root) %{_libdir}/libqca-qt5.so.*.*
%dir %{_libdir}/qt5/plugins/crypto
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-cyrus-sasl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-gcrypt.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-gnupg.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-logger.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-nss.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-ossl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool-qt5.1*

%files -n qca-qt5-devel
%defattr(644,root,root,755)
%{_includedir}/qt5/Qca-qt5
%{_libdir}/cmake/Qca-qt5
%attr(755,root,root) %{_libdir}/libqca-qt5.so
%{_pkgconfigdir}/qca2-qt5.pc
%{_libdir}/qt5/mkspecs/features/crypto.prf
