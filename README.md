# dhcp-leases

from dhcp_leases.dhcpleases import Dhcp

leases = Dhcp('/var/lib/dhcp/dhcpd.leases')
leases.get()
