class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        visits = {}

        for domain in cpdomains:
            count, dom = domain.split()

            # split upt domain and work through it from right to left
            domains = dom.split('.')
            for i in reversed(range(len(domains))):
                sub_dom = '.'.join(domains[i:])

                visits[sub_dom] = visits.get(sub_dom, 0) + int(count)

        return [(str(visits[domain]) + " " + domain) for domain in visits]
            
