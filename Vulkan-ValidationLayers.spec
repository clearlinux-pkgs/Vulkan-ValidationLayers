#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Vulkan-ValidationLayers
Version  : 1.2.137
Release  : 16
URL      : https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/v1.2.137/Vulkan-ValidationLayers-1.2.137.tar.gz
Source0  : https://github.com/KhronosGroup/Vulkan-ValidationLayers/archive/v1.2.137/Vulkan-ValidationLayers-1.2.137.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: Vulkan-ValidationLayers-data = %{version}-%{release}
Requires: Vulkan-ValidationLayers-license = %{version}-%{release}
BuildRequires : SPIRV-Headers-dev
BuildRequires : SPIRV-Tools-dev
BuildRequires : Vulkan-Headers-data
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : glslang-bin
BuildRequires : glslang-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-server)
BuildRequires : pkgconfig(x11-xcb)
BuildRequires : python3
Patch1: 0001-Fix-the-include-path-to-spirv.hpp.patch

%description
# Vulkan Ecosystem Components
This project provides the Khronos official Vulkan validation layers for Windows, Linux, Android, and MacOS.

%package data
Summary: data components for the Vulkan-ValidationLayers package.
Group: Data

%description data
data components for the Vulkan-ValidationLayers package.


%package dev
Summary: dev components for the Vulkan-ValidationLayers package.
Group: Development
Requires: Vulkan-ValidationLayers-data = %{version}-%{release}
Provides: Vulkan-ValidationLayers-devel = %{version}-%{release}
Requires: Vulkan-ValidationLayers = %{version}-%{release}

%description dev
dev components for the Vulkan-ValidationLayers package.


%package license
Summary: license components for the Vulkan-ValidationLayers package.
Group: Default

%description license
license components for the Vulkan-ValidationLayers package.


%prep
%setup -q -n Vulkan-ValidationLayers-1.2.137
cd %{_builddir}/Vulkan-ValidationLayers-1.2.137
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586894584
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake .. -DBUILD_WSI_MIR_SUPPORT=OFF \
-DGLSLANG_INSTALL_DIR=/usr \
-DCMAKE_INSTALL_INCLUDEDIR=/usr/include/vulkan/
make  %{?_smp_mflags}  VERBOSE=1
popd

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
cd clr-build; make test

%install
export SOURCE_DATE_EPOCH=1586894584
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Vulkan-ValidationLayers
cp %{_builddir}/Vulkan-ValidationLayers-1.2.137/LICENSE.txt %{buildroot}/usr/share/package-licenses/Vulkan-ValidationLayers/9bf8124f4495a48c4fd7104aebe2e957176b930b
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/vulkan/explicit_layer.d/VkLayer_khronos_validation.json

%files dev
%defattr(-,root,root,-)
/usr/lib64/libVkLayer_khronos_validation.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Vulkan-ValidationLayers/9bf8124f4495a48c4fd7104aebe2e957176b930b
