.lib cmos_models_emPowerSOC
.MODEL nmos NMOS (LEVEL   = 49 hdif = 0.25e-6 acm = 3 
+VERSION = 3.1            TNOM    = 27             TOX     = 4.2E-9
+XJ      = 1E-7           NCH     = 2.3549E17      VTH0    = 0.3710619
+K1      = 0.5940793      K2      = 2.070131E-3    K3      = 1E-3
+K3B     = 2.7158495      W0      = 1E-7           NLX     = 2.005089E-7
+DVT0W   = 0              DVT1W   = 0              DVT2W   = 0
+DVT0    = 1.4615376      DVT1    = 0.3798134      DVT2    = 0.0692378
+U0      = 293.522312     UA      = -6.73646E-10   UB      = 1.164182E-18
+UC      = -2.84532E-11   VSAT    = 9.286324E4     A0      = 1.7591856
+AGS     = 0.3162202      B0      = -5.950938E-8   B1      = -1E-7
+KETA    = 0.0111532      A1      = 3.896574E-4    A2      = 1
+RDSW    = 139.0465393    PRWG    = 0.5            PRWB    = -0.2
+WR      = 1              WINT    = 0              LINT    = 9.265899E-9
+XL      = -2E-8          XW      = -1E-8          DWG     = -1.343579E-9
+DWB     = -1.391607E-8   VOFF    = -0.0765575     NFACTOR = 2.4791597
+CIT     = 0              CDSC    = 2.4E-4         CDSCD   = 0
+CDSCB   = 0              ETA0    = 0              ETAB    = -0.0608407
+DSUB    = 1              PCLM    = 0.8853499      PDIBLC1 = 0.116863
+PDIBLC2 = 0.01           PDIBLCB = -0.0475298     DROUT   = 0.5922434
+PSCBE1  = 8E10           PSCBE2  = 5.248199E-10   PVAG    = 0.089248
+DELTA   = 0.01           RSH     = 6.8            MOBMOD  = 1
+PRT     = 0              UTE     = -1.5           KT1     = -0.11
+KT1L    = 0              KT2     = 0.022          UA1     = 4.31E-9
+UB1     = -7.61E-18      UC1     = -5.6E-11       AT      = 3.3E4
+WL      = 0              WLN     = 1              WW      = 0
+WWN     = 1              WWL     = 0              LL      = 0
+LLN     = 1              LW      = 0              LWN     = 1
+LWL     = 0              CAPMOD  = 2              XPART   = 0.5
+CGDO    = 7.75E-10       CGSO    = 7.75E-10       CGBO    = 1E-12
+CJ      = 9.955315E-4    PB      = 0.7345743      MJ      = 0.3629904
+CJSW    = 2.586055E-10   PBSW    = 0.6451808      MJSW    = 0.1296914
+CJSWG   = 3.3E-10        PBSWG   = 0.6451808      MJSWG   = 0.1296914
+CF      = 0              PVTH0   = 1.33957E-3     PRDSW   = -5
+PK2     = -1.7189E-4     WKETA   = 0.010864       LKETA   = -0.0102793
+PU0     = 37.4749547     PUA     = 1.762367E-10   PUB     = 9.411793E-25
+PVSAT   = 2E3            PETA0   = -1E-4          PKETA   = -1.356792E-3    )
*
.MODEL pmos PMOS (LEVEL   = 49 hdif = 0.25e-6 acm =3 
+VERSION = 3.1            TNOM    = 27             TOX     = 4.2E-9
+XJ      = 1E-7           NCH     = 4.1589E17      VTH0    = -0.4220357
+K1      = 0.5813738      K2      = 0.0303955      K3      = 0
+K3B     = 11.3426872     W0      = 1E-6           NLX     = 9.876034E-8
+DVT0W   = 0              DVT1W   = 0              DVT2W   = 0
+DVT0    = 0.5131166      DVT1    = 0.2665264      DVT2    = 0.1
+U0      = 120.5316596    UA      = 1.645481E-9    UB      = 1E-21
+UC      = -1E-10         VSAT    = 2E5            A0      = 1.671928
+AGS     = 0.3934127      B0      = 1.830733E-6    B1      = 4.739218E-6
+KETA    = 0.0202801      A1      = 0.1976849      A2      = 0.5787213
+RDSW    = 265.2609374    PRWG    = 0.5            PRWB    = -0.2145086
+WR      = 1              WINT    = 0              LINT    = 2.176517E-8
+XL      = -2E-8          XW      = -1E-8          DWG     = -4.223522E-8
+DWB     = 7.670464E-9    VOFF    = -0.096172      NFACTOR = 2
+CIT     = 0              CDSC    = 2.4E-4         CDSCD   = 0
+CDSCB   = 0              ETA0    = 0.023671       ETAB    = -0.3005133
+DSUB    = 1.2320494      PCLM    = 2.2844319      PDIBLC1 = 4.836921E-3
+PDIBLC2 = 0.0442167      PDIBLCB = -1E-3          DROUT   = 9.991187E-4
+PSCBE1  = 1.732893E9     PSCBE2  = 5E-10          PVAG    = 14.9616148
+DELTA   = 0.01           RSH     = 7.6            MOBMOD  = 1
+PRT     = 0              UTE     = -1.5           KT1     = -0.11
+KT1L    = 0              KT2     = 0.022          UA1     = 4.31E-9
+UB1     = -7.61E-18      UC1     = -5.6E-11       AT      = 3.3E4
+WL      = 0              WLN     = 1              WW      = 0
+WWN     = 1              WWL     = 0              LL      = 0
+LLN     = 1              LW      = 0              LWN     = 1
+LWL     = 0              CAPMOD  = 2              XPART   = 0.5
+CGDO    = 6.6E-10        CGSO    = 6.6E-10        CGBO    = 1E-12
+CJ      = 1.183858E-3    PB      = 0.8534482      MJ      = 0.4124158
+CJSW    = 2.066263E-10   PBSW    = 0.6189346      MJSW    = 0.2893774
+CJSWG   = 4.22E-10       PBSWG   = 0.6189346      MJSWG   = 0.2893774
+CF      = 0              PVTH0   = 2.308546E-3    PRDSW   = 13.6874174
+PK2     = 2.657069E-3    WKETA   = 2.467864E-3    LKETA   = -2.56649E-3
+PU0     = -1.846164      PUA     = -8.06063E-11   PUB     = 1E-21
+PVSAT   = -50            PETA0   = 1E-4           PKETA   = 2.794471E-3     )
*
.endl
