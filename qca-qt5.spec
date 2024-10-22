# TODO: crypto plugin subpackages?
Summary:	Qt Cryptographic Architecture (QCA) Library
Summary(pl.UTF-8):	Biblioteka Qt Cryptographic Architecture (QCA)
Name:		qca-qt5
Version:	2.3.9
Release:	1
License:	LGPL v2.1
Group:		Libraries
Source0:	https://download.kde.org/stable/qca/%{version}/qca-%{version}.tar.xz
# Source0-md5:	d8aaa46356a322464f65b04d00d2bac6
URL:		https://invent.kde.org/libraries/qca
BuildRequires:	Qt5Core-devel >= 5.14
# or botan3 (with C++20)
BuildRequires:	botan2-devel >= 2
BuildRequires:	cmake >= 3.16
BuildRequires:	cyrus-sasl-devel >= 2
BuildRequires:	libgcrypt-devel
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	nss-devel
BuildRequires:	openssl-devel >= 1.1.1
BuildRequires:	pkcs11-helper-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build
BuildRequires:	which
Requires:	Qt5Core >= 5.14
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
Requires:	Qt5Core-devel >= 5.14
Requires:	libstdc++-devel >= 6:7

%description devel
Qt Cryptographic Architecture (QCA) Library - development files.

%description devel -l pl.UTF-8
Biblioteka Qt Cryptographic Architecture (QCA) - pliki dla
programistów.

%prep
%setup -q -n qca-%{version}

%build
%cmake -B build \
	-DQCA_INSTALL_IN_QT_PREFIX=ON \
	-DQCA_MAN_INSTALL_DIR=%{_mandir}

%{__make} -C build

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
%attr(755,root,root) %{_libdir}/libqca-qt5.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libqca-qt5.so.2
%attr(755,root,root) %{_libdir}/qt5/bin/mozcerts-qt5
%attr(755,root,root) %{_libdir}/qt5/bin/qcatool-qt5
%dir %{_libdir}/qt5/plugins/crypto
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-botan.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-cyrus-sasl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-gcrypt.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-gnupg.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-logger.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-nss.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-ossl.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-pkcs11.so
%attr(755,root,root) %{_libdir}/qt5/plugins/crypto/libqca-softstore.so
%{_mandir}/man1/qcatool-qt5.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libqca-qt5.so
%{_includedir}/qt5/Qca-qt5
%{_pkgconfigdir}/qca2-qt5.pc
%{_libdir}/cmake/Qca-qt5
%{_libdir}/qt5/mkspecs/features/crypto.prf
