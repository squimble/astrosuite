_pkgname=astrosuite
pkgname=python+$_pkgname
pkgver=1.00r
pkgrel=1
pkgdesc="Astronomy research-focused software collection written in Python"
arch=('any')
url="https://github.com/squimble/astrosuite/tree/main"
license=('MIT')
depends=('python', 'python-pandas','python-astropy','python-astroquery')
makedepends=('git' 'python-build' 'python-installer' 'python-wheel' 'python-setuptools')
provides=("${pkgname%}")
conflicts=("${pkgname%}")
source=("git+https://github.com/squimble/astrosuite.git#branch=main")
md5sums=('SKIP')

prepare(){
	echo -e "\033[255;145;0m"
	cat << "EOF"

	                                                                                                                                        
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        
                                                                                                      ███                               
                                         ██                                                                   ██                        
                                         ██                                                                   ██                        
             ████████      ████████   ████████   ██ ████    ████████      ████████     ██        ██    ██  ████████    ████████         
           ███      ██    ██      ██     ██      ███      ███      ███   ███     ███   ██        ██    ██     ██      ██      ███       
                    ███   ██             ██      ██      ███        ██   ███           ██        ██    ██     ██     ██        ███      
              █████████    ██████        ██      ██      ██         ███   ██████       ██        ██    ██     ██     █████████████      
           ████     ███         ████     ██      ██      ██         ██         ████    ██        ██    ██     ██     ██                 
           ██       ███  ███      ███    ██      ██      ███        ██   ██       ██   ██       ███    ██     ██     ██        ███      
           ███    █████   ███     ██     ███     ██       ████    ███    ███     ███    ███    ████    ██     ██      ███     ███       
             ██████ ███     ███████        ███   ██          ██████        ███████       ██████  ██    ██      ████     ███████  


		Building from GitHub repo...
		Thanks for installing astrosuite!
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        

	
EOF
	echo -e  "\e[0m"

}

build(){
	cd "$_pkgname"
	python -m build --wheel --no-isolation

}

package(){
	cd "$_pkgname"
	python -m installer --destdir="$pkgdir" dist/*.whl

	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

