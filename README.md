# Open Academy

This an odoo app, going through the odoo `building module tutorial`, [https://www.odoo.com/documentation/11.0/howtos/backend.html](https://www.odoo.com/documentation/11.0/howtos/backend.html).
The app is ment to be a tool to practice odoo concepts.

The app is totaly hypothetical and only useful for learning

## New Client Installation Guide

### Create new PostgreSQL container

```sh
sudo docker run -d -e POSTGRES_USER=odoo -e POSTGRES_PASSWORD=odoo -e POSTGRES_DB=postgres --name {clientname}-db postgres:10
```

### Start new Odoo container

```sh
sudo docker run -d -v /path/to/the/project:/mnt/extra-addons -p {odoo-container-port}:8069 --name {clientname}-odoo --link {clientname}-db:db -t odoo:11
```

## Backups

### Backup PostgreSQL Database

Configure a nightly cron job as root for db backups in the scheduler.

```sh
docker exec -t {clientname}-db pg_dumpall -c -U postgres > /home/forge/{domain.com}/backups/{clientname}_`date +%d-%m-%Y"_"%H_%M_%S`.sql
```

### Clean Backups
Configure a nightly cron job as root to remove old backups in the scheduler.

```sh
find /home/forge/{domain.com}/backups/ -type f -mtime +90 -exec rm {} +
```

### Restore PostgreSQL Database

```sh
cat {clientname}_{01-01-2019_00_00_00}.sql | sudo docker exec -i {clientname}-db psql -U postgres
```

---

## Common Issues

### File Permissions
If modules aren't showing up, make sure all folders and files have the correct permissions:
```sh
sudo find ./ -type d -exec chmod 755 {} \;
sudo find ./ -type f -exec chmod 644 {} \;
```
