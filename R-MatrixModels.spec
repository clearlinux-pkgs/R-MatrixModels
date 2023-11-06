#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v2
# autospec commit: 250a666
#
Name     : R-MatrixModels
Version  : 0.5.3
Release  : 85
URL      : https://cran.r-project.org/src/contrib/MatrixModels_0.5-3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/MatrixModels_0.5-3.tar.gz
Summary  : Modelling with Sparse and Dense Matrices
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
modular prediction and response module classes.

%prep
%setup -q -n MatrixModels
pushd ..
cp -a MatrixModels buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1699289438

%install
export SOURCE_DATE_EPOCH=1699289438
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/MatrixModels/DESCRIPTION
/usr/lib64/R/library/MatrixModels/INDEX
/usr/lib64/R/library/MatrixModels/Meta/Rd.rds
/usr/lib64/R/library/MatrixModels/Meta/features.rds
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
/usr/lib64/R/library/MatrixModels/tests/MModels.R
