Name: nvidia-docker2
Version: %{version}
Release: %{release}
BuildArch: noarch
Group: Development Tools

Vendor: NVIDIA CORPORATION
Packager: NVIDIA CORPORATION <cudatools@nvidia.com>

Summary: nvidia-docker CLI wrapper
URL: https://github.com/NVIDIA/nvidia-docker
License: BSD

Source0: nvidia-docker
Source1: daemon.json
Source2: LICENSE
Source3: nvidia-docker.conf

Conflicts: nvidia-docker < 2.0.0
Requires: nvidia-container-runtime = %{runtime_version}
Requires: %{docker_version}

%description
Replaces nvidia-docker with a new implementation based on nvidia-container-runtime

%prep
cp %{SOURCE0} %{SOURCE1} %{SOURCE2} %{SOURCE3} .

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 -t %{buildroot}%{_bindir} nvidia-docker
mkdir -p %{buildroot}/etc/docker
install -m 644 -t %{buildroot}/etc/docker daemon.json
%if 0%{?suse_version}
mkdir -p %{buildroot}%{_unitdir}/docker.service.d
install -m 644 -t %{buildroot}%{_unitdir}/docker.service.d nvidia-docker.conf
%endif

%files
%license LICENSE
%{_bindir}/nvidia-docker
/etc/docker/daemon.json
%if 0%{?suse_version}
%{_unitdir}/docker.service.d/nvidia-docker.conf
%endif

%changelog
