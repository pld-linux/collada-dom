Summary:	COLLADA Document Object Model (DOM) library
Summary(pl.UTF-8):	Biblioteka obiektowego modelu dokumentu (DOM) COLLADA
Name:		collada-dom
Version:	2.5.0
Release:	2
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/rdiankov/collada-dom/tags
Source0:	https://github.com/rdiankov/collada-dom/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	5caf23bd2302d07c86c85fa9b9209d87
Patch0:		%{name}-minizip-include.patch
Patch1:		boost-1.87.patch
URL:		https://www.khronos.org/collada/
BuildRequires:	boost-devel >= 1.33
BuildRequires:	cmake >= 2.6.0
BuildRequires:	libstdc++-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	minizip-devel
BuildRequires:	pkgconfig
BuildRequires:	uriparser-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The COLLADA Document Object Model (DOM) is an application programming
interface (API) that provides a C++ object representation of a COLLADA
XML instance document.

%description -l pl.UTF-8
COLLADA Document Object Model (DOM - obiektowy model dokumentu) to
interfejs programowy (API) udostępniający obiektową reprezentację (w
języku C++) dokumentów instancji XML COLLADA.

%package devel
Summary:	Header files for COLLADA DOM library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki COLLADA DOM
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Header files for COLLADA DOM library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki COLLADA DOM.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%build
install -d build
cd build
%cmake ..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.rst changelog.rst licenses/*.txt
%attr(755,root,root) %{_libdir}/libcollada-dom2.5-dp.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libcollada-dom2.5-dp.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libcollada-dom2.5-dp.so
%{_includedir}/collada-dom2.5
%{_pkgconfigdir}/collada-dom.pc
%{_pkgconfigdir}/collada-dom-141.pc
%{_pkgconfigdir}/collada-dom-150.pc
%{_libdir}/cmake/collada_dom-2.5
