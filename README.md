# Gaia Node Kurulum 
![image](https://github.com/user-attachments/assets/54b74a74-5e0f-4f69-9ad7-483c4805b672)

<details>
  <summary> <h1>Daha Önce Kurduysan Bu işlemleri yap</summary> </h1>
## Kurulum

```console
# sırasıyla
gaianet stop
sudo kill -9 $(lsof -t -i:8080)
curl -sSfL 'https://github.com/GaiaNet-AI/gaianet-node/releases/latest/download/uninstall.sh' | bash
source /root/.bashrc

curl -sSfL 'https://github.com/GaiaNet-AI/gaianet-node/releases/latest/download/install.sh' | bash
source /root/.bashrc
gaianet init --config https://raw.githubusercontent.com/GaiaNet-AI/node-configs/main/qwen2-0.5b-instruct/config.json
# kurulumlar tamamlanana kadar bekleyin.
```
```console
# start edelim.
gaianet start

# node infoları
gaianet info
```

> [buradan](https://www.gaianet.ai/setting/nodes) node-info bilgilerinizi girip node'u ekleyin. Eskisinin yerine bunu kullanacağız.

<img width="397" alt="Ekran Resmi 2025-02-07 21 46 05" src="https://github.com/user-attachments/assets/45bd47ef-3aba-4141-baec-bbd03ca68aa4" />

> Kendi domainimize katılacağız (en düşük donanımı destekleyen tek bir domain var)

```console
gaianet stop
gaianet config --domain gaia.domains
gaianet init
gaianet start
```

> node ayarlarına [gidelim](https://www.gaianet.ai/setting/nodes)

> Görseldeki 3 noktaya tıklayıp join domain diyelim

<img width="424" alt="Ekran Resmi 2025-02-07 21 47 50" src="https://github.com/user-attachments/assets/a1de0b3e-1a80-498f-8bbc-0b373024173c" />

> rues yazıp domaini ekleyelim.

![image](https://github.com/user-attachments/assets/8c9fd6dc-b4dd-415b-87bf-e89db66bedf7)


> ChatGPT yerine [bu](https://www.gaianet.ai/chat?domain=ruesandora.gaia.domains&type=domain) botu kullanmak node puanınızı arttıracak.

> Kullanmadığımız zamanlarda da çalışması için oto text bot kuracağız.

#

> [Buradan](https://www.gaianet.ai/reward-summary) base ağına geçerek reeddem yapın EXP'leri.

<img width="1443" alt="Ekran Resmi 2025-02-07 21 50 23" src="https://github.com/user-attachments/assets/13309650-98fa-45db-8c3e-721c07092581" />

> Creditleri Consumed'e çevireceğiz.

> [Buradan](https://www.gaianet.ai/setting/gaia-api-keys) bir API key oluşturup saklayın keyi.

```console
curl -L -o gaiabot.py https://github.com/enzifiri/gaia-node/raw/main/gaiabot.py
screen -S gaia
python3 gaiabot.py

# akabinde CTRL A D ile çıkış yapabilirsiniz burdan.
```

> Refresh attıkca consumed artacak.

<img width="661" alt="Ekran Resmi 2025-02-07 21 52 10" src="https://github.com/user-attachments/assets/35c01933-f3ab-448e-b1ec-5b2dfea724a8" />

> Bu şekilde bir hesabınıza eklediğiniz kadar node eklersiniz.

> tokenininizin biteceğini unutmayın , expler önemli.


> Akabinde node puan artacak (24 saat sonra)

<img width="544" alt="Ekran Resmi 2025-02-07 21 55 26" src="https://github.com/user-attachments/assets/6157d573-2793-482c-9011-f125c7680aab" />

</details>



<details>
  <summary> <h1>Hiç Kurmadıysan Burdan Başla</summary> </h1>

  
## Kurulum

> Daha önce Gaia katılıp EXP'leri toplamıştık.

> Bu EXP'leri node'un çalışması için kredi olarak kullanacağız.

> [Buradan](https://gaianet.ai/reward?invite_code=RiFcz1) EXP'leri toplayabilirsiniz.

#
## Donanım

> CPU : 4 vCPU

> RAM : 8GB

#
## komutlar.

```console
# sırasıyla
sudo apt update && sudo apt upgrade -y
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev python3-pip pip

curl -sSfL 'https://github.com/GaiaNet-AI/gaianet-node/releases/latest/download/install.sh' | bash
source /root/.bashrc

gaianet init --config https://raw.githubusercontent.com/GaiaNet-AI/node-configs/main/qwen2-0.5b-instruct/config.json
