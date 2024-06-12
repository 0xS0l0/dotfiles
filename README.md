# dotfiles

<summary> Dependencies</summary> <br>

<!--Ok The headache starts here-->

  <details>
  <summary>i3</summary> <br>

  ```bash
  sudo apt install i3
  ```
  </details>

  <details>
  <summary>polybar</summary> <br>

  ```bash
  echo -e "\n\e[40mInstalling polybar...\n"
  sudo apt-get install cmake cmake-data libcairo2-dev libxcb1-dev libxcb-ewmh-dev libxcb-icccm4-dev libxcb-image0-dev libxcb-randr0-dev libxcb-util0-dev libxcb-xkb-dev pkg-config python3-xcbgen xcb-proto libxcb-xrm-dev i3-wm libasound2-dev libmpdclient-dev libiw-dev libcurl4-openssl-dev libpulse-dev libxcb-composite0-dev xcb libxcb-ewmh2
  sudo apt install polybar
  install -Dm644 /usr/share/doc/polybar/config $HOME/.config/polybar/config
  ```
  </details>

  <details>
  <summary>zsh</summary> <br>

  ```bash
  sudo apt install zsh
  ```
  </details>

  <details>
  <summary>oh-my-zsh</summary> <br>

  ```bash
  sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

  git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

  git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

  chsh -s $(which zsh)
  ```
  </details>
  
  <details>
  <summary>imagemagick</summary> <br>

  ```bash
  sudo apt install imagemagick
  ```
  
  </details>

  <details>
  <summary>compton</summary> <br>

  ```bash
  sudo apt install compton
  ```
  </details>

  <details>
  <summary>feh</summary> <br>

  ```bash
  sudo apt install feh
  ```
  </details>
  
  <details>
  <summary>ffmpeg</summary> <br>

  ```bash
  sudo apt install ffmpeg
  ```
  </details>

  <details>
  <summary>neofetch</summary> <br>

  ```bash
  sudo apt install neofetch
  ```
  </details>

  <details>
  <summary>i3-gaps</summary> <br>

  ```bash
  sudo apt  install i3-gaps 
  ```
  </details>

  <details>
  <summary>ranger</summary> <br>

  ```bash
  sudo apt install ranger 
  ```
  </details>

  <details>
  <summary>rofi</summary> <br>

  ```bash
  sudo apt install rofi 
  ```
  </details>
  
  <details>
  <summary>polybar-themes</summary> <br>

  ```bash
  git clone --depth=1 https://github.com/adi1090x/polybar-themes.git
  cd polybar-themes
  chmod +x setup.sh
  ./setup.sh
  ```
  
  ##### Ok now choose option 1 that's all
  
  </details> 
  

