# Zenodo Related works — 2026-10-09 一括整備の記録

Zenodo の API（ログイン中ブラウザ経由）で登録・公開。DOI は不変（メタデータのみの更新）。

## 1. Related works が空だった 15 本への 0SM 関係（相手 1 本につき 1 型、#1 は Is part of）

- **#2**: ispartof: #1
- **#3**: ispartof: #1
- **#5**: cites: #2; ispartof: #1
- **#8**: references: #7, #6; cites: #3, #5; ispartof: #1
- **#9**: references: #6; ispartof: #1
- **#12**: references: #10; ispartof: #1
- **#15**: continues: #14; references: #10; cites: #11, #6, #4; ispartof: #1
- **#50**: continues: #47, #46, #7, #10, #19; references: #49, #24, #38, #43; cites: #26, #29, #31, #33, #40, #9, #13, #6; ispartof: #1
- **#54**: continues: #31, #30, #29; references: #17; cites: #24, #26, #47, #45, #33; ispartof: #1
- **#55**: continues: #54; references: #29, #43, #45, #51; cites: #31, #40, #41, #30, #22, #17, #33, #10, #47, #26, #37, #50, #28, #11, #32, #46, #36, #52, #19; ispartof: #1
- **#57**: continues: #34; references: #49, #55, #56, #22, #37, #52; cites: #58, #59, #60, #28, #30, #54, #31; ispartof: #1
- **#59**: continues: #57; references: #10, #15, #33, #49, #52; cites: #34, #51, #42; ispartof: #1
- **#60**: continues: #58, #54; references: #48, #51, #31, #29; cites: #10, #46, #33, #55, #45, #52, #59, #56; ispartof: #1
- **#63**: continues: #51; references: #54, #55, #24, #29; cites: #30, #31, #40, #41, #50, #48, #49, #34, #22, #19, #60, #53, #46; ispartof: #1
- **#64**: continues: #3; iscontinuedby: #65; references: #51, #63; cites: #48, #50, #57, #59, #60, #10; ispartof: #1

注: #55 の bib `hanamura50` は題名 #50・DOI #49 の誤記 → #50 で登録。#60 の bib `hanamura54` は題名違い（DOI は #54）→ #54 で登録。

## 2. #65（10.5281/zenodo.23257458）への逆関係

- Is continued by #65: #64, #10, #51
- Is referenced by #65: #33, #38, #62, #20, #50, #17

## 3. 基本文献（大御所・主要実験）の Cites 追記 — 各論文の参考文献に実際に載っているものだけ

採録基準: 物理の古典論文・決定的実験で DOI が Crossref で照合できたもの（87 本）。教科書・DOI の無い文献（Schrödinger 1930 ZB 論文、Weyl 1918、Kaluza 1921 など）は対象外。resource type = Journal article。

