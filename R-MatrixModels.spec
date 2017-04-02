#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-MatrixModels
Version  : 0.4.1
Release  : 19
URL      : https://cran.r-project.org/src/contrib/MatrixModels_0.4-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MatrixModels_0.4-1.tar.gz
Summary  : Modelling with Sparse And Dense Matrices
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n MatrixModels

%build
export LANG=C
export SOURCE_DATE_EPOCH=1489098772

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1489098772
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library MatrixModels
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library MatrixModels


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MatrixModels/DESCRIPTION
/usr/lib64/R/library/MatrixModels/INDEX
/usr/lib64/R/library/MatrixModels/Meta/Rd.rds
/usr/lib64/R/library/MatrixModels/Meta/hsearch.rds
/usr/lib64/R/library/MatrixModels/Meta/links.rds
/usr/lib64/R/library/MatrixModels/Meta/nsInfo.rds
/usr/lib64/R/library/MatrixModels/Meta/package.rds
/usr/lib64/R/library/MatrixModels/NAMESPACE
/usr/lib64/R/library/MatrixModels/R/MatrixModels
/usr/lib64/R/library/MatrixModels/R/MatrixModels.rdb
/usr/lib64/R/library/MatrixModels/R/MatrixModels.rdx
/usr/lib64/R/library/MatrixModels/help/AnIndex
/usr/lib64/R/library/MatrixModels/help/MatrixModels.rdb
/usr/lib64/R/library/MatrixModels/help/MatrixModels.rdx
/usr/lib64/R/library/MatrixModels/help/aliases.rds
/usr/lib64/R/library/MatrixModels/help/paths.rds
/usr/lib64/R/library/MatrixModels/html/00Index.html
/usr/lib64/R/library/MatrixModels/html/R.css
