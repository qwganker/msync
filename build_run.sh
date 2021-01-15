#/bin/bash

echo "打包前端"

cd ./web/msync/ && npm run build

echo "移动前端打包文件到 django"

if [ -d "../../msync/web/dist" ]; then
  rm -rf ../../msync/web/dist
fi

mv  ./dist ../../msync/web

echo "打包完成"

cd ../../msync/
python3 manage.py runserver

