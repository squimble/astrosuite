_pkgname=astrosuite
pkgname=python+$_pkgname
pkgver=1.00r
pkgrel=1
pkgdesc="Astronomy research-focused software collection written in Python"
arch=('any')
url="https://github.com/squimble/astrosuite/tree/main"
license=('MIT')
depends=('python')
makedepends=('git' 'python-build' 'python-installer' 'python-wheel' 'python-setuptools' 'python-pip')
provides=("${pkgname%}")
conflicts=("${pkgname%}")
source=("git+https://github.com/squimble/astrosuite.git#branch=main")
md5sums=('SKIP')

prepare(){
	cd "$_pkgname"
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
		But first, Installing required python dependencies via AUR and pip! :)
		Thanks for installing astrosuite!
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        
                                                                                                                                        

	
EOF
	echo -e  "\e[0m"
	yay -S python-pyvo
	pip install --target='vendor' astroquery
	yay -S python-astroquery
	pip install --target='vendor' astropy
	pacman -S python-astropy
	pip install --target='vendor' pandas
	pacman -S python-pandas

}

build(){
	echo -e 
	cat << "EOF"

	Beginning build process... (If you got here, either you are very patient or lucky)
	Thanks for being patient! 
	(During full version updates of astrosuite, run pacman -R python+astrosuite to remove, before running makepkg -si in the cloned dir.)

	
EOF
	cd "$_pkgname"
	python -m build --wheel --no-isolation

}

package(){
	cd "$_pkgname"
	python -m installer --destdir="$pkgdir" dist/*.whl

	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

