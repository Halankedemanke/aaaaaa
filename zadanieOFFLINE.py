from zad7testy import runtests

def droga( G ):
    droga = []
    n = len(G)
    visit = [False for i in range(len(G))]
    def ścieżka(G, n, tmp, droga, i):
        if not visit[tmp]:
            visit[tmp] = True
            droga.append(tmp)
            if len(droga) == n and 0 in G[droga[-1]][i]:
                return droga
            if i == 1:
                for tmp_next in G[tmp][1]:
                    if tmp in G[tmp_next][0]:
                        cur_droga = [k for k in droga]
                        probilbi = ścieżka(G, n, tmp_next, cur_droga, 1)
                        if probilbi is not None:
                            return probilbi
                    elif tmp in G[tmp_next][1]:
                        cur_droga = [i for i in droga]
                        probilbi = ścieżka(G, n, tmp_next, cur_droga, 0)
                        if probilbi is not None:
                            return probilbi
            if i == 0:
                for tmp_next in G[tmp][0]:
                    if tmp in G[tmp_next][0]:
                        cur_droga = [i for i in droga]
                        probilbi = ścieżka(G, n, tmp_next, cur_droga, 1)
                        if probilbi is not None:
                            return probilbi
                    elif tmp in G[tmp_next][1]:
                        cur_droga = [i for i in droga]
                        probilbi = ścieżka(G, n, tmp_next, cur_droga, 0)
                        if probilbi is not None:
                            return probilbi

            visit[tmp] = False
        return None

    return ścieżka(G, len(G), 0, droga, 0)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True )
