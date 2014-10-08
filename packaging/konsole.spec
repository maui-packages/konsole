# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       konsole

# >> macros
# << macros

Summary:    Konsole is a terminal program for KDE 5
Version:    4.97.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  konsole.yaml
Source101:  konsole-rpmlintrc
Requires:   kf5-filesystem
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  qt5-tools
BuildRequires:  kdbusaddons-devel
BuildRequires:  kcoreaddons-devel
BuildRequires:  kconfig-devel
BuildRequires:  kcodecs-devel
BuildRequires:  ki18n-devel
BuildRequires:  kwidgetsaddons-devel
BuildRequires:  karchive-devel
BuildRequires:  kitemmodels-devel
BuildRequires:  kauth-devel
BuildRequires:  kguiaddons-devel
BuildRequires:  kconfigwidgets-devel
BuildRequires:  kitemviews-devel
BuildRequires:  knotifications-devel
BuildRequires:  kjs-devel
BuildRequires:  kpty-devel
BuildRequires:  kjobwidgets-devel
BuildRequires:  kiconthemes-devel
BuildRequires:  kcompletion-devel
BuildRequires:  ktextwidgets-devel
BuildRequires:  kglobalaccel-devel
BuildRequires:  kxmlgui-devel
BuildRequires:  solid-devel
BuildRequires:  kwallet-devel
BuildRequires:  kbookmarks-devel
BuildRequires:  kio-devel
BuildRequires:  kunitconversion-devel
BuildRequires:  knotifyconfig-devel
BuildRequires:  kparts-devel
BuildRequires:  kross-devel
BuildRequires:  kdelibs4support-devel
BuildRequires:  kdoctools-devel

%description
Konsole is a terminal program for KDE 5.


%package doc
Summary:    Documentation and user manuals for %{name}
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation and user manuals for %{name}


%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc README COPYING COPYING.DOC COPYING.LIB COPYING.Unicode
%{_kf5_bindir}/konsole
%{_kf5_bindir}/konsoleprofile
%{_kf5_libdir}/libkdeinit5_konsole.so
%{_kf5_libdir}/libkonsoleprivate.so.*
%{_kf5_plugindir}/*
%{_kf5_sharedir}/konsole
%{_kf5_sharedir}/kxmlgui5/*
%{_kf5_sharedir}/kconf_update/*
%{_kf5_sharedir}/applications/org.kde.konsole.desktop
%{_kf5_servicesdir}/*
%{_kf5_servicetypesdir}/*
%{_kf5_sharedir}/knotifications5/konsole.notifyrc
# >> files
# << files

%files doc
%defattr(-,root,root,-)
%{_kf5_htmldir}/en/konsole/
# >> files doc
# << files doc