- **#2** (2): Gerlach-Stern 1922, Uhlenbeck-Goudsmit 1925
- **#4** (2): Tonomura et al. 1989, Arndt et al. 1999
- **#10** (5): Thomas 1926, Uhlenbeck-Goudsmit 1926, Einstein 1912, Fan et al. 2023, Dehmelt 1988
- **#11** (12): Berry 1984, Aharonov-Bohm 1959, Dirac 1928, Thomas 1926, Wheeler 1957, Barut-Bracken 1981, Hestenes 1990, Schwinger 1948, DeWitt 1975, BCS 1957, Fan et al. 2023, Dehmelt 1988
- **#12** (3): Breit 1928, Gerritsma et al. 2010, Fan et al. 2023
- **#13** (13): Bell 1964, Aspect et al. 1982, Gerlach-Stern 1922, EPR 1935, Thomas 1926, Uhlenbeck-Goudsmit 1926, Hestenes 1990, Dirac 1928, Berry 1984, Aharonov-Anandan 1987, Einstein 1905, Barut-Zanghi 1984, Fan et al. 2023
- **#14** (7): Barut-Bracken 1981, Schwinger 1948, Aoyama et al. 2015, Aoyama et al. 2012, Fan et al. 2023, Hanneke et al. 2008, Penrose 1996
- **#15** (8): Bohm 1952, Thomas 1926, Thomas 1927, Einstein 1912, Fan et al. 2023, Rabi 1937, EPR 1935, Higgs 1964
- **#17** (8): Wilson 1974, Aharonov-Bohm 1959, Weyl 1929, Yang-Mills 1954, Tonomura et al. 1986, Berry 1984, Thomas 1926, Thomas 1927
- **#19** (6): Uhlenbeck-Goudsmit 1926, Barut-Bracken 1981, Hestenes 1990, Gerritsma et al. 2010, Thomas 1926, LeBlanc et al. 2013
- **#20** (10): Einstein 1905, Barut-Bracken 1981, Aoyama et al. 2015, Hill 1951, Uhlenbeck-Goudsmit 1926, Thomas 1926, Fan et al. 2023, LeBlanc et al. 2013, Dehmelt 1988, Wigner 1960
- **#21** (17): Fan et al. 2023, Hanneke et al. 2008, Gabrielse et al. 2006, Schwinger 1948, Feynman 1949a, Feynman 1949b, Tomonaga 1946, Aoyama et al. 2015, Dirac 1928, Thomas 1926, Thomas 1927, Hestenes 1990, Barut-Bracken 1981, Barut-Zanghi 1984, Gerritsma et al. 2010, LeBlanc et al. 2013, Uhlenbeck-Goudsmit 1926
- **#22** (10): Dirac 1928, Compton 1923, Uhlenbeck-Goudsmit 1926, Thomas 1926, Schwinger 1948, Fan et al. 2023, Einstein 1916, Hestenes 1990, Barut-Bracken 1981, Pound-Rebka 1960
- **#23** (7): Einstein 1916, Fan et al. 2023, Dirac 1928, Hestenes 1990, Barut-Bracken 1981, Gerritsma et al. 2010, LeBlanc et al. 2013
- **#24** (7): Gerritsma et al. 2010, Fan et al. 2023, Dirac 1928, Barut-Bracken 1981, Hestenes 1990, LeBlanc et al. 2013, Wheeler 1955
- **#25** (16): Dirac 1928, Heisenberg 1925, Schrodinger 1926, Dehmelt 1988, Yang-Mills 1954, Glashow 1961, Weinberg 1967, 't Hooft 1971, Higgs 1964, Englert-Brout 1964, ATLAS 2012, Einstein 1936, Pauli 1927, Uhlenbeck-Goudsmit 1926, Thomas 1926, Thomas 1927
- **#26** (4): Anandan-Aharonov 1990, Barut-Bracken 1981, Berry 1984, Einstein 1912
- **#27** (6): EPR 1935, Bohm 1952, Thomas 1926, Thomas 1927, Fan et al. 2023, Einstein 1912
- **#28** (4): Schwinger 1948, Dirac 1928, Fan et al. 2023, Thomas 1926
- **#29** (10): Feynman 1949a, Wigner 1939, Bargmann-Wigner 1948, Dirac 1928, Berry 1984, Schwinger 1951, Aharonov-Bohm 1959, Thomas 1926, Hawking 1975, Unruh 1976
- **#30** (2): Thomas 1926, Berry 1984
- **#31** (4): Aharonov-Bohm 1959, Wu-Yang 1975, Berry 1984, Wilson 1974
- **#32** (6): Weinberg 1989, Aharonov-Bohm 1959, Berry 1984, Wilson 1974, Wu-Yang 1975, Jacobson 1995
- **#33** (1): Penrose 1965
- **#34** (7): Einstein 1916, Dirac 1928, Barut-Bracken 1981, Aharonov-Bohm 1959, Berry 1984, Wilson 1974, Jacobson 1995
- **#37** (4): Pound-Rebka 1960, Gerritsma et al. 2010, Fan et al. 2023, Jacobson 1995
- **#38** (7): Tonomura et al. 1989, Berry 1984, Simon 1983, Hanneke et al. 2008, Foldy-Wouthuysen 1950, Dirac 1928, Bloch-Nordsieck 1937
- **#39** (1): Perlmutter et al. 1999
- **#40** (3): Einstein 1916, Yang-Mills 1954, Wu-Yang 1975
- **#41** (4): Einstein 1916, Yang-Mills 1954, Aharonov-Bohm 1959, Shapiro 1964
- **#42** (2): Dirac 1931, Dirac 1928
- **#43** (4): Aharonov-Bohm 1959, Berry 1984, Wilson 1974, Dirac 1928
- **#44** (4): Dirac 1938, Hestenes 1990, Aharonov-Bohm 1959, Berry 1984
- **#47** (3): Hanneke et al. 2008, Thomas 1926, Einstein 1912
- **#48** (8): Berry 1984, Dirac 1928, Hanneke et al. 2008, Aharonov-Anandan 1987, Thomas 1926, Weinberg 1989, EPR 1935, Bell 1964
- **#49** (2): Dirac 1928, Jacobson 1995
- **#50** (1): Dirac 1928
- **#51** (2): Gerritsma et al. 2010, Jacobson 1995
- **#52** (6): EPR 1935, Thomas 1926, Berry 1984, Bell 1964, Bohm 1952, Weinberg-Witten 1980
- **#53** (1): DeWitt 1967
- **#54** (7): Aharonov-Bohm 1959, Tonomura et al. 1986, Wu-Yang 1975, Berry 1984, Dirac 1931, Wilson 1974, Yang-Mills 1954
- **#55** (8): Wu-Yang 1975, Yang-Mills 1954, Aharonov-Bohm 1959, Tonomura et al. 1986, Berry 1984, Wilson 1974, DeWitt-Brehme 1960, Mandelstam 1968
- **#56** (4): Aharonov-Bohm 1959, Tonomura et al. 1986, Mandelstam 1968, Wu-Yang 1975
- **#57** (5): Wilson 1974, Aharonov-Bohm 1959, Pound-Rebka 1960, Vessot et al. 1980, Berry 1984
- **#58** (4): Thomas 1926, Wigner 1939, Fierz-Pauli 1939, Glauber 1963
- **#60** (10): Aharonov-Bohm 1959, Berry 1984, Wilson 1974, Myers 1941, Klein 1926, Ryu-Takayanagi 2006, Dirac 1928, Hestenes 1990, Thomas 1927, Weinberg-Witten 1980
- **#61** (1): Dirac 1928
- **#62** (6): Thomas 1926, Thomas 1927, Dirac 1928, Wilson 1974, Aharonov-Bohm 1959, Berry 1984
- **#63** (5): Wu-Yang 1975, Aharonov-Bohm 1959, Berry 1984, DeWitt-Brehme 1960, Morette 1951
- **#64** (2): Dirac 1928, Bar 1996
