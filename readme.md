# Dự án chia sẻ tài liệu mã nguồn mở được thực hiện bởi

- Nguyễn Hữu Sơn - sonnhfit@gmail.com (founder)
- Hoàng Thị Mỹ Linh -linlinciu5998@gmail.com
- Phạm Thanh Phong - thanhphongdz2707@gmail.com
- Nguyễn Nhật Nam - nhatnamnguyen.gtvthcm@gmail.com
- Hoàng Đình Hùng - h1oangdinhhung59@gmail.com
- Nguyễn Trung Phúc - ntpdev264@gmail.com
- Trần Nam Phương - trannamphuong2k@gmail.com
- Nguyễn Trọng Nghĩa - trongnghiabn99@gmail.com
- Nguyễn Hùng Tình - cautunn0501@gmail.com
- Đặng Thị Huệ - dangthihue.2006@gmail.com
- Lê Anh (DuaHau) - leanh41@gmail.com
- Trần - Tuấn - tuantt1889@gmail.com

# Codebase appserver

## The Gentlemen way (Using Docker) 

1. Install ``docker`` and ``docker-compose``
2. cd in to Project dir and Build docker with command 
```
$ docker-compose build
```
3. Runserver 

```
$ docker-compose up -d

```

Now the API server is running on : [http://localhost:8000](http://localhost:8000)
API Document server is running on [http://localhost:1234](http://localhost:1234)


## Development 

### Coding style

- ALWAYS follow PEP8 coding style [http://pep8.org](http://pep8.org)

### RUN Unit test

```
$ docker exec -it <container-id> python manage.py test
```
### backup 

#### Show container id
```
    docker ps
```
#### Backup command 
``` 
docker exec -t <db container id>  pg_dumpall -c -U postgres > dump_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```

### Restore 

- The first  ```docker-compose down```
- show docker volume ``` docker volume  ls ```
- remove volume sql exist with command : ```docker volume rm <name volume>```
- create docker db volume blank with command: ```docker-compose up -d db```
  ```docker-compose up -d <db_name_serivice>``` 
- import sql file with command: ```cat <sqlfile.sql> | docker exec -i <dontainer id> psql -U <username> -d <dbname>```
- for example:   ```cat app-db-2018-11-16.sql | docker exec -i e1a2a1e3ab89 psql -U postgres -d postgres```


