YAY="(^-^)"
SAD="(╯°□°）╯︵ ┻━┻"
YELLOW="$(tput setaf 3 0 0)"
RED="$(tput setaf 1 0 0)"
NORM="$(tput sgr0)"
BLUE="$(tput setaf 4 0 0)"
GREEN="$(tput setaf 2 0 0)"

PS1='\[\e]0;\W\a\]$(
LEXIT="$?"
ps1
) \u@\h:\W\$ '


ps1() {
		[ $LEXIT -eq 0 ] && echo "$GREEN$YAY$NORM" || echo "$RED$SAD$NORM"
	}
