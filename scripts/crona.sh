#!/bin/bash
echo "00 10 * * * bash -c /root/crontab.sh" >> /var/spool/cron/crontabs/root
