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
