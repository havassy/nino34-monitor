# Niño 3.4 automatikus monitor

Magyar nyelvű, diákokkal is megosztható GitHub Pages oldal. A grafikon a NOAA/CPC heti relatív Niño 3.4 adatsorát mutatja 2026 januárjától, és új NOAA-adat megjelenésekor automatikusan bővül.

## Fájlok

- `index.html` – a weboldal és a grafikon, külső JavaScript/CSS nélkül
- `data.json` – a megjelenített NOAA-adatok
- `update_data.py` – letölti és feldolgozza a NOAA friss adatsorát
- `.github/workflows/update-noaa.yml` – naponta ellenőrzi az adatot, és közzéteszi a friss oldalt
- `.nojekyll` – jelzi, hogy egyszerű statikus oldalról van szó

## Közzététel GitHub Pages-en

1. Hozz létre egy új GitHub repositoryt (például `nino34-monitor`).
2. Töltsd fel a csomag **tartalmát a repository gyökerébe**, úgy, hogy a `.github/workflows/update-noaa.yml` útvonal is megmaradjon.
3. A repositoryban nyisd meg: **Settings → Pages**.
4. A **Build and deployment / Source** résznél válaszd a **GitHub Actions** lehetőséget.
5. Nyisd meg: **Settings → Actions → General → Workflow permissions**, és engedélyezd a **Read and write permissions** beállítást, ha a repository vagy a szervezeti szabályok ezt nem engedik alapból.
6. Nyisd meg az **Actions** lapot. A `Niño 3.4 monitor frissítése és közzététele` workflow az első feltöltés után lefut; kézzel is indítható a **Run workflow** gombbal.
7. A nyilvános címet ezután a **Settings → Pages** oldalon a **Visit site** gombbal tudod megnyitni.

A workflow naponta ellenőrzi a NOAA forrást. Ha új heti érték jelent meg, frissíti a `data.json` fájlt, majd közvetlenül újra közzéteszi a GitHub Pages oldalt. Így a frissítés nem függ attól, hogy egy automatikus commit elindít-e új Pages-buildet.

## Adatforrás

NOAA Climate Prediction Center: Weekly Relative OISST.v2.1 (1991–2020 base period) Niño 3.4.
https://www.cpc.ncep.noaa.gov/data/indices/rel_wksst9120.txt

## Fontos értelmezési megjegyzés

A heti érték önmagában nem jelenti egy ENSO-esemény hivatalos kezdetét vagy végét. Az ENSO értékeléséhez tartós óceáni eltérés és a légkör kapcsolódó viselkedése is szükséges.
