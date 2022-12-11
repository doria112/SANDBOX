class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        rv = []
        c_to_d = collections.defaultdict(list)
        for p in paths:
            directory = ""
            for i, f in enumerate(p.split(" ")):
                if i == 0:
                    directory = f
                    continue
                fn, fc = f.split("(")
                fc = fc[:-1]
                c_to_d[fc].append(directory+"/"+fn)
        for k, v in c_to_d.items():
            if len(v) > 1:
                rv.append(v)
        return rv
