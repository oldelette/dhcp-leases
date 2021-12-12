# dhcp-leases

from dhcp_leases.dhcpleases import Dhcp <br>

leases = Dhcp('/var/lib/dhcp/dhcpd.leases') <br>
leases.get() <br>
leases.get_current() <br>
