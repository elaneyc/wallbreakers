class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        visits = {}

        # Add all complete domains to visits
        for domain in cpdomains:
            cp = domain.split()
            visits[cp[1]] = visits.get(cp[1],0) + int(cp[0])

        # Iterate through visits and break up
        for dom in visits.keys():
            domains = dom.split('.')
            #print dom
            #print visits[dom]
            sub_dom = '.'.join(domains[1:])
            #print sub_dom
            visits[sub_dom] = visits.get(sub_dom, 0) + visits[dom]
            #print visits[sub_dom]
            if len(domains) > 2:
                sub_dom = '.'.join(domains[2:])
                visits[sub_dom] = visits.get(sub_dom, 0) + visits[dom]

        return [(str(visits[domain]) + " " + domain) for domain in visits]
