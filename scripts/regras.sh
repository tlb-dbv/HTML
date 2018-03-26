#!/bin/sh
#LIMPAR AS REGRAS DAS CHAINS DA TABELA FILTER
iptables -F
#######################################################################
iptables -A INPUT -p icmp -j DROP
iptables -A OUTPUT -p icmp -j DROP
