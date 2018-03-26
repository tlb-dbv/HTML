#!/bin/sh
#tornando o firewall restritivo - politicasdas tabelas filter em drop
iptables -P INPUT ACCEPT
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
#LIMPAR AS REGRAS DAS CHAINS DA TABELA FILTER
iptables -F
